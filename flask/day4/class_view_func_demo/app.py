from flask import Flask,views,render_template,request

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

class LoginView(views.MethodView):
    def __render(self,error=None):
        return render_template('login.html',error=error)
    def get(self):
        return self.__render()
    def post(self):
        username =request.form.get('username')
        password = request.form.get('password')
        if username=='君莫笑' and password=='123456':
            return '登陆成功'
        else:
            return self.__render(error="用户名或密码输入错误")

    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass
@app.route('/')
def hello_world():
    return 'Hello World!'

app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
if __name__ == '__main__':
    app.run(port=5002)
