from .. import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)
    details = db.Column(db.Text)
    featured = db.Column(db.Integer)
    image = db.Column(db.String(50))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    cart = db.relationship('Cart', back_populates='product')
