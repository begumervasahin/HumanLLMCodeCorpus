import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
class DB:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def add_or_update_user(self, user):
        existing_user = self.session.query(User).filter(User.email == user.email).first()
        if existing_user:
            existing_user.name = user.name
        else:
            self.session.add(user)
        self.session.commit()
if __name__ == "__main__":
    DATABASE_URL = os.getenv("DATABASE_URL")
    db = DB(DATABASE_URL)
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
    Base.metadata.create_all(db.engine)