from .. import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256))
    cart = db.relationship('Cart', backref='user',
                           lazy=True, uselist=False)
