======
README
======

Summary
=======


Install and configure
=====================

1. Create a virtual environment.

2. Install the dependencies::

       $ pip install -r requirements.txt

3. Read through the settings in ``PROJECTMODULE/settings_local.py``

   TODO: If there are any settings that need to be changed, mention
   that here.

4. Create the database::

       $ python manage.py db_create

   This creates the database based on the settings in
   ``PROJECTMODULE/settings_local.py``.


Run server
==========

Run::

    $ python manage.py runserver


Run tests
=========

Run::

    $ nosetests
