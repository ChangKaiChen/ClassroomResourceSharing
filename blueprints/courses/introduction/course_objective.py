from blueprints.courses import course_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_required, current_user


@course_bp.route('/course-objective')
@login_required
async def course_objective():
    return await render_template('/course/introduction/course-objective.html', title='课程目标', username=current_user.auth_id)