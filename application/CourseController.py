from application.models import Course, Class, Prerequisite, Trainer
from flask import jsonify

class CourseController():
    # Add more functions here 
    def view_all_courses(self):
        try :
            listOfCourses = []
            dbCourseList = Course.query.all()
            for course in dbCourseList:
                courseJSON = course.get_details()
                classList = []
                prerequisiteList = []

                dbClassList = Class.query.filter_by(course_id = courseJSON["course_id"]).all() # filter classes by courseid
                for c in dbClassList:
                    classList.append(c.get_details()["class_id"])

                courseJSON["classes"] = classList # add classes list to courseJSON
                

                dbPrerequisite = Prerequisite.query.filter_by(postrequisite_id = courseJSON["course_id"]).all() # filter prerequisite by courseid
                for p in dbPrerequisite:
                    prerequisiteList.append(p.get_details()["prerequisite_id"])
                
                courseJSON["prerequisites"] = prerequisiteList # add prerequisite list to courseJSON

                listOfCourses.append(courseJSON)

            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": {
                        "courses": listOfCourses
                    }
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue retrieving all courses. " + str(e)
                }
            ), 500

    def view_course_details(self, p_course_id):
        try :
            course = Course.query.filter_by(course_id = p_course_id).all()
            courseJSON = course[0].get_details()
            classList = []
            prerequisiteList = []

            dbClassList = Class.query.filter_by(course_id = p_course_id).all() # filter classes by courseid
            for c in dbClassList:
                
                input_trainer_email = c.get_details()["trainer_email"]
                trainer_name = Trainer.query.with_entities(Trainer.name).filter_by(email = input_trainer_email).first()[0]
                revisedJSON = c.get_details()
                revisedJSON["trainer_name"] = trainer_name
                classList.append(revisedJSON)

            courseJSON["classes"] = classList # add classes list to courseJSON

            dbPrerequisite = Prerequisite.query.filter_by(postrequisite_id = p_course_id).all() # filter prerequisite by courseid
            for p in dbPrerequisite:
                prerequisiteList.append(p.get_details()["prerequisite_id"])
            
            courseJSON["prerequisites"] = prerequisiteList # add prerequisite list to courseJSON

            del courseJSON["created_datetime"]


            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": courseJSON
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue retrieving all courses. " + str(e)
                }
            ), 500
