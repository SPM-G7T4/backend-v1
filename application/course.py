from application.models import Course, Class, Prerequisite
from flask import jsonify

def view_all_courses_test():
    try:
        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": {
                    "courses": [
                        {
                            "course_id": "REP1101",
                            "course_name": "Printer Concepts and Terminology",
                            "created_datetime": "2021-03-20 10:00:00",
                            "classes": [1,2,3],
                            "prerequisites": []
                        },
                        {
                            "course_id": "REP1201",
                            "course_name": "Printer Operations",
                            "created_datetime":"2021-03-20 10:00:00",
                            "classes": [1,2,3,4,5],
                            "prerequisites": []
                        },
                        {
                            "course_id": "REP1301",
                            "course_name": "Printer Startup Tutorial",
                            "created_datetime":"2021-03-20 10:00:00",
                            "classes": [1,2],
                            "prerequisites": ["REP1101","REP1201"]
                        }
                    ]
                }
            }
        )

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There was an issue retrieving all courses. " + str(e)
            }
        )

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
        "sections": 4,
        "videos": 4,
        "classes": [1,2,3,5,6],
        "duration": "3.5 hours",
        "description": "Briefly describes the relationship between printers, and their assigned lines, processes and statuses."

    }
}

def view_course_details(course_id):
    return {
        "code" : 500,
        "message" : "work in progress"
        }