from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

app.config['SECRET_KEY']='YWTRYAGSDHG3256'
app.config['BOOTSTRAP_SERVE_LOCAL']=True#在实例化bootstrap之前，设置使用本地文件,不需在官网下载
bootstrap = Bootstrap(app)



class LoginForm(FlaskForm):
    username=StringField("用户名",validators=[DataRequired()])
    password=PasswordField("密码名",validators=[DataRequired()])
    submit = SubmitField("立即登录")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(port=5001)
