from flask import Flask
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
import transaction
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:pass@localhost:3306/test"
## db = SQLAlchemy(app)
db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()

class member(Base):
    __tablename__ = 'member'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    email = Column(String)

    def __init__(self,name):
        self.name = name


Base.metadata.create_all(db)
Session = sessionmaker(bind=db)
register(Session)
session = Session()


@app.route("/")
def f():
    # sql = 'select * from member'
    session.add(member("Tony"))
    sp = transaction.savepoint()
    # sp = transaction.savepoint()
    # db.engine.execute("insert into member (name) values ('YYYYYYYYYYYYY')")
    session.add(member("kiki"))
    session.add(member("1234"))
    # db.session.commit()
    try:
        session.add()
        transaction.commit()
        # db.session.commit()
        # db.session.rollback()
    except Exception as e:
        print(e)
        sp.rollback()
        transaction.commit()
        # transaction.abort()
        # sql = 'rollback'
        
    # for i in result:
    #     print(i)
    return "ok"


if __name__=="__main__":
    app.run(debug=True)