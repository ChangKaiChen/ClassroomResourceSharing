from . import teacher_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@teacher_bp.route('/editor', methods=['POST', 'GET'])
@login_required
def editor():
    return render_template('teachers/editor.html', title='编辑文件')