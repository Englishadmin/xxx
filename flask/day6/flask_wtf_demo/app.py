from flask import Flask,render_template
from flask_wtf import FlaskForm#导入表单基类
from wtforms import StringField,SubmitField#导入字段类型
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY']='GAFSDJSXNSG4657python '
class RegisterForm(FlaskForm):
    name =StringField("用户名:",validators=[DataRequired()])
    submit=SubmitField("立即注册")
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods=['POST','GET'])
def register():
    name=None
    form = RegisterForm()
    if form.validate_on_submit():  #判断用户输入是否符合要求
        name=form.name.data    # 接收表单提交的内容
        form.name.data=''    # 提交之后将输入框清空
    return render_template('index.html',form=form,name=name)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
