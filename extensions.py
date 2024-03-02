from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


class User(UserMixin):
    def __init__(self, username):
        self.id = username


login_manager = LoginManager()
login_manager.login_view = 'users.login'  # TODO 重定向到登录页面


@login_manager.user_loader
def load_user(user):
    return User(user)


# TODO 数据库
db = SQLAlchemy()
