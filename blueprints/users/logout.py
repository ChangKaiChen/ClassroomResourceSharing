from . import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_user, logout_user, login_required, current_user


@user_bp.route('/logout')
@login_required
async def logout():
    logout_user()
    return redirect('/login')
