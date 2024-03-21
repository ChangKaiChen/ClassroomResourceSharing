from blueprints.courses import course_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@course_bp.route('/teaching-programme')
@login_required
def teaching_programme():
    return render_template('course/introduction/teaching-programme.html', title='教学大纲')