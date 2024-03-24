from blueprints.courses import course_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_required


@course_bp.route('/related-videos')
@login_required
async def related_videos():
    videos = [
        {'id': 1, 'title': '视频1'},
        {'id': 2, 'title': '视频2'},
    ]
    video = request.args.get('video', default=1, type=int)
    return await render_template('/course/related_videos/related_videos.html', title=f'{videos[video - 1]["title"]}', video_path='/static/test.mp4', videos=videos, current=video)