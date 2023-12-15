from flask import Blueprint, render_template, request
from .models import Product

views = Blueprint('views', __name__)


@views.route("/", strict_slashes=False)
def home():
    return render_template('index.html')


@views.route("/shop", strict_slashes=False)
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)


@views.route("/about", strict_slashes=False)
def about():
    return render_template('about.html')


@views.route("/contact_us", strict_slashes=False)
def contact_us():
    return render_template('contact.html')


@views.route("/sproduct", strict_slashes=False)
def sproduct():
    return render_template('sproduct.html')
