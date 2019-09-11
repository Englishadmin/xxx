from flask import Blueprint
book_bp = Blueprint('book',__name__,url_prefix='/book')

@book_bp.route("/list/")
def list():
    return '图书列表页面'

@book_bp.route("/detail/")
def detail():
    return '图书详情页面'