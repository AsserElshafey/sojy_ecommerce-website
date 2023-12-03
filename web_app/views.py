from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template('index.html')


@views.route("/shop")
def shop():
    return render_template('shop.html')


@views.route("/auth")
def auth():
    return render_template("login.html")
