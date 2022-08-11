from crypt import methods
from flask import Flask
from flask import request
import authorization as auth

from gui import blueprint


app = Flask("__name__")
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.register_blueprint(blueprint)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        auth.show_login()


app.run(debug=True)