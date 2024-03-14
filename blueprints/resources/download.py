from . import resource_bp
from flask import send_file
from flask_login import login_required


@resource_bp.route('/download/<file>')
@login_required
def download(file):
    return send_file(f'{file}', as_attachment=True)