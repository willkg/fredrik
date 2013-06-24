import os

from PROJECTMODULE.utils import truthiness


# Whether or not we're in DEBUG mode. DEBUG mode is good for
# development and BAD BAD BAD for production.
DEBUG = truthiness(os.environ.get('DEBUG', True))

# This is the url to the database.
# For a sqlite file-based database, use sqlite:///path/to/db
DATABASE = os.environ.get('DATABASE_URL', 'sqlite:///PROJECTMODULE_app.db')

# Set the SECRET_KEY in your settings_local.py file.

# TODO: Add project settings here..

# This imports settings_local.py thus everything in that file
# overrides what's in this file.
try:
    from PROJECTMODULE.settings_local import *
except ImportError:
    pass
