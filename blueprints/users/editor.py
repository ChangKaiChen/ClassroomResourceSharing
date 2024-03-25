import os
from sqlalchemy import select, or_
from werkzeug.utils import secure_filename

from blueprints.users import user_bp
from quart import request, render_template, redirect, session, url_for, jsonify, current_app
from quart_auth import login_required, current_user
from models import PublishedArticles, Users


@user_bp.route('/editor', methods=['POST', 'GET'])
@login_required
async def editor():
    if request.method == 'GET':
        return await render_template('users/editor.html', title='编辑文件')
    async with current_app.session_local() as session:
        try:
            json = await request.form
            title = json.get('title')
            content = json.get('html')
            category = json.get('category')
            file = (await request.files).get('file')
            username_or_email = current_user.auth_id
            existing_user = await session.execute(
                select(Users).where(or_(Users.username == username_or_email, Users.email == username_or_email))
            )
            existing_user = existing_user.scalar_one_or_none()
            author = existing_user.username
            new_article = PublishedArticles(title=title, content=content, category=category, author=author)
            session.add(new_article)
            await session.commit()
            if file:
                filename = secure_filename(file.filename)
                file_extension = os.path.splitext(filename)[1]
                save_path = os.path.join('static', 'assets', 'uploads', f'{new_article.id}.{file_extension}')
                await file.save(save_path)
            return jsonify({'success': True, 'msg': '发布成功'}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            print(e)
            await session.rollback()
            return jsonify({'success': False, 'msg': '发布失败！'}), 200, {'ContentType': 'application/json'}
