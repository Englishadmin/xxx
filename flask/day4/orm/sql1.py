from sqlalchemy import create_engine

hostname='127.0.0.1'
port=3306
database='professional_master'
username='root'
password='123456'

# dialect+driver://username:password@host:port/database?charset=utf8
db_url='mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,hostname,port,database)

engine = create_engine(db_url)
with engine.connect() as con:
    rs=con.execute('select 10')
    print(rs.fetchone())