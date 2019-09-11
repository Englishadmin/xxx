from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker

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
class Person(Base):
    __tablename__='person'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name= Column(String(20),nullable=False)
    age=Column(Integer)
    team=Column(String(50))
    def __str__(self):
        return "(Person(name:%s,age:%d,team:%s))" % (self.name,self.age,self.team)
# Base.metadata.drop_all()  #删除数据库
Base.metadata.create_all() #创建数据库

def add_data():
    p1 = Person(name="君莫笑",age="25",team="兴欣")
    p2 = Person(name="寒烟柔",age="22",team="兴欣")
    p3 = Person(name="沐雨橙风",age="23",team="嘉世")
    p4 = Person(name="逐烟霞",age="25",team="兴欣")
    session.add_all([p1,p2,p3,p4])
    # session.add(p1)
    session.commit()
def search_data():
    # all_person=session.query(Person).all()
    # for p in all_person:
    #     print(p)

    # all_person=session.query(Person).filter_by(name="寒烟柔").all()
    # for p in all_person:
    #     print(p)

    # all_person = session.query(Person).filter(Person.team=="嘉世").all()
    # for p in all_person:
    #     print(p)

    person = session.query(Person).first()
    print(person)
    session.commit()

def update_data():
    p1 = session.query(Person).first()
    p1.name='一叶知秋'
    session.commit()

def delete_data():
    p1=session.query(Person).first()
    session.delete(p1)
    session.commit()
if __name__=="__main__":
    # add_data()
    # search_data()
    # update_data()
    delete_data()