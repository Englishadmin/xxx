from sqlalchemy import (
    create_engine,Integer,String,Column,Enum,Float,
Boolean,DECIMAL,DateTime,Date,Time
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import enum
hostname='127.0.0.1'
port=3306
database='professional_master'
username='root'
password='123456'
db_url='mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,hostname,port,database)
engine=create_engine(db_url)
Base = declarative_base(engine)
# Session=sessionmaker(engine)
# session=Session()
session =sessionmaker(engine)()
class TagNum(enum.Enum):
    python = '君莫笑'
    linux = '寒烟柔'
    mysql = '韩文清'

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    price=Column(Float)
    is_delete = Column(Boolean)
    prices = Column(DECIMAL(10,2))
    tag = Column(Enum(TagNum))
    create_time=Column(DateTime)
    content = Column(LONGTEXT)
Base.metadata.create_all()

article = Article(prices=9999999.8888)
session.add(article)
session.commit()