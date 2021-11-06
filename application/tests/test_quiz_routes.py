import pytest
import json
import sys
sys.path.append('../../')
from application import create_app
from application.DatabaseController import DatabaseController

@pytest.fixture(scope="session")
def setup_database():
    app = create_app(True)    
    client = app.test_client()
    databaseController = DatabaseController()
    databaseController.up_database(app)

    yield client

    databaseController.down_database(app)

# def test_cleanup():
#     app = create_app(True)
#     d = DatabaseController()
#     d.down_database(app)

def test_get_all_quizzes(setup_database):

    url = '/quiz/view'

    response = setup_database.get(url)
    print("test1", response)

    response_body = json.loads(response.get_data())
    print("test1", response_body)

    # assert values here
    assert response.status_code == 200
    assert response_body["data"]["quiz"][0]["quiz_name"] == "Term Definitions"
    assert response_body["data"]["quiz"][1]["quiz_name"] == "Systems"
    assert response_body["data"]["quiz"][1]["quiz_id"] == 2
    assert len(response_body["data"]["quiz"]) > 0
    return

def test_add_quiz(setup_database):
    # View the quizzes before I create a new quiz
    url = '/quiz/view'

    response = setup_database.get(url)

    response_body = json.loads(response.get_data())
    print("test2", response_body)
    # print(response_body["data"]["quiz"])
    
    assert response.status_code == 200

    # Create the quiz on the test db
    url = '/quiz/create'

    req_body = {
        "quiz_name": "New Test Quiz"
    }

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')

    response_body = json.loads(response.get_data())
    print(response_body)
    # assert response.status_code == 201

    # View the quizzes AFTER I create a new quiz
    url = '/quiz/view'

    response = setup_database.get(url)

    response_body = json.loads(response.get_data())
    print(response_body["data"]["quiz"])

    # assert values here
    assert response.status_code == 200
    assert response_body["data"]["quiz"][-1]["quiz_name"] == "New Test Quiz"
    return