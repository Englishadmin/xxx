from flask import Flask, render_template, request

from forms import RegisterForm,LoginForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})
app.config['SECRET_KEY']='523dgzxbchad'
app.config['BOOTSTRAP_SERVE_LOCAL']=True
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods=['GET','POST'])
def register():
    form =RegisterForm()
    if request.method=="GET":
        return render_template('register.html',form=form)
    else:
        form = RegisterForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'



@app.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=="GET":
        return render_template('login.html',form=form)
    else:
        form=LoginForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'

if __name__ == '__main__':
    app.run(port=5001)
