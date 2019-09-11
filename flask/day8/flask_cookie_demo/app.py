from flask import Flask,request,Response
from flask_script import Manager
from datetime import datetime, timedelta

app = Flask(__name__)
manager=Manager(app)

@app.route('/')
def hello_world():
    resp=Response("千锋教育")
    # expires=datetime(year=2019,month=9,day=11,hour=9,minute=37,second=30)
    expires = datetime.now()+timedelta(days=30,hours=7)
    resp.set_cookie("username","君莫笑",expires=expires)
    return resp

if __name__ == '__main__':
    manager.run()
