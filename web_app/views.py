from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/", strict_slashes=False)
def home():
    return render_template('index.html')


@views.route("/shop", strict_slashes=False)
def shop():
    return render_template('shop.html')
