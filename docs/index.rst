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

    fredrik-cmd createproject <PROJECTNAME>

It'll create the project skeleton in the current working directory. You
can run your project immediately::

    $ cd <PROJECTMODULE>
    $ mkvirtualenv <ENVNAME>
    $ pip install -r requirements.txt
    $ python manage.py runserver

Open browser and view ``http://127.0.0.1:5000/``.

Now you have a project skeleton for your new project!


Contents
========

.. toctree::
   :maxdepth: 1

   changelog
   license
   project_layout
   hacking
