from flask import Blueprint, request, render_template


product = Blueprint('product', __name__)


@product.route('/admin', strict_slashes=False, methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('product_name')
        quantity = request.form.get('product_quantity')
        price = request.form.get('product_price')
        details = request.form.get('product_details')
        print(name)
        print(quantity)
        print(price)
        print(details)
    return render_template('admin.html')
