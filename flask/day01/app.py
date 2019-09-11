from flask import Flask, Response, render_template, redirect, request,url_for
from werkzeug.routing import BaseConverter

import uuid

app = Flask(__name__)  # 初始化一个flask实例


# 这是路由  访问这个地址就能看到下面函数的返回值
@app.route('/')
def hello_world():
    return '大乘已到，仙人可期'


@app.route('/adminstring/')
def adminstring():
    return '来了'


#
@app.route('/adminint/<int:user_id>/')
def adminint(user_id):
    return '来了:%s' % user_id


class TelephoneConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['tel'] = TelephoneConverter


@app.route('/telephone/<tel:user_id>/')
def admintel(user_id):

    return '电话:%s' % user_id


@app.route('/adminuuid/<uuid:test>/')
def adminuuid(test):
    return '大乘:%s' % test


@app.route('/article/<path:test>/')
def article(test):
    return "散仙:%s" % test


@app.route('/anyes/<any(shehuiyuan,xinyu):url_path>/<id>')
def detail(url_path, id):
    if url_path == 'shehuiyuan':
        return "详情:%s" % id
    else:
        return "地仙:%s" % id


@app.route('/about/')
def about():
    rep = Response(response='cx', status=404, content_type='text/html')
    return rep


@app.route('/signup/')
def login():
    return render_template('index2.html')

@app.route('/profile/')
def profile():
    name = request.args.get('name')
    if name:
        return render_template('profile.html')
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
