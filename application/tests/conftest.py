import pytest

from application.DatabaseController import DatabaseController
from wsgi import app

@pytest.fixture(scope="session")
def setup_database():
    # app = create_app(True)    
    temp = app.config["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_DATABASE_URI"] = temp + "_test"
    client = app.test_client()
    databaseController = DatabaseController()
    databaseController.up_database(app)

    yield client

    databaseController.down_database(app)
