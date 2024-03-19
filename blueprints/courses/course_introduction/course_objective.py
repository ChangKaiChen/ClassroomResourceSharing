from blueprints.courses import course_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@course_bp.route('/course-objective')
@login_required
def course_objective():
    return render_template('/course/course_introduction/course-objective.html', title='课程目标')