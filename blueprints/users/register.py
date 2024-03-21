from . import user_bp
from flask import request, render_template, jsonify


@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('users/register.html')
    else:
        try:
            return jsonify({'success': True, 'message': '注册成功'}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            return jsonify({'success': False, 'message': '注册失败'}), 200, {'ContentType': 'application/json'}
