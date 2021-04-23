from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes 

        from .models import db
        db.init_app(app)
        migrate.init_app(app, db)       
        db.create_all()

    return app