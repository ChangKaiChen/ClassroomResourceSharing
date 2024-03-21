from flask import Blueprint

course_bp = Blueprint('courses', __name__)

from .introduction import course_objective
from .introduction import teaching_programme
from .teaching import teaching
from .books import books