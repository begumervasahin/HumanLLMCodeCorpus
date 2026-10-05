import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
b1 = declarative_base()
class class1(b1):
    b2 = "users"
    b3 = Column(Integer, primary_key=True)
    b4 = Column(String(50))
    b5 = Column(String(50), unique=True)
class class2:
    def fonk1(self):
        self.b6 = create_engine(os.getenv("DATABASE_URL"))
        self.b7 = sessionmaker(bind=self.b6)
    def fonk2(self, user):
        with self.b7() as session:
            b8 = session.query(class1).filter(class1.b5 == user.b5).first()
            if b8:
                b8.b4 = user.b4
                session.add(b8)
            else:
                session.add(user)
            session.commit()
def fonk3(b10):
    if not database_exists(b10.b6.url):
        create_database(b10.b6.url)
    b1.metadata.create_all(b10.b6)
if b9 = = "__main__":
    b10 = class2()
    fonk3(b10)