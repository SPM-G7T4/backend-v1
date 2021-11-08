from application.models import HR
from flask import jsonify

class HrController():
    def view_all_hr(self):
        try :
            hrList = HR.query.all()
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "hr": [hr.get_details() for hr in hrList]
                    }
                }
            ), 200

        except Exception as e:
            
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue retrieving all hr. " + str(e)
                }
            ), 500

    # Add more functions here 