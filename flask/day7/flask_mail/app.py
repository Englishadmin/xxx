from flask import Flask,render_template,current_app
import os
from threading import Thread
from flask_script import Manager
from flask_mail import Message,Mail
app = Flask(__name__)

app.config['MAIL_SERVER']=os.environ.get('MAIL_SERVER','smtp.163.com')
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME','cx15926878953@163.com')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD','19666894981016cx')

mail=Mail(app)
manager=Manager(app)
def async_send_mail(app,msg):
    with app.app_context():
        mail.send(message=msg)
@app.route('/')
def index():
    # msg=Message(subject="账户激活",recipients=['2592668397@qq.com'],sender=app.config['MAIL_USERNAME'])
    # msg.html='<h1>你好，有缘人</h1>'
    #
    # msg.body='君莫笑'
    # mail.send(message=msg)
    #
    # return '邮件已经发送'
    send_mail('2592668397@qq.com', '激活账户', 'activate', username="家彬")
    return '邮件已经发送'

def send_mail(to,sub,template,**kwargs):
    app = current_app
    # 创建邮件对象
    msg = Message(subject=sub, recipients=[to], sender=app.config['MAIL_USERNAME'])
    # 如果你是用浏览器访问 邮件
    msg.html = render_template(template + '.html', **kwargs)

    # 如果你是用客户端 来查看邮件
    msg.body = render_template(template + '.txt', **kwargs)
    thread = Thread(target=async_send_mail,args=[])
    mail.send(message=msg)


if __name__ == '__main__':
   manager.run()
