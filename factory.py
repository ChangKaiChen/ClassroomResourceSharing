from flask import Flask
from sqlalchemy import text
from os import urandom
from extensions import db
import settings
from blueprints.students import student_bp
from blueprints.teachers import teacher_bp
from extensions import login_manager


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")

    # TODO 加载配置
    app.config.from_object(settings.DevelopmentConfig)
    # TODO 注册蓝本
    app.register_blueprint(student_bp)
    app.register_blueprint(teacher_bp)
    app.secret_key = urandom(66)
    # TODO 初始化配置
    login_manager.init_app(app)
    db.init_app(app)

    return app
