from flask import Blueprint, render_template, request

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
        print(email)
        print(password1)
        print(password2)
    return render_template("login.html")


@auth.route('/logout', strict_slashes=False)
def logout():
    return "logout"
