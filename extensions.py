from quart_auth import QuartAuth, login_user, logout_user, current_user
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

auth_manager = QuartAuth()
# auth_manager.login_view = 'users.login'  # TODO 重定向到登录页面


# TODO 数据库
Base = declarative_base()


async def init_db(app):
    DATABASE_URL = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_async_engine(DATABASE_URL, echo=True, connect_args={
        "connect_timeout": 10,
        "read_timeout": 20
    })
    SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    return SessionLocal
