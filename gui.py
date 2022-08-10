from abc import ABC, abstractmethod

 
class AuthorizationGUI(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def registration_form(self):
        pass

    @abstractmethod
    def login_form(self):
        pass

    @abstractmethod
    def success_page(self):
        pass

    @abstractmethod
    def show_error(self):
        pass