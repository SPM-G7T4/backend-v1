from application.models import Class, Section, Material
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
                
                section_id = sectionJson["section_id"]
                class_id = sectionJson["class_id"]
                course_id = sectionJson["course_id"]
                class_start_datetime = sectionJson["class_start_datetime"]

                listOfMaterials = []
                dbMaterialsList = Material.query.filter_by(
                    section_id = section_id,
                    class_id = class_id,
                    course_id = course_id,
                    class_start_datetime = class_start_datetime
                ).all()
                for dbMaterial in dbMaterialsList:
                    materialJson = dbMaterial.get_details()
                    title = materialJson["title"]
                    view_link = materialJson["view_link"]
                    download_link = materialJson["download_link"]
                    materialJson = {
                        "title" : title,
                        "view_link" : view_link,
                        "download_link" : download_link
                    }
                    listOfMaterials.append(materialJson)

                sectionJson["materials"] = listOfMaterials
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

