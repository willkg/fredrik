===================
Database and models
===================

We're using `sqlalchemy <http://www.sqlalchemy.org/>`_.

By default, it uses sqlite. You can use something else---you just have
to configure it.

Models go in ``PROJECTMODULE/models.py``.

To create the database, do::

    $ python manage.py db_create


There's no migration system set up. Any time you modify the schema,
you'll have to wipe the database and start over.
