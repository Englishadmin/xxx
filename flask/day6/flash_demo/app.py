from flask import Flask,render_template,request,flash,redirect,url_for
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']='sadgy7634234hj'
app.config['BOOTSTRAP_SERVE_LOCAL']=True
manager = Manager(app)
bootstrap =Bootstrap(app)

class NameForm(FlaskForm):
    name=StringField('用户名',validators=[DataRequired()])
    submit = SubmitField("立即提交")

    def validate_name(self,field):
        if len(field.data)<6:
            raise ValidationError("用户名不能少于6个字符")


@app.route('/',methods=['GET','POST'])
def hello_world():
    form=NameForm()
    if form.validate():
        lastname = "醉卧沙场君莫笑，古来征战几人回"
        if lastname != form.name.data:
            flash('欢迎回到神之领域，愿有你的荣耀永不散场')
            return redirect(url_for('hello_world'))
    name = form.name.data
    return render_template('form.html',form=form,name=name)


if __name__ == '__main__':
    manager.run()
