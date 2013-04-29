#!/usr/bin/env python
import os
import subprocess

from flask.ext.script import Manager

from PROJECTMODULE.database import create_all
from PROJECTMODULE.wsgi import app


manager = Manager(app)

app_path = os.path.join(os.path.dirname(__file__), 'PROJECTMODULE')
db_url = app.config.get('DATABASE_URL')


def call_command(cmd, verbose=False):
    if verbose:
        print cmd
    subprocess.call(cmd)


@manager.command
def db_create():
    """Create the database"""
    create_all(app)
    print 'Database created: {0}'.format(app.config['DATABASE_URL'])


if __name__ == '__main__':
    manager.run()
