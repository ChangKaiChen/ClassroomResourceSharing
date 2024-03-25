from sqlalchemy import select, func, or_
from . import resource_bp
from quart import request, render_template, jsonify, current_app
from quart_auth import login_required, current_user
from models import PublishedArticles


@resource_bp.route('/resources', methods=['POST', 'GET'])
@login_required
async def get_resources():
    if request.method == 'GET':
        return await render_template('resources/resources.html', title='资源列表', username=current_user.auth_id)
    async with current_app.session_local() as session:
        keyword = request.args.get('keyword', default=None, type=str)
        json = await request.get_json()
        page = json['page']
        per_page = 20
        query = select(PublishedArticles)
        if keyword:
            keyword_filter = or_(
                PublishedArticles.title.ilike(f'%{keyword}%'),
                PublishedArticles.author.ilike(f'%{keyword}%'),
                PublishedArticles.category.ilike(f'%{keyword}%')
            )
            query = query.filter(keyword_filter)
        total_count_result = await session.execute(select(func.count(PublishedArticles.id)).select_from(query.subquery()))
        total_count = total_count_result.scalar_one()
        total_pages = (total_count + per_page - 1) // per_page  # 计算总页数
        if int(page) > total_pages:
            return jsonify({'success': False, 'msg': '无更多数据'}), 200, {'ContentType': 'application/json'}
        query = query.order_by(PublishedArticles.date.desc()).offset((page - 1) * per_page).limit(per_page)
        result = await session.execute(query)
        articles = result.scalars().all()
        data = [{
            "id": article.id,
            "author": article.author,
            "date": article.date.strftime("%Y-%m-%d %H:%M"),
            "title": article.title,
            "category": article.category
        } for article in articles]
        return jsonify({'success': True, 'msg': '获取成功', 'data': data}), 200, {'ContentType': 'application/json'}
