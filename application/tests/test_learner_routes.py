import json
import sys
sys.path.append('../../')


def test_get_all_learners(setup_database):
    """ Test viewing list of all learners """
    url = "/learners"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    # Check if content return is application/json or text/html
    assert response.content_type == 'application/json'
    assert len(response_body["data"]["learners"]) > 0

    #Check for data returned
    assert response_body["data"]["learners"][0]["name"] == "Niankai"
    assert response_body["data"]["learners"][0]["department"] == "Engineering"
    assert response_body["data"]["learners"][0]["designation"] == "Junior systems engineer"
    assert response_body["data"]["learners"][0]["email"] == "niankai@smu.edu.sg"
    assert response_body["data"]["learners"][0]["password"] == "123"

    assert response_body["data"]["learners"][1]["name"] == "Sean"
    assert response_body["data"]["learners"][1]["department"] == "Engineering"
    assert response_body["data"]["learners"][1]["designation"] == "Junior electrical engineer"
    assert response_body["data"]["learners"][1]["email"] == "sean@smu.edu.sg"
    assert response_body["data"]["learners"][1]["password"] == "123"

def test_get_trainers(setup_database):
    """ Test viewing list of all trainers """
    url = "/trainers"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    # Check if content return is application/json or text/html
    assert response.content_type == 'application/json'
    assert len(response_body["data"]["trainers"]) > 0
    assert len(response_body["data"]["trainers"]) == 2

    #Check for data returned
    assert response_body["data"]["trainers"][0]["name"] == "Ong Jia Le"
    assert response_body["data"]["trainers"][1]["name"] == "Ken Tich"

    assert response_body["data"]["trainers"][0]["email"] == "jiale@smu.edu.sg"
    assert response_body["data"]["trainers"][1]["email"] == "ken@smu.edu.sg"

def test_get_hr(setup_database):
    """ Test viewing list of all trainers """
    url = "/hr"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    # Check if content return is application/json or text/html
    assert response.content_type == 'application/json'
    assert len(response_body["hr"]["hr"]) > 0
    assert len(response_body["hr"]["hr"]) == 2

    #Check for data returned
    assert response_body["data"]["hr"][0]["name"] == "avigale"
    assert response_body["data"]["hr"][1]["name"] == "joen"


def test_learners_completed_courses(setup_database):
    """ Test viewing list of learner's completed course """
    url = "/completed/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    assert len(response_body["data"]["course_completed"]) > 0
    assert response_body["data"]["course_completed"][0]["course_id"] == "REP1101"

def test_learners_enrolments(setup_database):
    """ Test viewing list course learner successfully enrolled in """
    url = "/enrolments/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg"
    }
    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    assert len(response_body["data"]["enrolments"]) > 0

    assert response_body["data"]["enrolments"][0]["class_end_datetime"] == "2021-05-30 23:59:59"
    assert response_body["data"]["enrolments"][0]["class_id"] == 1
    assert response_body["data"]["enrolments"][0]["class_size"] == 40

    assert response_body["data"]["enrolments"][0]["class_start_datetime"] == "2021-01-07 00:00:00"
    assert response_body["data"]["enrolments"][0]["course_id"] == "REP1101"
    assert response_body["data"]["enrolments"][0]["course_name"] == "Printer Concepts and Terminology"
    assert response_body["data"]["enrolments"][0]["description"] == "Briefly describes the relationship between printers, and their assigned lines, processes and statuses."
    assert response_body["data"]["enrolments"][0]["status"] == "enrolled"
    assert response_body["data"]["enrolments"][0]["trainer_email"] == "jiale@smu.edu.sg"

#def test_learner_eligibility(setup_database):
#    url = '/learners/eligibility'

#    req_body =  {
#        "learner_email" : "sean@smu.edu.sg",
#        "course_id" : "REP1101",
#        "class_id" : 1
#    }
#    response = setup_database.post(url, data=json.dumps(
#        req_body), content_type='application/json')

#    response_body = json.loads(response.get_data())

#    assert response.status_code == 500

#    assert response_body["data"][0]["eligibility"] == True

