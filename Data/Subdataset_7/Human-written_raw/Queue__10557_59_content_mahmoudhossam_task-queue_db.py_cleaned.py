import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import database_exists, create_database
b1 = declarative_base()
class class1:
    def fonk1(self):
        self.b2 = create_engine(os.getenv("DATABASE_URL"))
        b3 = sessionmaker(bind=self.b2)
        self.b4 = b3()
    def fonk2(self, user):
        b5 = (
            self.b4.query(class2).filter(class2.b6 = = user.b6).first()
        )
        if b5:
            b5.b7 = user.b7
            self.b4.fonk2(b5)
        else:
            self.b4.fonk2(user)
        self.b4.commit()
class class2(b1):
    b8 = "users"
    b9 = Column(Integer, primary_key=True)
    b7 = Column(String(50))
    b6 = Column(String(50), unique=True)
if b10 = = "__main__":
    b11 = class1()
    if not database_exists(b11.b2.url):
        create_database(b11.b2.url)
    b1.metadata.create_all(b11.b2)