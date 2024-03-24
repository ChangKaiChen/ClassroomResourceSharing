import datetime
import random
from . import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify
import aiosmtplib
from email.mime.text import MIMEText
import email.utils
import asyncio

verification_codes = {}


@user_bp.route('/verification_code', methods=['POST'])
async def verification_code():
    form = await request.form
    username = form.get('username')
    user_email = form.get('email')
    code = ''.join(random.choices('0123456789', k=6))
    expiry_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    verification_codes[username] = {'code': code, 'expiry': expiry_time, 'email': user_email}
    subject = "CourseWeb注册验证码"
    message = f"【CourseWeb】您好，验证码有效期3分钟，请不要泄露{code}"
    await send_email(subject, message, [user_email])
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
