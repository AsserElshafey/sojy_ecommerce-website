from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hiddenleaf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sojy'
    db.init_app(app)

    from .views import views
    from .auth import auth

    from . import models

    with app.app_context():
        db.create_all()

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
