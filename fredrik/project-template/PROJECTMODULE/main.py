import os

from flask import Flask, render_template, url_for


# Create the app
app = Flask(__name__)

# Handle settings--look at os.environ first
settings_key = 'PROJECTMODULE_SETTINGS'.upper()
if os.environ.get(settings_key):
    app.config.from_envvar(settings_key, silent=True)
else:
    from PROJECTMODULE import settings
    app.config.from_object(settings)

# Register error handlers
from PROJECTMODULE.errors import register_error_handlers
register_error_handlers(app)

# Add the config to the context, so it's available in templates
@app.context_processor
def context_processor():
    return dict(config=app.config)

# Nix the db when tearing down
@app.teardown_request
def teardown_request(exception=None):
    # Remove the database session if it exists
    if hasattr(app, 'db_session'):
        app.db_session.close()

# Special rule for old browsers to correctly handle favicon.
app.add_url_rule(
    '/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))


# Import models here
from PROJECT_MODULE.models import Sample


# Views go below this line

@app.route('/')
def index():
    return render_template('index.html')

