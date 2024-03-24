import asyncio
from hypercorn import Config
from quart import render_template
from factory import create_app
from quart_auth import login_required
from blueprints.users.register import clear_expired_verification_codes
from hypercorn.asyncio import serve


async def main():
    app = await create_app()

    @app.route('/')
    @app.route('/index')
    @login_required
    async def index():
        return await render_template('index.html', title='首页')
    config = Config()
    config.bind = ["127.0.0.1:5000"]
    config.loglevel = "info"
    await serve(app, config)
    await clear_expired_verification_codes()


if __name__ == '__main__':
    asyncio.run(main())
