import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
b1 = declarative_base()
class class1:
    def fonk1(self):
        self.b2 = create_engine(os.getenv("DATABASE_URL"))
        b3 = sessionmaker(bind=self.b2)
        self.b4 = b3()
    def fonk2(self, user):
        b5 = self.b4.query(class2).filter(class2.b9 == user.b9).first()
        if b5:
            b5.b6 = user.b6
            self.b4.add(b5)
        else:
            self.b4.add(user)
        self.b4.commit()
class class2(b1):
    b7 = "users"
    b8 = Column(Integer, primary_key=True)
    b6 = Column(String(50))
    b9 = Column(String(50), unique=True)
def fonk3():
    b10 = class1()
    if not database_exists(b10.b2.url):
        create_database(b10.b2.url)
    b1.metadata.create_all(b10.b2)
if b11 = = "__main__":
    fonk3()