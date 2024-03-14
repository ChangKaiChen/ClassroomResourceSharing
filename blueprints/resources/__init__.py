from flask import Blueprint

resource_bp = Blueprint('resources', __name__)
from . import resources
from . import details
from . import download
