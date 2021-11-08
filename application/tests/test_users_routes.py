""""Primary author: Ranullo Avigale Balisacan"""

import json
import sys
sys.path.append('../../')


def test_get_all_learners(setup_database):
    """ Test viewing list of all learners """
    url = "/learners"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    #Check is it learners
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
    assert len(response_body["data"]["trainers"]) > 0

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
    assert len(response_body["data"]["hr"]) > 0

    #Check for data returned
    assert response_body["data"]["hr"][0]["name"] == "avigale"
    assert response_body["data"]["hr"][1]["name"] == "joen"

def test_learner_check_complete_course(setup_database):
    """ Test whether learner has taken a course """
    url = '/learners/eligibility'

    req_body =  {
        "learner_email" : "sean@smu.edu.sg",
        "course_id" : "REP1101",
        "class_id" : 1
    }
    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')

    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    assert response_body["data"]["eligibility"] == False
    assert response_body["data"]["reason"] == "Completed Course"

def test_learner_check_prereq(setup_database):
    """ Test whether learner has taken all the prequisite for a course """

    url = '/learners/eligibility'

    req_body =  {
        "learner_email" : "niankai@smu.edu.sg",
        "course_id" : "REP1301",
        "class_id" : 1
    }
    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')

    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    assert response_body["data"]["eligibility"] == False
    assert response_body["data"]["reason"] == "Prerequisite not met"



