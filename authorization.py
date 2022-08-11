from database import Database, SQLAlchemyDB
from gui import FlaskHTMLAuthGUI


def check_password(database: Database, nickname: str, password: str) -> bool:
    user = database.get_user(nickname)
    if user["password"] == password:
        return True
    return False


def check_nickname(database: Database, nickname: str) -> bool:
    user = database.get_user(nickname)
    if len(user) > 0:
        return True
    return False


gui = FlaskHTMLAuthGUI()
database = SQLAlchemyDB("users.db")


def show_registration():
    gui.registration_form()


def show_login():
    gui.login_form()


def login_password_check(func):
    def wrapper(**kwargs):
        if check_nickname(kwargs["nickname"]):
            if check_password(kwargs["password"]):
                func()
            else:
                raise Exception(f"Wrong password for {kwargs['nickname']}.")
        else:
            raise Exception(f"User {kwargs['nickname']} not found.")


def create_user(nickname: str, password: str):
    if not check_nickname(nickname):
        database.add_user(nickname, password)
    else:
        raise Exception(f"User {nickname} already exists.")


@login_password_check
def delete_user(nickname: str, password: str):
    database.delete_user(nickname)


@login_password_check
def login_validation(nickname: str, password: str):
    gui.success_page()