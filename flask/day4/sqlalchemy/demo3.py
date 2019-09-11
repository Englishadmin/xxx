from sqlalchemy import create_engine,DECIMAL,Boolean,Float,Integer,Enum,Column
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)
Base =declarative_base(engine)

session=sessionmaker(engine)()


class TagNum(enum.Enum):
    python="python"
    linux="linux"
    mysql="mysql"

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    price=Column(Float)
    is_delete=Column(Boolean)
    prices = Column(DECIMAL(10,4))
    tag = Column(Enum(TagNum))
Base.metadata.create_all()

article=Article(prices=100000.9999)
session.add(article)
session.commit()