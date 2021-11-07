import pytest
import json
import sys
sys.path.append('../../')
from wsgi import app

# def test_home_page():
#     # This is an example test case, feel free to copy/delete/modify
#     client = app.test_client()

#     # Define the relative url for the endpoint you will test here
#     url = '/'

#     response = client.get(url)

#     # assert values here
#     assert response.get_data() == b'<h1>Greetings from SPM-G7T4</h1>'
#     assert response.status_code == 200
#     return

# def test_get_all_learners():
#     # This is an example test case, feel free to copy/delete/modify
#     client = app.test_client()

#     # Define the relative url for the endpoint you will test here
#     url = '/learners'

#     response = client.get(url)

#     response_body = json.loads(response.get_data())

#     # assert values here
#     assert response.status_code == 200
#     assert response_body["data"]["learners"][0]["name"] == "Niankai"
#     assert response_body["data"]["learners"][1]["name"] == "Sean"
#     assert len(response_body["data"]["learners"]) == 2
#     return


