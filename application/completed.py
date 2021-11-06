from application.models import Completed, Course
from flask import jsonify
from application import db

class CompletedController():
    def view_completed_courses(self, input_learner_email):
        try:
            listOfCompletedCourses = []
            courseDetailsList = []
            dbCompletedList = Completed.query.filter_by(learner_email = input_learner_email).all()
            for completed in dbCompletedList:
                completedJson = completed.get_details()
                del completedJson["completion_datetime"]
                del completedJson["learner_email"]
                courseDetailsList.extend(Course.query.filter_by(course_id = completedJson["course_id"]).all())

                if courseDetailsList:
                    courseDetailsDict = courseDetailsList.pop().get_details()
                    completedJson["course_name"] = courseDetailsDict["course_name"]
                    completedJson["description"] = courseDetailsDict["description"]
                
                listOfCompletedCourses.append(completedJson)

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

