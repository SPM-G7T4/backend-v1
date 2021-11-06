import pytest
import json
import sys
sys.path.append('../../')
from wsgi import app

def test_get_all_quizzes():
    # This is an example test case, feel free to copy/delete/modify
    client = app.test_client()

    # Define the relative url for the endpoint you will test here
    url = '/quiz/view'

    response = client.get(url)

    response_body = json.loads(response.get_data())

    # assert values here
    assert response.status_code == 200
    assert response_body["data"]["quiz"][0]["quiz_name"] == "Term Definitions"
    assert response_body["data"]["quiz"][1]["quiz_name"] == "Systems"
    assert response_body["data"]["quiz"][1]["quiz_id"] == 2
    assert len(response_body["data"]["quiz"]) > 0
    return
