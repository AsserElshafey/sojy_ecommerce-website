from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models.user import User
from . import db
from flask_login import login_user, login_required, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Your password is incorrect.", category='error')
        else:
            flash("This user doesn't exist", category='error')
            return redirect(url_for('auth.login'))
    return render_template("login.html")


@auth.route('/register', strict_slashes=False, methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('reg_email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password must be atleast 8 characters', category='error')
        elif user:
            flash('This user already exists', category='error')
        else:
            # Create new user
            new_user = User(
                email=email, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("login.html")


@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    return render_template("login.html")
