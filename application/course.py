from application.models import Learner
from flask import jsonify

def view_all_courses():
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