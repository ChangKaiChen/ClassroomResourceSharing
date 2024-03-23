from flask import render_template
from factory import create_app
from flask_login import login_required
from settings import DevelopmentConfig
from blueprints.users.register import clear_expired_verification_codes
import asyncio

app = create_app()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='首页')


if __name__ == '__main__':
    config = DevelopmentConfig
    app.run(debug=config.debug)
    asyncio.run(clear_expired_verification_codes())
