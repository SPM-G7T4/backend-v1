# Primary Author: Choon Wing Kit Sean

import json
import sys
sys.path.append('../../')


def test_view_all_enrolment(setup_database):
    """ Test viewing list of all enrolments """
    url = "/enrolments/view"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][0]["course_id"] == "REP1101"
    assert response_body["data"]["enrolments"][0]["learner_email"] == "niankai@smu.edu.sg"
    assert response_body["data"]["enrolments"][0]["status"] == "enrolled"

    assert response_body["data"]["enrolments"][1]["course_id"] == "REP1101"
    assert response_body["data"]["enrolments"][1]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][1]["status"] == "enrolled"


def test_view_learner_enrolment(setup_database):
    """ Test viewing list of learner enrolments """

    url = "/enrolments/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][0]["course_id"] == "REP1101"
    assert response_body["data"]["enrolments"][0]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][0]["status"] == "enrolled"


def test_learner_self_enrol(setup_database):
    """ Test learner self enrolment into class """

    # Creates self-enrolment responses
    url = "/enrolments/create"

    req_body = {
        "learner_email": "sean@smu.edu.sg",
        "course_id": "REP1301",
        "class_id": 1,
        "class_start_datetime": "2021-01-07 00:00:00",
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 201

    req_body = {
        "learner_email": "sean@smu.edu.sg",
        "course_id": "REP1201",
        "class_id": 1,
        "class_start_datetime": "2021-01-07 00:00:00",
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 201

    # Check that enrolment has been created for user with pending status (pending HR approval)
    url = "/enrolments/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][1]["course_id"] == "REP1201"
    assert response_body["data"]["enrolments"][1]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][1]["status"] == "pending"

    assert response_body["data"]["enrolments"][2]["course_id"] == "REP1301"
    assert response_body["data"]["enrolments"][2]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][2]["status"] == "pending"

def test_hr_approve_learner(setup_database):
    """ Test HR approve learner enrolment into class """

    # Approve enrolment request
    url = "/enrolments/approve"

    req_body = {
        "learner_email": "sean@smu.edu.sg",
        "course_id": "REP1301",
        "class_id": 1,
        "class_start_datetime": "2021-01-07 00:00:00",
        "approver_email": "joen@smu.edu.sg",
        "status": "enrolled"
    }

    response = setup_database.put(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    # Check that enrolment has been created for user with enrolled status
    url = "/enrolments/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][2]["course_id"] == "REP1301"
    assert response_body["data"]["enrolments"][2]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][2]["status"] == "enrolled"

def test_hr_reject_learner(setup_database):
    """ Test HR reject learner enrolment into class """

    # Approve enrolment request
    url = "/enrolments/approve"

    req_body = {
        "learner_email": "sean@smu.edu.sg",
        "course_id": "REP1201",
        "class_id": 1,
        "class_start_datetime": "2021-01-07 00:00:00",
        "approver_email": "joen@smu.edu.sg",
        "status": "rejected"
    }

    response = setup_database.put(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    # Check that enrolment has been created for user with enrolled status
    url = "/enrolments/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][1]["course_id"] == "REP1201"
    assert response_body["data"]["enrolments"][1]["learner_email"] == "sean@smu.edu.sg"
    assert response_body["data"]["enrolments"][1]["status"] == "rejected"
