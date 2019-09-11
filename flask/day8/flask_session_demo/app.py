from flask import Flask,session
from flask_script import Manager
app = Flask(__name__)
app.config['SECRET_KEY']='jsadhfsjdf7653784'
manager =Manager(app)
@app.route('/')
def index():
    session['username']='寒烟柔'
    session['user_id']='战斗法师'
    print(type(session))
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    username=session.get('username')
    user_id=session.get('user_id')
    print(username,user_id)
    return username or "没有任何session"

@app.route('/del_session/')
def del_session():
    session.clear()
    return '退出成功'

if __name__ == '__main__':
  manager.run()
