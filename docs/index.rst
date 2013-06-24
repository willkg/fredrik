=======
Fredrik
=======

Fredrik was created to make it easy to build scaffolding for a Flask app
that's suitable for hack-days. It's just enough to get going quickly.

If you're looking for something more serious, checkout `buchner
<http://buchner.rtfd.org/>`_.

:code:          https://github.com/willkg/fredrik/
:issues:        https://github.com/willkg/fredrik/issues
:license:       BSD 3-clause
:documentation: http://fredrik.rtfd.org/


Quickstart
==========

This covers how to get up and running with Fredrik.

Set it up system-wide since you'll use it to create new Flask projects.

Run::

    pip install fredrik

After you install it, you can use Fredrik to create new Flask-based
projects::

    fredrik-cmd create <PROJECTNAME>

It'll create the project skeleton in the current working directory. You
can run your project immediately::

    $ cd <PROJECTMODULE>
    $ mkvirtualenv <ENVNAME>
    $ pip install -r requirements.txt
    $ python manage.py runserver

Open browser and view ``http://127.0.0.1:5000/``.

Now you have a project skeleton for your new project!

Oh, but wait---wtf do you do now?

1. Read, skim or vaguely flip through these docs which cover the
   project layout and neato things like that!
2. Read your new project README.rst.
3. Run::

       fredrik-cmd todo

   which lists all the TODO items in your project.


Contents
========

Documentation for Fredrik:

.. toctree::
   :maxdepth: 1

   changelog
   license
   hacking

Documentation for projects created with Fredrik:

.. toctree::
   :maxdepth: 1

   fredrik_intro
   fredrik_layout
   fredrik_configuration
   fredrik_views
   fredrik_db
   fredrik_templates
   fredrik_static
