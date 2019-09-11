from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    context={
        'name':'cx',
        'age':"18",
        'jingjie':"大乘",
        'country':'wuhan',
        'hobby':{
            'game':'王者荣耀',
            'tv':'全职高手'
    }
    }
    return render_template('index.html',**context)

@app.route('/test/')
def test():
    return render_template('test.html',username="cx",password="666")



@app.route('/login/<id>/')
def logins(id):
    return render_template('login.html',id=id)

@app.route('/urlfor/')
def urlfor():
    return render_template('urlfor.html')


if __name__ == '__main__':
    app.run()
