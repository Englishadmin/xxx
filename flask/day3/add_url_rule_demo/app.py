from flask import Flask,url_for

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELODE':True
})

@app.route('/')
def hello_world():
    print(url_for('hello_world'))
    return 'Hello World!'
def my_list():
    return "我是大乘高手"
app.add_url_rule('/list/',view_func=my_list)

if __name__ == '__main__':
    app.run(port=5002)
