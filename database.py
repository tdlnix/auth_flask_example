from abc import ABC, abstractmethod


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