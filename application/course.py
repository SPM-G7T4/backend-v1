from application.models import Course, Class, Prerequisite
from flask import jsonify

# Add more functions here 
def view_all_courses():
    try :
        listOfCourses = []
        dbCourseList = Course.query.all()
        for course in dbCourseList:
            courseJSON = course.json()
            classList = []
            prerequisiteList = []

            dbClassList = Class.query.filter_by(course_id = courseJSON["course_id"]).all() # filter classes by courseid
            for c in dbClassList:
                classList.append(c.json()["class_id"])

            courseJSON["classes"] = classList # add classes list to courseJSON
            

            dbPrerequisite = Prerequisite.query.filter_by(postrequisite_id = courseJSON["course_id"]).all() # filter prerequisite by courseid
            for p in dbPrerequisite:
                prerequisiteList.append(p.json()["prerequisite_id"])
            
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
        )

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "The Course List cannot be shown." + str(e)
            }
        )
#Get Course Detail by course_id
def view_course_details(p_course_id):
    try :
        course = Course.query.filter_by(course_id = p_course_id).all()
        courseJSON = course[0].json()
        classList = []
        prerequisiteList = []

        dbClassList = Class.query.filter_by(course_id = p_course_id).all() # filter classes by courseid
        for c in dbClassList:
            classList.append(c.json()["class_id"])

        courseJSON["classes"] = classList # add classes list to courseJSON
        

        dbPrerequisite = Prerequisite.query.filter_by(postrequisite_id = p_course_id).all() # filter prerequisite by courseid
        for p in dbPrerequisite:
            prerequisiteList.append(p.json()["prerequisite_id"])
        
        courseJSON["prerequisites"] = prerequisiteList # add prerequisite list to courseJSON

        del courseJSON["created_datetime"]


        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": courseJSON
            }
        )

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "Course ID unable to locate." + str(e)
            }
        )
