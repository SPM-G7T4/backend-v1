from application.models import Enrolment, Course, Class
from flask import jsonify
from application import db

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
            status = "pending"
        )
        db.session.add(new_enrolment)
        db.session.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Success"
            }
        ), 201

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue create an enrolment. " + str(e)
            }
        ), 500

def view_enrolment(input_learner_email=None):
    try:
        listOfEnrolments = []

        if input_learner_email:
            dbEnrolmentList = Enrolment.query.filter_by(learner_email = input_learner_email).all()
        else:
            dbEnrolmentList = Enrolment.query.all()

        for e in dbEnrolmentList:
            enrolmentJSON = e.json()
            dbCourseDetails = Course.query.with_entities(Course.course_name, Course.description).filter_by(course_id = enrolmentJSON["course_id"]).first()
            dbClassDetails = Class.query.with_entities(Class.trainer_email, Class.start_datetime, Class.end_datetime, Class.class_size).filter_by(course_id = enrolmentJSON["course_id"], class_id = enrolmentJSON["class_id"]).first()
            eachEnrolment = {
                "course_id": enrolmentJSON["course_id"],
                "class_id": enrolmentJSON["class_id"],
                "learner_email": enrolmentJSON["learner_email"],
                "course_name": dbCourseDetails[0],
                "description": dbCourseDetails[1],
                "trainer_email": dbClassDetails[0],
                "class_start_datetime": dbClassDetails[1].strftime("%Y-%m-%d %H:%M:%S"),
                "class_end_datetime": dbClassDetails[2].strftime("%Y-%m-%d %H:%M:%S"),
                "class_size": dbClassDetails[3],
                "status": enrolmentJSON["status"]
            }
            listOfEnrolments.append(eachEnrolment)
            
        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": {
                    "enrolments": listOfEnrolments
                }
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue viewing the enrolments. " + str(e)
            }
        ), 500


def change_enrolment_status(request_body):
    try :
        enrolment = Enrolment.query.filter_by(
            learner_email = request_body["learner_email"],
            course_id = request_body["course_id"],
            class_id = request_body["class_id"],
            class_start_datetime = request_body["class_start_datetime"] 
        ).first()
        enrolment.approver_email = request_body["approver_email"]
        enrolment.status = request_body["status"]
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": enrolment.json()
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue changing enrolment status. " + str(e)
            }
        ), 500