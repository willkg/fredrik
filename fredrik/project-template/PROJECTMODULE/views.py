from flask import Blueprint, render_template

# TODO: Import models here
from PROJECTMODULE.models import Sample


mod = Blueprint('main', __name__)


@mod.route('/')
def index():
    return render_template('index.html')
