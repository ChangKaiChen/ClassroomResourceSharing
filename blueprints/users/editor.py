from blueprints.users import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_required


@user_bp.route('/editor', methods=['POST', 'GET'])
@login_required
async def editor():
    return await render_template('users/editor.html', title='编辑文件')