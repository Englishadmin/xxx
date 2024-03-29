from flask import Flask
from apps.user import user_bp
from apps.book import book_bp
from apps.movie import movie_bp


app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
app.register_blueprint(movie_bp)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port='5003')
