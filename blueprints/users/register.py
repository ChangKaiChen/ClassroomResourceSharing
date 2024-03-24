import re
from sqlalchemy import select, or_
from . import user_bp
from quart import request, render_template, jsonify, current_app
import datetime
import random
import asyncio
import aiosmtplib
from email.mime.text import MIMEText
import email.utils
from models import Users

verification_codes = {}


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


@user_bp.route('/register', methods=['POST', 'GET'])
async def register():
    if request.method == 'GET':
        return await render_template('users/register.html')
    else:
        async with current_app.session_local() as session:
            try:
                json = await request.get_json()
                username = json.get('username')
                password = json.get('password')
                email = json.get('email')
                code = json.get('code')
                existing_user = await session.execute(
                    select(Users).where(or_(Users.username == username, Users.email == email))
                )
                existing_user = existing_user.scalar_one_or_none()
                if existing_user:
                    return jsonify({'success': False, 'msg': '用户或邮箱已存在'}), 200, {
                        'ContentType': 'application/json'}
                if username in verification_codes:
                    if datetime.datetime.now() > verification_codes[username]['expiry']:
                        return jsonify({'success': False, 'msg': '验证码已过期!'}), 200, {'ContentType': 'application/json'}
                    if code == verification_codes[username]['code'] and email == verification_codes[username]['email']:
                        new_user = Users(username=username, email=email, password=password)
                        session.add(new_user)
                        await session.commit()
                        return jsonify({'success': True, 'msg': '注册成功'}), 200, {'ContentType': 'application/json'}
                    else:
                        return jsonify({'success': False, 'msg': '验证码错误！'}), 200, {'ContentType': 'application/json'}
            except Exception as e:
                print(e)
                await session.rollback()
                return jsonify({'success': False, 'msg': '注册失败'}), 200, {'ContentType': 'application/json'}


@user_bp.route('/verification_code', methods=['POST'])
async def verification_code():
    json = await request.get_json()
    username = json.get('username')
    email = json.get('email')
    if not is_valid_email(email):
        return jsonify({'success': False, 'msg': '无效邮箱！'}), 200, {'ContentType': 'application/json'}
    if username in verification_codes and datetime.datetime.now() < verification_codes[username]['expiry']:
        return jsonify({'success': False, 'msg': '请勿重复请求！'}), 200, {'ContentType': 'application/json'}
    code = ''.join(random.choices('0123456789', k=6))
    expiry_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    verification_codes[username] = {'code': code, 'expiry': expiry_time, 'email': email}
    subject = "CourseWeb注册验证码"
    message = f"【CourseWeb】您好，验证码有效期3分钟，请不要泄露{code}"
    await send_email(subject, message, [email])
    return jsonify({'success': True, 'msg': '验证码发送成功！'}), 200, {'ContentType': 'application/json'}


async def clear_expired_verification_codes():
    while True:
        current_time = datetime.datetime.now()
        keys_to_delete = [key for key, value in verification_codes.items() if current_time >= value['expiry']]
        for key in keys_to_delete:
            del verification_codes[key]
        await asyncio.sleep(3600)


async def send_email(subject, message, target):
    sender_email = ""
    password = ""
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
