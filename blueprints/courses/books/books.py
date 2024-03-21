from blueprints.courses import course_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_required


@course_bp.route('/books')
@login_required
def books():
    books = [
        {'id': 1, 'title': '计算机网络基础'},
        {'id': 2, 'title': '计算机操作系统'},
    ]
    book = request.args.get('book', default=1, type=int)
    return render_template('/course/books/books.html', title=f'第{book}章', pdf_path='/static/test.pdf', books=books, current=book)