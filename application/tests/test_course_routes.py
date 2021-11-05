import pytest
import requests
import json
# from application import create_app
from flask import Flask
import sys
sys.path.append('../../')
from wsgi import app
# from application.routes import configure_routes
# from application.routes import configure_routes

def setup():
    # app = create_app()
    # configure_routes(app)
    client = app.test_client()
    return client

# def test_get_all_courses():
#     response = requests.get("http://localhost:5000/courses")
#     assert response.status_code == 200

#     print(response.json())

# test_home_page()
# test_get_all_learners()
