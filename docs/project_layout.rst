============================
Layout and project structure
============================

.. Note::

   This needs some work.


This covers the layout and structure of Fredrik projects. We also talk
about some of the decisions we made. It's high level. For more
details, read through the skeleton code that
``fredrik-cmd createproject ... creates.

Here's the layout::

    # Project documentation
    ./CONTRIBUTORS
    ./LICENSE
    ./README.rst

    # Script for running project commands
    ./manage.py

    # File specifying all dependencies for this project
    ./requirements.txt

    # Project code directory
    ./PROJECTMODULE

    # Project scaffolding files -- you probably don't need to
    # fiddle with these
    ./PROJECTMODULE/__init__.py
    ./PROJECTMODULE/database.py
    ./PROJECTMODULE/errors.py
    ./PROJECTMODULE/utils.py
    ./PROJECTMODULE/wsgi.py

    # Project configuration files
    ./PROJECTMODULE/settings.py
    ./PROJECTMODULE/settings_local.py-dist

    # This is where the bulk of your project code goes
    ./PROJECTMODULE/main.py
    ./PROJECTMODULE/models.py

    # Template files and directories
    ./PROJECTMODULE/templates
    ./PROJECTMODULE/templates/base.html
    ./PROJECTMODULE/templates/index.html
    ./PROJECTMODULE/templates/errors
    ./PROJECTMODULE/templates/errors/base.html
    ./PROJECTMODULE/templates/errors/404.html
    ./PROJECTMODULE/templates/errors/500.html

    # Directory and scaffolding for your tests
    ./PROJECTMODULE/tests
    ./PROJECTMODULE/tests/__init__.py


The project consists of some project scaffolding, templates, configuration
and your code.


Configuration
=============

Project configuration is done in ``PROJECTMODULE/settings.py`` and
server-specific configuration that differs between instances of your
site should be done in ``PROJECTMODULE/settings_local.py``.

There's a ``settings_local.py-dist`` template that you can copy over to
start this file.


Database and models
===================

We're using `sqlalchemy <http://www.sqlalchemy.org/>`_.

By default, it uses sqlite. You can use something else---you just have
to configure it.

Models go in ``PROJECTMODULE/models.py``.

There's no migration system set up. Any time you modify the schema,
you'll have to wipe the database and start over.

To create the database, do::

    $ python manage.py db_create


View code
=========

View code is at the bottom of ``PROJECTMODULE/main.py``.


Templates
=========

Templates are all in ``PROJECTMODULE/templates/``.

The base template is ``base.html``.

Error templates are in ``errors/``.


Javascript
==========

Javascript files are in ``PROJECTMODULE/static/js/``.

`Twitter Bootstrap <http://twitter.github.io/bootstrap/>`_ is installed.

`JQuery <https://jquery.org/>`_ is installed.

Any Javascript you want to do should go in ``PROJECTMODULE.js``. If you
want to break this into multiple files, make sure to specify the files in
your templates.


CSS
===

CSS files are in ``PROJECTMODULE/static/css/``.

`Twitter Bootstrap <http://twitter.github.io/bootstrap/>`_ is installed.

Any CSS you want to do should go in ``PROJECTMODULE.css``. If you want
to break this into multiple files, make sure to specify the files in
your templates.
