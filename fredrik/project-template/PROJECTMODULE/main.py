import os

from flask import Flask, send_from_directory


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

# Register views
from PROJECTMODULE import views
app.register_blueprint(views.mod)


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
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')
