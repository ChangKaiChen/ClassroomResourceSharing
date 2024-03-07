from flask import render_template
from factory import create_app
from flask_login import login_required
from settings import DevelopmentConfig

app = create_app()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='首页')


if __name__ == '__main__':
    config = DevelopmentConfig
    app.run(debug=config.debug)
