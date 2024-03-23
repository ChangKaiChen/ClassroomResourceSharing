from . import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, LoginManager, UserMixin
from extensions import User, db


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
