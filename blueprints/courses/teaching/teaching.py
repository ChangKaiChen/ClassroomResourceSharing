from blueprints.courses import course_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@course_bp.route('/teaching')
@login_required
def teaching():
    chapters = [
        {'id': 1, 'title': '第一章'},
        {'id': 2, 'title': '第二章'},
        {'id': 3, 'title': '第三章'}
    ]
    chapter = request.args.get('chapter', default=1, type=int)
    return render_template('/course/teaching/teaching.html', title=f'第{chapter}章', pdf_path='/static/test.pdf', chapters=chapters, current=chapter)