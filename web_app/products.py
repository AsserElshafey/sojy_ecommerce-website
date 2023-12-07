from flask import Blueprint, request, render_template
from .models import Product
from . import db


product = Blueprint('product', __name__)


@product.route('/admin', strict_slashes=False, methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('product_name')
        quantity = request.form.get('product_quantity')
        price = request.form.get('product_price')
        details = request.form.get('product_details')
        new_product = Product(name=name, quantity=quantity,
                              price=price, details=details)
        db.session.add(new_product)
        db.session.commit()
        print("New product added")
    products = Product.query.all()
    return render_template('admin.html', products=products)
