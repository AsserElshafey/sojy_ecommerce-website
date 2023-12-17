from flask import Blueprint, request, render_template, url_for, redirect, session
from werkzeug.utils import secure_filename
from .models.product import Product
from .models.cart import Cart
from .models.user import User
from flask_login import current_user
import os
from . import db

product = Blueprint('product', __name__)


@product.route('/admin', strict_slashes=False, methods=['GET', 'POST'])
def admin():
    products = Product.query.all()
    return render_template('admin.html', products=products)


@product.route('/add_product', strict_slashes=False, methods=['POST'])
def add_product():
    name = request.form.get('product_name')
    quantity = request.form.get('product_quantity')
    price = request.form.get('product_price')
    details = request.form.get('product_details')
    #### IMAGE #####
    pic = request.files['pic']
    if not pic:
        return "No pic uploaded", 400
    filename = secure_filename(pic.filename)
    from . import create_app
    app = create_app()
    pic.save(os.path.join(app.root_path,
             app.config['UPLOAD_FOLDER'], filename))
    if request.form.get('featured'):
        featured = 1
    else:
        featured = 0
    print(featured)
    new_product = Product(name=name, quantity=quantity,
                          price=price, details=details, featured=featured, image=filename)
    db.session.add(new_product)
    db.session.commit()
    print("New product added")
    return redirect('/admin')


@product.route('/update_product/<int:id>', strict_slashes=False, methods=['POST'])
def update_product(id):
    fetched_product = Product.query.get_or_404(int(id))
    fetched_product.name = request.form.get('product_name')
    fetched_product.quantity = request.form.get('product_quantity')
    fetched_product.price = request.form.get('product_price')
    fetched_product.details = request.form.get('product_details')
    fetched_product.featured = request.form.get('featured')
    if request.form.get('featured'):
        fetched_product.featured = 1
    else:
        fetched_product.featured = 0
    db.session.commit()
    print("product updated")
    products = Product.query.all()
    return render_template('admin.html', products=products)


@product.route('/delete_product/<int:id>', strict_slashes=False, methods=['POST'])
def delete_product(id):
    fetched_product = Product.query.get_or_404(int(id))
    db.session.delete(fetched_product)
    db.session.commit()
    print("product deleted")
    products = Product.query.all()
    return render_template('admin.html', products=products)

#### Cart ######


@product.route('/add_to_cart/<int:id>', strict_slashes=False, methods=['POST'])
def add_to_cart(id):

    product = Product.query.get(int(id))
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

    product.cart = cart
    db.session.add(cart)
    db.session.add(product)
    db.session.commit()
    print(cart)
    return render_template('cart.html', cart=cart)
