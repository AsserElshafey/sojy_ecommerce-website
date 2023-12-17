from flask import Blueprint, render_template, request, session
from .models.product import Product
from .models.user import User
from .models.cart import Cart
from flask_login import current_user
from . import db

views = Blueprint('views', __name__)


@views.route("/", strict_slashes=False)
def home():
    featured_products = Product.query.filter_by(featured=1)
    print(session.get('id'))
    print(current_user.get_id())
    return render_template('index.html', featured=featured_products)


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


@views.route("/sproduct/<int:id>", strict_slashes=False)
def sproduct(id):
    sproduct = Product.query.get(int(id))
    featured_products = Product.query.filter_by(featured=1)
    return render_template('sproduct.html', sproduct=sproduct, featured=featured_products)


@views.route("/cart", strict_slashes=False)
def cart():
    if current_user.get_id() is None:
        if session.get('id'):
            user = User.query.get(session['id'])
            cart = Cart.query.filter_by(user_id=user.id).first()
            if not cart:
                cart = Cart(user_id=user.id)
        else:
            user = User()
            db.session.add(user)
            db.session.commit()
            session['id'] = user.id
            cart = Cart.query.filter_by(user_id=user.id).first()
            if not cart:
                cart = Cart(user_id=user.id)
    else:
        print(current_user.get_id())
        cart = Cart.query.filter_by(user_id=int(current_user.get_id())).first()

    return render_template('cart.html', cart=cart)


@views.route("/checkout", strict_slashes=False)
def checkout():
    return render_template('checkout.html')
