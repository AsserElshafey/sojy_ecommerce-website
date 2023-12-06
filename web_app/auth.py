from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db

from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        print(password)
    return render_template("login.html")


@auth.route('/register', strict_slashes=False, methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('reg_email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        new_user = User(
            email=email, password=generate_password_hash(password1, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        print('account created!')

        print(email)
        print(password1)
        print(password2)
        return redirect(url_for('views.home'))
    return render_template("login.html")


@auth.route('/logout', strict_slashes=False)
def logout():
    return "logout"
