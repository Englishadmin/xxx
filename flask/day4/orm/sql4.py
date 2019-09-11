from sqlalchemy import (
    create_engine,Integer,String,Column,Enum,Float,
Boolean,DECIMAL,DateTime,Date,Time
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

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

class Article(Base):
    __tablename__="article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)
    def __str__(self):
        return "Article(title:%s,price:%s)" % (self.title,self.price)
Base.metadata.drop_all()
Base.metadata.create_all()

for x in range(99):
    article = Article(title='title%s' % x, price=random.randint(60, 100))
    session.add(article)
session.commit()


