from . import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_user, logout_user, login_required, current_user, AuthUser
# from models import Students


@user_bp.route('/login', methods=['POST', 'GET'])
async def login():
    if request.method == 'GET':
        return await render_template('users/login.html')
    else:
        user = AuthUser('cck')
        login_user(user)
        return redirect('/index')
