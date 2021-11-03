# import pytest
import requests

def test_home_page():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.text == "<h1>Greetings from SPM-G7T4</h1>"

def test_get_all_learners():
    response = requests.get("http://localhost:5000/learners")
    assert response.status_code == 200
    response_body = response.json()["data"]
    assert response_body["learners"][0]["name"] == "niankai"
    assert response_body["learners"][1]["name"] == "sean"

    print(response.json())

def test_get_all_courses():
    response = requests.get("http://localhost:5000/courses")
    assert response.status_code == 200

    print(response.json())

test_get_all_learners()