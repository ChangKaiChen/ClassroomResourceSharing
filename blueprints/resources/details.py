from sqlalchemy import select
import os
from . import resource_bp
from quart import request, render_template, redirect, session, url_for, jsonify, current_app
from quart_auth import login_required, current_user
from models import PublishedArticles


async def file_exists_in_static(file_name):
    for i in ['.rar', '.zip', '.7z']:
        absolute_file_path = os.path.join('static', 'uploads', f'{file_name}{i}')
        if os.path.exists(absolute_file_path):
            return i
    return None


@resource_bp.route('/resources/<id>', methods=['GET'])
@login_required
async def details(id):
    async with current_app.session_local() as session:
        existing_info = await session.execute(
            select(PublishedArticles).where(PublishedArticles.id == id)
        )
        existing_info = existing_info.scalar_one_or_none()
        if not existing_info:
            return jsonify({'success': False, 'msg': '未找到该文章'}), 200, {'ContentType': 'application/json'}
        title = existing_info.title
        content = existing_info.content
        time = existing_info.date
        author = existing_info.author
        existing_links = await session.execute(
            select(PublishedArticles).where(PublishedArticles.author == author)
        )
        existing_links = existing_links.scalars().all()
        links = [{
            "id": link.id,
            "author": link.author,
            "time": link.date,
            "title": link.title,
            "classification": link.category
        } for link in existing_links]
        file_extension = await file_exists_in_static(id)
        download_url = f'/download/static/download/{id}{file_extension}' if file_extension else None
    return await render_template('resources/details.html', title=title,
                                 image='/static/assets/images/avatar.jpg', time=time, author=author,
                                 content=content, links=links, download_url=download_url,
                                 username=current_user.auth_id)
