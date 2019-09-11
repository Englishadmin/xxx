from flask import Flask
import flask

app = Flask(__name__)
app.config['DEBUG']=True
app.config['TEMPLATES_AUTO_RELOAD']=True

#　电影
movies = [
    {
        'id': '26287884',
        'title': u'追龙',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2499052494.webp',
        'rating': u'7.5',
        'comment_count': 33060,
        'authors': u'刘德华 / 张家辉 / 古天乐'

    },
    {
        'id': '34532',
        'title': u'羞羞的铁拳',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'rating': u'7.6',
        'comment_count': 39450,
        'authors': u'艾伦/马丽/沈腾'
    },
    {
        'id': '394558',
        'title': u'情圣',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2409022364.webp',
        'rating': u'6.3',
        'comment_count': 38409,
        'authors': u'肖央 / 闫妮 / 小沈阳'
    },
    {
        'id': '9384089',
        'title': u'全球风暴',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2501769525.webp',
        'rating': u'7.4',
        'comment_count': 4555,
        'authors': u'杰拉德·巴特勒/吉姆·斯特'
    },
    {
        'id': '26921827',
        'title': u'大卫贝肯之倒霉特工熊',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2408893200.webp',
        'rating': u'4.3',
        'comment_count': 682,
        'authors': u'汤水雨 / 徐佳琪 / 杨默'
    },
    {
        'id': '11211',
        'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2499792043.webp',
        'title': u'王牌特工2：黄金圈',
        'rating': u'7.3',
        'comment_count': 12000,
        'authors': u'科林·费尔斯 / 塔伦·埃格顿 / 朱丽安·摩尔'
    }
]

# 电视剧
tvs = [
    {
        'id': '292843',
        'title': u'芈月传',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2196596996.webp',
        'rating': u'8.2',
        'comment_count': 23456,
        'authors': u'孙俪 / 刘涛 / 黄轩 / 马苏 /'
    },
    {
        'id': '9498327',
        'title': u'孤芳不自赏',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2407425119.jpg',
        'rating': u'3.7',
        'comment_count': 8493,
        'authors': u'钟汉良 / 杨颖 / 甘婷婷 / 孙艺洲 / 亓航 /'
    },
    {
        'id': '26685451',
        'title': u'全职高手',
        'thumbnail': u'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2563437048.webp',
        'rating': u'9.9',
        'comment_count': 345,
        'authors': u' 杨洋 / 江疏影 / 赖雨濛 / 李沐宸 / 蝴蝶蓝 /'
    },
    {
        'id': '235434',
        'title': u'九州缥缈录',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2562677270.webp',
        'rating': u'7.6',
        'comment_count': 25532,
        'authors': u'刘昊然 / 宋祖儿 / 张嘉译 /'
    },
    {
        'id': '48373095',
        'title': u'灵魂摆渡',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2172608583.webp',
        'rating': u'6.4',
        'comment_count': 2483,
        'authors': u'小吉祥天 / 于毅 / 肖茵/ 刘智扬 /'
    },
    {
        'id': '235434',
        'title': u'鬼吹灯之精绝古城',
        'thumbnail': u'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2404604903.webp',
        'rating': u'8.4',
        'comment_count': 49328,
        'authors': u'靳东 / 陈乔恩 / 赵达 / 付枚 / 金泽灏 /'

    }
]
# 这是首页
@app.route('/')
def index():
    context = {
        'movies': movies,
        'tvs': tvs
    }
    return flask.render_template('index.html',**context)

# 列表
@app.route('/list/<int:category>')
def item_list(category):
    # 如果category是等于1，就返回电影
    # 如果category是等于2，就返回电视剧
    # 否则就返回一个空数组
    items = []
    if category == 1:
        items = movies
    elif category == 2:
        items = tvs
    else:
        items = []

    return flask.render_template('list.html',items=items,category=category)
# 详情页
@app.route('/detail/<int:category>/<id>')
def detail(category,id):
    item = None
    if category == 1:
        for movie in movies:
            if movie['id'] == id:
                item = movie
                break
    elif category == 2:
        for tv in tvs:
            if tv['id'] == id:
                item = tv
                break

    return flask.render_template('detail.html',item=item)


if __name__ == '__main__':
    app.run(port=5001)
