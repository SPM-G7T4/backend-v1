import json
import sys
sys.path.append('../../')

def test_get_all_quizzes(setup_database):
    """ Test viewing of all quizzes """
    url = '/quiz/view'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert len(response_body["data"]["quiz"]) > 0
    assert response.status_code == 200

    assert response_body["data"]["quiz"][0]["quiz_name"] == "Term Definitions"
    assert response_body["data"]["quiz"][0]["quiz_id"] == 1

    assert response_body["data"]["quiz"][1]["quiz_name"] == "Systems"
    assert response_body["data"]["quiz"][1]["quiz_id"] == 2
    
def test_add_quiz(setup_database):
    """ Test adding of quiz """

    # View the quizzes before I create a new quiz
    url = '/quiz/view'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())
    
    num_of_quizzes = len(response_body["data"]["quiz"])
    assert response.status_code == 200

    # Create quizzes
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

    assert len(response_body["data"]["quiz"]) == num_of_quizzes + 1
    assert response.status_code == 200
    assert response_body["data"]["quiz"][-1]["quiz_name"] == "New Test Quiz"
    assert response_body["data"]["quiz"][-1]["quiz_id"] == num_of_quizzes + 1


def test_attach_quiz(setup_database):
    """ Test attaching of quiz to a section """

    # View section before attaching a quiz
    # Might have to create "View Section Endpoint"


def test_view_quiz_details(setup_database):
    """ Test viewing of quiz details """

    # View the quiz details of specific quiz
    url = '/quiz/view/1'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    print(response_body)

    assert len(response_body["data"]["questions"]) > 0
    assert response.status_code == 200
    
    assert response_body["data"]["quiz_name"] == "Term Definitions"

    assert response_body["data"]["questions"][0]["question_id"] == 1
    assert response_body["data"]["questions"][0]["question_text"] == "Define 'System'"
    assert response_body["data"]["questions"][0]["answer_id"] == 1

    assert response_body["data"]["questions"][0]["options"][0]["option_id"] == 1
    assert response_body["data"]["questions"][0]["options"][0]["option_value"] == "A set of things working together as parts of a mechanism or an interconnecting network"
    
    assert response_body["data"]["questions"][0]["options"][1]["option_id"] == 2
    assert response_body["data"]["questions"][0]["options"][1]["option_value"] == "Multiple components joined together"

    assert response_body["data"]["questions"][1]["question_id"] == 2
    assert response_body["data"]["questions"][1]["question_text"] == "Define 'Component'"
    assert response_body["data"]["questions"][1]["answer_id"] == 3

    assert response_body["data"]["questions"][1]["options"][0]["option_id"] == 1
    assert response_body["data"]["questions"][1]["options"][0]["option_value"] == "Objects that are used by humans or other objects"
    
    assert response_body["data"]["questions"][1]["options"][1]["option_id"] == 2
    assert response_body["data"]["questions"][1]["options"][1]["option_value"] == "An inanimate object"


def test_update_quiz(setup_database):
    """ Test adding of quiz """

    # View the quiz details before I update the quiz details

    # View the quiz details before updating the quiz
    url = '/quiz/view/1'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert len(response_body["data"]["questions"]) > 0
    assert response.status_code == 200
    
    assert response_body["data"]["quiz_name"] == "Term Definitions"

    assert response_body["data"]["questions"][0]["question_text"] == "Define 'System'"
    assert response_body["data"]["questions"][0]["answer_id"] == 1

    assert response_body["data"]["questions"][0]["options"][0]["option_id"] == 1
    assert response_body["data"]["questions"][0]["options"][0]["option_value"] == "A set of things working together as parts of a mechanism or an interconnecting network"
    
    assert response_body["data"]["questions"][0]["options"][1]["option_id"] == 2
    assert response_body["data"]["questions"][0]["options"][1]["option_value"] == "Multiple components joined together"

    # Update quizzes
    url = '/quiz/update'

    new_request_body = response_body["data"]
    new_request_body["questions"][0]["answer_id"] = 2
    new_request_body["questions"][0]["options"][0]["option_id"] = 1
    new_request_body["questions"][0]["options"][0]["option_value"] = "Multiple components joined together"
    
    new_request_body["questions"][0]["options"][1]["option_id"] = 2
    new_request_body["questions"][0]["options"][1]["option_value"] = "A set of things working together as parts of a mechanism or an interconnecting network"

    req_body = new_request_body

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')
    assert response.status_code == 200

    # View the quiz details after updating the quiz - switch option 1 and 2
    url = '/quiz/view/1'

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert len(response_body["data"]["questions"]) > 0
    assert response.status_code == 200
    
    assert response_body["data"]["quiz_name"] == "Term Definitions"

    assert response_body["data"]["questions"][0]["question_text"] == "Define 'System'"
    assert response_body["data"]["questions"][0]["answer_id"] == 2

    assert response_body["data"]["questions"][0]["options"][0]["option_id"] == 1
    assert response_body["data"]["questions"][0]["options"][0]["option_value"] == "Multiple components joined together"
    
    assert response_body["data"]["questions"][0]["options"][1]["option_id"] == 2
    assert response_body["data"]["questions"][0]["options"][1]["option_value"] == "A set of things working together as parts of a mechanism or an interconnecting network"