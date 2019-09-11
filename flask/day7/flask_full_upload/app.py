from flask import Flask,render_template
import os
import random
from flask_script import Manager
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField
from flask_bootstrap import Bootstrap
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY']='asgd2374hgsdf7'
app.config['MAX_CONTENT_LENGTH']=8*1024*1024
app.config['UPLOADED_PHOTOS_DEST']=os.path.join(os.path.dirname(__file__),'uploads')
app.config['BOOTSTRAP_SERVE_LOCAL']=True
photos = UploadSet('photos',IMAGES)

configure_uploads(app,photos)

patch_request_class(app,size=None)
bootstrap = Bootstrap(app)
manager = Manager(app)

def random_string(length=20):
    base_str='1234567890qwertyuioplkjhgfdsazxcvbnm'
    return ''.join(random.choice(base_str) for i in range(length))

class UploadForm(FlaskForm):
    photo = FileField('头像上传',validators=[FileRequired('请选择文件'),FileAllowed(photos,message='只允许上传图片')])
    submit=SubmitField('立即上传')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/',methods=['GET','POST'])
def upload():
    img_url = None
    form=UploadForm()
    if form.validate():
        suffix = os.path.splitext(form.photo.data.filename)[1]
        filename = random_string()+suffix
        photos.save(form.photo.data,name=filename)
        pathname = os.path.join(app.config['UPLOADED_PHOTOS_DEST'],filename)
        img = Image.open(pathname)
        img.thumbnail((128,128))
        img.save(pathname)

        img_url=photos.url(filename)
    return render_template('index.html',form=form,img_url=img_url)

if __name__ == '__main__':
    manager.run()
