from application.models import Learner
from flask import jsonify

def view_all_learners():
    try :
        learnerList = Learner.query.all()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learners": [learner.json() for learner in learnerList]
                }
            }
        )

    except Exception as e:
        
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue retrieving all learners. " + str(e)
            }
        )

# Add more functions here 