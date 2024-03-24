from . import resource_bp
from quart import send_file
from quart_auth import login_required


@resource_bp.route('/download/<file>')
@login_required
async def download(file):
    return await send_file(f'{file}', as_attachment=True)