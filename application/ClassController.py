from application.models import Class
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

