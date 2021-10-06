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

            dbClassList = Class.query.filter_by(course_id = courseJSON["course_id"]).all()
            for c in dbClassList:
                classList.append(c.json()["class_id"])

            courseJSON["classes"] = classList
            

            dbPrerequisite = Prerequisite.query.filter_by(postrequisite_id = courseJSON["course_id"]).all()
            for p in dbPrerequisite:
                prerequisiteList.append(p.json()["prerequisite_id"])
            
            courseJSON["prerequisites"] = prerequisiteList

            listOfCourses.append(courseJSON)

        # print(listOfCourses)
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
                "code": 500,
                "message": "There was an issue retrieving all courses. " + str(e)
            }
        )

def view_course_details_test(course_id):
    return {
    "code": 200, 
    "data": {
        "course_id": "REP1101",
        "course_name": "Printer Concepts and Terminology",
        "classes": [1,2,3,5,6],
        "description": "Briefly describes the relationship between printers, and their assigned lines, processes and statuses.",
        "prerequisites": []
    }

}

def view_course_details(course_id):
    return {
        "code" : 500,
        "message" : "work in progress"
        }
