======
README
======

Command line for generating Flask app scaffolding suitable for
fast-and-furious hack-days.

:code:          https://github.com/willkg/fredrik/
:issues:        https://github.com/willkg/fredrik/issues
:license:       BSD 3-clause
:documentation: http://fredrik.rtfd.org/


Install
=======

Install it with pip::

    $ pip install fredrik


Install it with pip from git::

    $ pip install https://github.com/willkg/fredrik/zipball/master#egg=fredrik


Install it from source::

    $ git clone git://github.com/willkg/fredrik/
    $ cd fredrik
    $ python setup.py install


Run
===

To create a Flask project using fredrik::

    $ fredrik-cmd createproject <PROJECTNAME>


That will create the project directory with all the files for the skeleton
with items marked TODO that need to be done.
