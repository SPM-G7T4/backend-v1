"""Primary Author: Chua Jo En"""

import json
import sys
sys.path.append('../../')

def test_get_list_of_courses(setup_database):
    url ="/courses"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200

    assert response_body["data"]["courses"][0]["course_id"] == "REP1101"
    assert response_body["data"]["courses"][1]["course_id"] == "REP1201"
    assert response_body["data"]["courses"][2]["course_id"] == "REP1301"
    assert response_body["data"]["courses"][3]["course_id"] == "REP2101"
    assert len(response_body["data"]["courses"]) == 4

def test_get_courses_details(setup_database):
    url="/courses/REP1101"

    response = setup_database.get(url)
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert response_body["data"]["course_id"] == "REP1101"
    assert response_body["data"]["course_name"] == "Printer Concepts and Terminology"
    assert response_body["data"]["description"] == "Briefly describes the relationship between printers, and their assigned lines, processes and statuses."
    assert len(response_body["data"]["prerequisites"]) == 0

    assert len(response_body["data"]["classes"]) == 2
    assert response_body["data"]["classes"][0]["class_id"] == 1
    assert response_body["data"]["classes"][1]["class_id"] == 2
    assert response_body["data"]["classes"][0]["class_size"] == 40
    assert response_body["data"]["classes"][1]["class_size"] == 40
    assert response_body["data"]["classes"][0]["end_datetime"] == "2021-05-30 23:59:59"
    assert response_body["data"]["classes"][1]["end_datetime"] == "2021-05-30 23:59:59"
    assert response_body["data"]["classes"][0]["enrol_end_datetime"] == "2020-12-30 23:59:59"
    assert response_body["data"]["classes"][1]["enrol_end_datetime"] == "2020-12-30 23:59:59"
    assert response_body["data"]["classes"][0]["enrol_start_datetime"] == "2020-12-01 00:00:00"
    assert response_body["data"]["classes"][1]["enrol_start_datetime"] == "2020-12-01 00:00:00"
    assert response_body["data"]["classes"][0]["start_datetime"] == "2021-01-07 00:00:00"
    assert response_body["data"]["classes"][1]["start_datetime"] == "2021-01-07 00:00:00"
    assert response_body["data"]["classes"][0]["trainer_email"] == "jiale@smu.edu.sg"
    assert response_body["data"]["classes"][1]["trainer_email"] == "ken@smu.edu.sg"
    assert response_body["data"]["classes"][0]["trainer_name"] == "Ong Jia Le"
    assert response_body["data"]["classes"][1]["trainer_name"] == "Ken Tich"

def test_get_completed_courses(setup_database):
    url ="/completed/view"

    req_body = {
        "learner_email": "sean@smu.edu.sg",
    }

    response = setup_database.post(url, data=json.dumps(
        req_body), content_type='application/json')
    response_body = json.loads(response.get_data())

    assert response.status_code == 200
    assert response_body["data"]["course_completed"][0]["course_id"] == "REP1101"

def test_page_not_found_equal_404(setup_database):
    url = '/asd'
    response = setup_database.get(url)
    assert response.status_code == 404

def test_get_all_hr_equal_200(setup_database):
    url = '/hr'
    response = setup_database.get(url)
    assert response.status_code == 200

def test_get_all_trainers_equal_200(setup_database):
    url = '/trainers'
    response = setup_database.get(url)
    assert response.status_code == 200

def test_get_all_courses_equal_200(setup_database):
    url = '/courses'
    response = setup_database.get(url)
    assert response.status_code == 200

def test_get_course_details_equal_200(setup_database):
    url = '/courses/REP1101'
    response = setup_database.get(url)
    assert response.status_code == 200

def test_get_course_details_equal_500(setup_database):
    url = '/courses/REP1000'
    response = setup_database.get(url)
    assert response.status_code == 500
