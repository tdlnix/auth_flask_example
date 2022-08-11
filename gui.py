from abc import ABC, abstractmethod

from flask import render_template, Blueprint

 
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


blueprint = Blueprint('simple_page', __name__,
                                    template_folder='templates')
class FlaskHTMLAuthGUI():
    def __init__(self):
        pass

    def registration_form(self):
        pass

    @blueprint.route('/login')
    def login_form():
        return render_template("login.html")

    def success_page(self):
        pass

    def show_error(self):
        pass  


