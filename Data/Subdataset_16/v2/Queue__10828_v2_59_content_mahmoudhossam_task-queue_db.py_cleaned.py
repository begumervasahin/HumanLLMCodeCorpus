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
        b6 = os.getenv("DATABASE_URL")
        self.b7 = create_engine(b6)
        b8 = sessionmaker(bind=self.b7)
        self.b9 = b8()
    def fonk2(self, user):
        b10 = self.b9.query(class1).filter(class1.b5 == user.b5).first()
        if b10:
            b10.b4 = user.b4
            self.b9.add(b10)
        else:
            self.b9.add(user)
        self.b9.commit()
def fonk3():
    b11 = class2()
    if not database_exists(b11.b7.url):
        create_database(b11.b7.url)
    b1.metadata.create_all(b11.b7)
if b12 = = "__main__":
    fonk3()