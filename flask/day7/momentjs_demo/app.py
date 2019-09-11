from flask import Flask,render_template
from flask_moment import Moment# 导入类库
from flask_script import Manager
from datetime import datetime
app = Flask(__name__)
# app.config.update({
#     'DEBUG':True,
#     'TEMPLATES_AUTO_RELOAD':True
# })

manage = Manager(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/moment/')
def moments():
    publice_time=datetime.utcnow()
    return render_template('moment.html',publice_time=publice_time)

if __name__ == '__main__':
    manage.run()
