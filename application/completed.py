from application.models import Completed
from flask import jsonify
from application import db


def view_completed_courses(input_learner_email):
    try:
        listOfCompletedCourses = []
        dbCompletedList = Completed.query.filter_by(learner_email = input_learner_email).all()
        for completed in dbCompletedList:
            listOfCompletedCourses.append(completed.json()["course_id"])

        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": {
                    "learner_email": input_learner_email,
                    "course_completed": listOfCompletedCourses
                }
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue viewing completed courses. " + str(e)
            }
        ), 500

