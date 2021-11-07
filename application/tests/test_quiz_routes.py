import json
import sys
sys.path.append('../../')

def test_get_all_quizzes(setup_database):
    url = '/quiz/view'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert len(response_body["data"]["quiz"]) > 0
    assert response.status_code == 200
    assert response_body["data"]["quiz"][0]["quiz_name"] == "Term Definitions"
    assert response_body["data"]["quiz"][1]["quiz_name"] == "Systems"
    assert response_body["data"]["quiz"][1]["quiz_id"] == 2
    
def test_add_quiz(setup_database):
    # View the quizzes before I create a new quiz
    url = '/quiz/view'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())
        
    assert response.status_code == 200

    url = '/quiz/create'

    req_body = {
        "quiz_name": "New Test Quiz"
    }

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    # View the quizzes AFTER I create a new quiz
    url = '/quiz/view'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert response_body["data"]["quiz"][-1]["quiz_name"] == "New Test Quiz"