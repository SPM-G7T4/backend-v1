from application.models import Class, Section
from flask import jsonify
from application import db

class ClassController():
    def view_trainer_classes(self, request_body):
        try:
            if "trainer_email" not in request_body:
                return jsonify(
                    {
                        "code": 500,
                        "message": "Missing Trainer Email or invalid request body."
                    }
                ), 500

            trainer_email = request_body["trainer_email"]

            listOfTrainerClasses = []
            dbTrainerClassList = Class.query.filter_by(trainer_email = trainer_email).all()
            for class_model in dbTrainerClassList:
                classJson = class_model.get_details()
                
                listOfTrainerClasses.append(classJson)

            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": {
                        "classes": listOfTrainerClasses,
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

    def view_class_sections(self, request_body):
        try:
            required_fields = ["class_start_datetime", "course_id", "class_id"]
            for field in required_fields:
                if field not in request_body:
                    return jsonify(
                        {
                            "code": 500,
                            "message": f"Missing {field} or invalid request body."
                        }
                    ), 500

            class_start_datetime = request_body["class_start_datetime"]
            course_id = request_body["course_id"]
            class_id = request_body["class_id"]

            listOfSections = []
            dbClassSectionList = Section.query.filter_by(
                class_start_datetime = class_start_datetime,
                course_id = course_id,
                class_id = class_id
            ).all()
            for section in dbClassSectionList:
                sectionJson = section.get_details()
                
                listOfSections.append(sectionJson)

            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": {
                        "sections": listOfSections,
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

