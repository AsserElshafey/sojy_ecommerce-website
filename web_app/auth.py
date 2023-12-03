from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login', strict_slashes=False)
def login():
    return render_template("login.html")


@auth.route('/logout', strict_slashes=False)
def logout():
    return "logout"
