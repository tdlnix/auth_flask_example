from abc import ABC, abstractmethod
import os

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session


class Database(ABC):
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def add_user(self, username, password):
        pass

    @abstractmethod
    def get_user(self, username):
        pass

    # Delete
    @abstractmethod  
    def delete_user(self, username):
        pass


class SQLAlchemyDB(Database):
    def __init__(self, path):
        path = os.path.join("sqlite:///", path)
        self.engine = create_engine(path, echo=True, future=True)
        self.Base = declarative_base()
        self.User = self.create_user_table()
        self.Base.metadata.create_all(self.engine)

    def create_user_table(self):
        class User(self.Base):
            __tablename__ = 'user_account'
            id = Column(Integer, primary_key=True)
            name = Column(String(20), nullable=False, unique=True)
            password = Column(String(80), nullable=False)
        return User

    def add_user(self, username, password):
        with Session(self.engine) as session:
            user = self.User(
                name=username,
                password=password)
            session.add(user)
            session.commit()

    def get_user(self, username):
        pass

    def delete_user(self, username):
        session = Session(self.engine)
        stmt = select(self.User).where(self.User.name.in_([username]))
        users = list(session.scalars(stmt))
        if len(users) > 0:
            user = list(session.scalars(stmt))[0]
            session.flush()
            session.delete(user)
            session.commit()


if __name__ == "__main__":
    db = SQLAlchemyDB("database.db")
    db.delete_user("user")
    db.add_user("user", "password")