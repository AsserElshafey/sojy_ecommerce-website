from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hiddenleaf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sojy'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .products import product

    from . import models
    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(product, url_prefix="/")
    return app
