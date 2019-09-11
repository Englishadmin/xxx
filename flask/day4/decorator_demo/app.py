from flask import Flask,render_template,request,redirect,url_for,views

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})
def login_required(func):
    def wrapper(*args,**kwargs):
        username = request.args.get('username')
        if username and username=='君莫笑':
            return func(*args,**kwargs)
        return redirect(url_for('login'))
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/profile/')
@login_required
def profile():
    return '个人中心页面'

class SettingView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '个人设置页面'
app.add_url_rule('/settings/',view_func=SettingView.as_view('settings'))
if __name__ == '__main__':
    app.run(port=5002)
