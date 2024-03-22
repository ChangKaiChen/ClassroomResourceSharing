from blueprints.courses import course_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@course_bp.route('/related-videos')
@login_required
def related_videos():
    videos = [
        {'id': 1, 'title': '视频1'},
        {'id': 2, 'title': '视频2'},
    ]
    video = request.args.get('video', default=1, type=int)
    return render_template('/course/related_videos/related_videos.html', title=f'{videos[video - 1]["title"]}', pdf_path='/static/test.pdf', videos=videos, current=video)