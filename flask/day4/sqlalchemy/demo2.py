from sqlalchemy import create_engine,Integer,String,Column
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
# 创建一个orm模型，必须继承自sqlalchemy提供给我们的基类
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),nullable=False)
    age=Column(Integer)
    country=Column(String(50))
    def __str__(self):
        return "(User(name:%s,age:%d,country:%s))"%(self.name,self.age,self.country)

#将创建好的模型映射到数据库,映射以后，以后修改字段，不会重新映射
# Base.metadata.drop_all()
Base.metadata.create_all()

def add_data():
    u1=User(name="cx",age=18,country="wh")
    u2=User(name="cy",age=18,country="wh")
    u3=User(name="cz",age=18,country="wh")
    session.add_all([u1,u2,u3])
    session.commit()

def search_data():
    # all_user = session.query(User).all()
    # for a in all_user:
    #     print(a)

    # all_user = session.query(User).filter_by(name='cx').all()
    # for a in all_user:
    #     print(a)

    # all_user = session.query(User).filter(User.name=='cf')
    # for a in all_user:
    #     print(a)

    person = session.query(User).first()
    print(person)

def update_data():
    u1 = session.query(User).first()
    u1.name='cc'
    session.commit()

def delete_data():
    u1 = session.query(User).first()
    session.delete(u1)
    session.commit()


if __name__=="__main__":
    # add_data()
    # search_data()
    # update_data()
    delete_data()