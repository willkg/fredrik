import os
import os.path
import string
import sys
from optparse import OptionParser

from fredrik import __version__


USAGE = '%prog [options] [command] [command-options]'
VERSION = '%prog ' + __version__


def build_parser(usage):
    parser = OptionParser(usage=usage, version=VERSION)
    return parser


DIGIT_TO_WORD = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
    }


def clean_project_module(s):
    s = s.lower()

    s = ''.join([char for char in s
                 if char in string.ascii_letters + string.digits])

    if s[0] in string.digits:
        s = DIGIT_TO_WORD[s[0]] + s[1:]

    return s


def err(s):
    sys.stderr.write(s + '\n')


def todo(command, argv):
    parser = build_parser('%prog todo')

    (options, args) = parser.parse_args(argv)

    # TODO: Add the fact you can specify a directory to the help.

    if len(args) > 0:
        project_dir = args[0]
    else:
        project_dir = '.'

    project_dir = os.path.abspath(project_dir)

    # Go through all the text files (.txt, .rst, .py, .js, ...)
    # and print out TODO lines.
    for root, dirs, files in os.walk(project_dir):
        for fn in files:
            fn = os.path.join(root, fn)

            if not fn.endswith(('.rst', '.txt', '.js', '.css', '.py')):
                continue

            fp = open(fn, 'r')
            lines = fp.readlines()
            fp.close()

            output = []

            for i, line in enumerate(lines):
                if 'TODO' not in line:
                    continue

                output.append('{0}: {1}'.format(i + 1, line.strip()))

            if output:
                print ''
                print fn
                print '\n'.join(output)


def create(command, argv):
    parser = build_parser('%prog create <PROJECTNAME>')
    parser.add_option(
        '--noinput',
        action='store_true',
        default=False,
        help='runs fredrik without requiring input')

    (options, args) = parser.parse_args(argv)

    if not args:
        err('ERROR: You must provide a project name.')
        return 1

    project_name = args[0]
    project_module = clean_project_module(project_name)

    if not options.noinput:
        # Ask them for project module name and then double-check it's
        # valid.
        new_project_module = raw_input(
            'Python module name for your project: [{0}] '.format(
                project_module))
    else:
        new_project_module = project_module

    new_project_module = new_project_module.strip()
    if not new_project_module:
        new_project_module = project_module

    if new_project_module != clean_project_module(new_project_module):
        err('ERROR: "{0}" is not a valid Python module name.'.format(
                new_project_module))
        return 1

    project_module = new_project_module
    project_dir = os.path.abspath(project_module)

    if os.path.exists(project_dir):
        err('ERROR: Cannot create "{0}"--something is in the way.'.format(
                project_dir))
        return 1

    # Walk the project-template and create all files and directories
    # replacing:
    #
    # * PROJECTMODULE -> project_module

    project_template_dir = os.path.join(os.path.dirname(__file__),
                                        'project-template')

    for root, dirs, files in os.walk(project_template_dir):
        rel_root = root[len(project_template_dir) + 1:]

        for f in files:
            source = os.path.join(root, f)
            dest = os.path.join(project_dir, rel_root, f)
            dest = dest.replace('PROJECTMODULE', project_module)

            if not os.path.exists(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))

            fp = open(source, 'rb')
            data = fp.read()
            fp.close()

            data = data.replace('PROJECTMODULE', project_module)

            fp = open(dest, 'wb')
            fp.write(data)
            fp.close()

            print 'create file: {0}'.format(dest)

    print 'Done!'
    print ''
    print 'Gah! What next?'
    print ''
    print 'There are a series of TODO lines in the code. You can do:'
    print ''
    print '    fredrik-cmd todo'
    print ''
    print 'to list them. You should skim the Fredrik docs including'
    print 'project layout at:'
    print ''
    print '    http://fredrik.readthedocs.org/en/latest/'
    print ''
    print 'Good luck!'
    return 0


HANDLERS = (
    ('create', create, 'Creates a new fredrik project.'),
    ('todo', todo, 'Lists todo items in a fredrik project.'),
    )


def cmdline_handler(scriptname, argv):
    print '%s version %s' % (scriptname, __version__)

    # TODO: Rewrite using subparsers.
    handlers = HANDLERS

    if not argv or '-h' in argv or '--help' in argv:
        parser = build_parser('%prog [command]')
        parser.print_help()
        print ''
        print 'Commands:'
        for cmd, _, hlp in handlers:
            print '  %-14s %s' % (cmd, hlp)
        return 0

    if '--version' in argv:
        # We've already printed the version, so we can just exit.
        return 0

    command = argv.pop(0)
    for (cmd, fun, hlp) in handlers:
        if cmd == command:
            return fun(command, argv)

    err('Command "{0}" does not exist.'.format(command))
    for cmd, fun, hlp in handlers:
        err('  %-14s %s' % (cmd, hlp))
    return 1
