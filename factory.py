from quart import Quart, redirect, url_for
from os import urandom
import settings
from blueprints.resources import resource_bp
from blueprints.courses import course_bp
from blueprints.users import user_bp
from extensions import auth_manager, init_db
from quart_auth import AuthUser, Unauthorized


async def create_app():
    app = Quart(__name__, template_folder="templates", static_folder="static", static_url_path="/static")

    # TODO 加载配置
    app.config.from_object(settings.DevelopmentConfig)
    # TODO 注册蓝本
    app.session_local = await init_db(app)
    app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(course_bp)

    @app.errorhandler(Unauthorized)
    async def redirect_to_login(*_):
        return redirect(url_for("users.login"))
    app.secret_key = urandom(66)
    # TODO 初始化配置
    auth_manager.init_app(app)

    return app
