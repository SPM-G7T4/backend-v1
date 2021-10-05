from application.models import Course
from flask import jsonify

def view_all_courses_test():
    return jsonify(
        {
            "code" : 200,
            "message": "Success",
            "data" :{
                "courses" : [
                    {
                        "courseID": "REP2101",
                        "courseName": "Printer Coach Repairs",
                        "courseStartDate": "2021-03-20 10:00:00",
                        "courseEndDate": "2021-09-01 11:59:00",
                        "classes": ["C1","C2"],
                        "prerequisites": ["REP1101","REP1201"]
                    },
                    {
                        "courseID": "REP1101",
                        "courseName": "General Repairs",
                        "courseStartDate": "2021-03-20 10:00:00",
                        "courseEndDate": "2021-09-01 11:59:00",
                        "classes": ["C1","C2","C3","C4","C5"],
                        "prerequisites": []
                    }
                ]
            }
        }
    )

# Add more functions here 
def view_all_courses():
    try :
        courseList = Course.query.all()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learners": [course.json() for course in courseList]
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