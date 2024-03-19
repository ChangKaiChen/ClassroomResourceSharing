from flask import Blueprint

course_bp = Blueprint('courses', __name__)

from .course_introduction import course_objective
from .course_introduction import teaching_programme