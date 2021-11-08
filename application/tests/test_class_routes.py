"""Primary Author: Ong Jia Le"""

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
    print(response_body)

    assert len(response_body["data"]) != None
    assert response.status_code == 200

    assert response_body["data"]["classes"][0]["course_id"] == "REP1101"
    assert response_body["data"]["classes"][0]["trainer_email"] == "jiale@smu.edu.sg"

    assert response_body["data"]["classes"][1]["course_id"] == "REP1201"
    assert response_body["data"]["classes"][1]["trainer_email"] == "jiale@smu.edu.sg"

    assert len(response_body["data"]["classes"]) == 2

def test_class_sections(setup_database):
    url = '/classes/sections'

    req_body = {
        "course_id": "REP1101",
        "class_id" : 1,
        "class_start_datetime" : "2021-01-07 00:00:00"
    }

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')
    response_body = json.loads(response.get_data())
    print(response_body)

    assert len(response_body["data"]) != None
    assert response.status_code == 200

    data = response_body["data"]["sections"]

    assert data[0]["section_name"] == "Introductions: Terms"
    assert data[0]["course_id"] == "REP1101"

    assert len(data[0]["materials"]) > 0
    assert data[0]["materials"][0]["title"] == "01 Types of Printer - Slides"

    assert data[1]["section_name"] == "Systems and Operations"
    assert data[1]["course_id"] == "REP1101"

    assert len(data) == 2

def test_fail_class_sections(setup_database):
    url = '/classes/sections'

    req_body = {
        "class_id" : 1,
        "class_start_datetime" : "2021-01-07 00:00:00"
    }

    response = setup_database.post(url, data=json.dumps(req_body), content_type='application/json')
    response_body = json.loads(response.get_data())
    print(response_body)

    assert response.status_code == 500