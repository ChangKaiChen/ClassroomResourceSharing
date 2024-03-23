import re

from . import user_bp
from flask import request, render_template, jsonify
import datetime
import random
import asyncio
import aiosmtplib
from email.mime.text import MIMEText
import email.utils

verification_codes = {}


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('users/register.html')
    else:
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            code = request.form.get('code')
            if username in verification_codes:
                if datetime.datetime.now() > verification_codes[username]['expiry']:
                    return jsonify({'success': False, 'msg': '验证码已过期!'})
                if code == verification_codes[username]['code'] and email == verification_codes[username]['email']:
                    return jsonify({'success': True, 'message': '注册成功'}), 200, {'ContentType': 'application/json'}
                else:
                    return jsonify({'success': False, 'msg': '验证码错误！'})
        except Exception as e:
            return jsonify({'success': False, 'message': '注册失败'}), 200, {'ContentType': 'application/json'}


@user_bp.route('/verification_code', methods=['POST'])
async def verification_code():
    json = request.get_json()
    username = json.get('username')
    email = json.get('email')
    if not is_valid_email(email):
        return jsonify({'success': False, 'msg': '无效邮箱！'})
    if username in verification_codes and datetime.datetime.now() < verification_codes[username]['expiry']:
        return jsonify({'success': False, 'msg': '请勿重复请求！'})
    code = ''.join(random.choices('0123456789', k=6))
    expiry_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    verification_codes[username] = {'code': code, 'expiry': expiry_time, 'email': email}
    subject = "CourseWeb注册验证码"
    message = f"【CourseWeb】您好，验证码有效期3分钟，请不要泄露{code}"
    await send_email(subject, message, [email])
    return jsonify({'success': True, 'msg': '验证码发送成功！'}), 200


async def clear_expired_verification_codes():
    while True:
        current_time = datetime.datetime.now()
        keys_to_delete = [key for key, value in verification_codes.items() if current_time >= value['expiry']]
        for key in keys_to_delete:
            del verification_codes[key]
        await asyncio.sleep(3600)


async def send_email(subject, message, target):
    sender_email = "cck@cck.serv00.net"
    password = "cck2004CCK"
    msg = MIMEText(message)
    msg['To'] = email.utils.formataddr(('尊敬的用户', ''))
    msg['From'] = email.utils.formataddr(('CourseWeb', sender_email))
    msg['Subject'] = subject
    await aiosmtplib.send(
        msg,
        hostname="mail2.serv00.com",
        port=465,
        local_hostname='CourseWeb',
        use_tls=True,
        username=sender_email,
        password=password,
        recipients=target
    )
