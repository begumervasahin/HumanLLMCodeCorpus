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
class DBManager:
    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.Session = sessionmaker(bind=self.engine)
    def add_or_update_user(self, user):
        with self.Session() as session:
            existing_user = session.query(User).filter(User.email == user.email).first()
            if existing_user:
                existing_user.name = user.name
                session.add(existing_user)
            else:
                session.add(user)
            session.commit()
def create_database_tables(db_manager):
    if not database_exists(db_manager.engine.url):
        create_database(db_manager.engine.url)
    Base.metadata.create_all(db_manager.engine)
if __name__ == "__main__":
    db_manager = DBManager()
    create_database_tables(db_manager)