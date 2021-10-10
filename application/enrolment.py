from application.models import Enrolment
from flask import jsonify
from application import db


def create_enrolment_test():
    return jsonify(
        {
            "code": 201,
            "message": "Success"
        }
    )

def create_enrolment(request_body):
    try :
        if "hr_enroler_email" not in request_body:
            request_body["hr_enroler_email"] = None

        new_enrolment = Enrolment(
            learner_email = request_body["learner_email"],
            course_id = request_body["course_id"],
            class_id = request_body["class_id"],
            class_start_datetime = request_body["class_start_datetime"],
            hr_enroler_email = request_body["hr_enroler_email"],
            approved = "pending"
        )
        db.session.add(new_enrolment)
        db.session.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Success"
            }
        )

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue create an enrolment. " + str(e)
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