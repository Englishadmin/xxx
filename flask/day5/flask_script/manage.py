from flask_script import Manager
from app import app

manager = Manager(app)

@manager.command
def greet():
    print("hello")

@manager.option("-u","--username",dest="username")
@manager.option("-a","--age",dest="age")
def add_user(username,age):
    print("你的姓名:%s,您的年龄:%s"%(username,age))
if __name__ == "__main__":
    manager.run()

