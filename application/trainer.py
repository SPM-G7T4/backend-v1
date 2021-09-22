from application.models import Trainer
from flask import jsonify

def view_all_trainers():
    try :
        trainerList = Trainer.query.all()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "trainers": [trainer.json() for trainer in trainerList]
                }
            }
        )

    except Exception as e:
        
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue retrieving all trainers. " + str(e)
            }
        )

# Add more functions here 