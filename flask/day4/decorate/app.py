from flask import Flask,render_template,request,views,url_for,redirect

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

def login_required(func):
    def wrapper(*args,**kwargs):
        username = request.args.get('username')
        if username and username == '君莫笑':
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/profile/')
@login_required
def profile():
    return '剑之所指的地方，就是我们的荣耀'

class SettingView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '欢迎回到神之领域，愿有你的荣耀永不散场'
app.add_url_rule('/settings/',view_func=SettingView.as_view('settings'))


if __name__ == '__main__':
    app.run(port=5001)
