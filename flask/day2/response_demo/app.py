from flask import Flask,Response,render_template,request,redirect,url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config['DEBUG']=True

class TelConverter(BaseConverter):
    regex = '1[3-9]\d{9}'
app.url_map.converters['tel']=TelConverter

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/admins/<tel:telephone>/')
def admin(telephone):
    return "欢迎来到管理后台 %s" % telephone

@app.route('/about/')
def about():
    rep=Response(response="我是大乘高手",status='509',content_type='text/html;charset=utf-8')
    return rep

@app.route('/signin/')
def login():
    return render_template('index.html')

@app.route('/profile/')
def profile():
    name= request.args.get('name')
    if name:
        return render_template('profile.html')
    else:
        return redirect(url_for('login'))





if __name__ == '__main__':
    app.run(port=5001)
