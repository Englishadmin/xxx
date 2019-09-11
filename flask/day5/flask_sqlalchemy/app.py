from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

hostname = '127.0.0.1'
port = 3306
database='database3'
username='root'
password='123456'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,hostname,port,database)

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__='user_model'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username =db.Column(db.String(50),nullable=False)
    def __repr__(self):
        return 'User(username:%s)'% self.username

class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =db.Column(db.String(50),nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user_model.id"))
    author = db.relationship("UserModel",backref="articles")

# db.drop_all()
# db.create_all()

# 添加数据
user = UserModel(username="君莫笑")
article = Article(title="title one")
article.author=user
db.session.add(user)
db.session.commit()

# 排序
# users = UserModel.query.order_by(UserModel.id.desc()).all()
# print(users)

# 修改数据
# users = UserModel.query.filter(UserModel.username=="君莫笑").first()
# users.username = "寒烟柔"
# db.session.commit()

# 删除数据
# users = UserModel.query.filter(UserModel.username=="寒烟柔").first()
# db.session.delete(users)
# db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
