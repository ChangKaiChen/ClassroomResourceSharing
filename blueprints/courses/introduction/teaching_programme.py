from blueprints.courses import course_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_required


@course_bp.route('/teaching-programme')
@login_required
async def teaching_programme():
    return await render_template('course/introduction/teaching-programme.html', title='教学大纲')