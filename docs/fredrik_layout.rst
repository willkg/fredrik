======================
Fredrik project layout
======================

Here's the layout of your new project::

    # Basic project stuff
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
    ./PROJECTMODULE/main.py
    ./PROJECTMODULE/utils.py
    ./PROJECTMODULE/wsgi.py

    # Project configuration files
    ./PROJECTMODULE/settings.py
    ./PROJECTMODULE/settings_local.py-dist

    # This is where the bulk of your project code goes
    ./PROJECTMODULE/views.py
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
