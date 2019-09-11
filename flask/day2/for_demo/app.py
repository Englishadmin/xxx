from flask import Flask, render_template

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    "TEMPLATES_AUTO_RELOAD": True
})


@app.route('/')
def hello_world():
    context = {
        'users': ['user1', 'user2', 'user3'],
        'person': {
            'name': "君莫笑",
            'age': 2700,
            'jingjie': '大乘中期'
        },
        'books': [
            {
                'name': '亘古大帝',
                'author': '陈辉',
                'price': 100
            },
            {
                'name': '人皇纪',
                'author': '没注意',
                'price': 108
            },
            {
                'name': '蛮荒记',
                'author': '我吃西红柿',
                'price': 88
            }
        ]
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(port=5001)
