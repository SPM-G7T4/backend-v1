import json
import sys
sys.path.append('../../')

def test_get_trainer_classes(setup_database):
    url = '/classes/trainer'

    req_body = {
        "trainer_email": "jiale@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert len(response_body["data"]) != None
    assert response.status_code == 200
    # assert response_body["data"]["quiz"][0]["quiz_name"] == "Term Definitions"
    # assert response_body["data"]["quiz"][1]["quiz_name"] == "Systems"
    # assert response_body["data"]["quiz"][1]["quiz_id"] == 2
