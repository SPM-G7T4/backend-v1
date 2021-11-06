"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(testing=False):
    """Construct the core application."""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    if testing:
        temp = app.config["SQLALCHEMY_DATABASE_URI"]
        app.config["SQLALCHEMY_DATABASE_URI"] = temp + "_test"

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        return app