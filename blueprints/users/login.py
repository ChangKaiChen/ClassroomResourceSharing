from . import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, LoginManager, UserMixin
from extensions import User, db
# from models import Students


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = User('cck')
        login_user(user)
        return redirect('/index')
