from sqlalchemy import select, or_
from models import Users
from . import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify, current_app
from quart_auth import login_user, logout_user, login_required, current_user, AuthUser


@user_bp.route('/login', methods=['POST', 'GET'])
async def login():
    if request.method == 'GET':
        return await render_template('users/login.html')
    else:
        async with current_app.session_local() as session:
            json = await request.get_json()
            username_or_email = json.get('username_or_email')
            password = json.get('password')
            existing_user = await session.execute(
                select(Users).where(or_(Users.username == username_or_email, Users.email == username_or_email))
            )
            existing_user = existing_user.scalar_one_or_none()
            if existing_user:
                if existing_user.password == password:
                    user = AuthUser(existing_user.username)
                    login_user(user)
                    return redirect('/index')
                else:
                    return jsonify({'success': False, 'msg': '密码错误！'}), 200, {
                        'ContentType': 'application/json'}
            else:
                return jsonify({'success': False, 'msg': '当前用户未注册！'}), 200, {'ContentType': 'application/json'}
