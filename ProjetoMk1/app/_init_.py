from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = None

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    from .routes import auth, projects, comments, favorites, admin, chat
    app.register_blueprint(auth.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(comments.bp)
    app.register_blueprint(favorites.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(chat.bp)

    with app.app_context():
        db.create_all()

    return app