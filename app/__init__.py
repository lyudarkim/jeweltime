from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.account import Account
    from app.models.project import Project
    from app.models.signin import Signin

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes.account import accounts_bp
    from .routes.project import projects_bp
    from .routes.account import signin_bp
    from .routes.account import test_bp
    from .routes.account import metals_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(signin_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(metals_bp)

    return app
