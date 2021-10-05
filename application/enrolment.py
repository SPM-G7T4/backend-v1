from application.models import Enrolment
from flask import jsonify

def create_enrolment_test():
    return jsonify(
        {
            "code": 201,
            "message": "Success"
        }
    )

def create_enrolment():
    return jsonify (
        {
            "code" : 500,
            "message" : "work in progress"
        }
    )

def view_enrolment_test():
    return jsonify(
        {
            "code": 200,
            "message": "Success",
            "data": {
                "learner_email": "sue.lim@allinOne.com",
                "enrolments": [
                    {
                        "course_id":"REP1101",
                        "class_id": 1
                    },
                    {
                        "course_id":"REP1201",
                        "class_id": 2
                    }
                ]
            }
        }
    )

def view_enrolment():
    return jsonify(
        {
            "code" : 500,
            "message" : "work in progress"
        }
    )