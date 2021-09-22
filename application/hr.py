from application.models import HR
from flask import jsonify

def view_all_hr():
    try :
        hrList = HR.query.all()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "hr": [hr.json() for hr in hrList]
                }
            }
        )

    except Exception as e:
        
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue retrieving all hr. " + str(e)
            }
        )

# Add more functions here 