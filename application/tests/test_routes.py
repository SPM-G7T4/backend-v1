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

def test_home_page():
    client = setup()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'<h1>Greetings from SPM-G7T4</h1>'
    assert response.status_code == 200
    return

def test_get_all_learners():
    client = setup()
    response = client.get("/learners")

    assert response.status_code == 200
    response_body = json.loads(response.get_data())
    print(response_body)
    assert response_body["data"]["learners"][0]["name"] == "niankai"
    assert response_body["data"]["learners"][1]["name"] == "sean"
    return

# def test_get_all_courses():
#     response = requests.get("http://localhost:5000/courses")
#     assert response.status_code == 200

#     print(response.json())

# test_home_page()
test_get_all_learners()
