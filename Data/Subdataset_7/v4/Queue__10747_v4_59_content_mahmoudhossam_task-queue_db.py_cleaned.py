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
        b7 = sessionmaker(bind=self.b6)
        self.b8 = b7()
    def fonk2(self, user):
        b9 = self.b8.query(class1).filter(class1.b5 == user.b5).first()
        if b9:
            b9.b4 = user.b4
            self.b8.fonk2(b9)
        else:
            self.b8.fonk2(user)
        self.b8.commit()
if b10 = = "__main__":
    b11 = class2()
    if not database_exists(b11.b6.url):
        create_database(b11.b6.url)
    b1.metadata.create_all(b11.b6)