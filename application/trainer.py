from application.models import Trainer
from flask import jsonify

class TrainerController():
    def view_all_trainers(self):
        try :
            trainerList = Trainer.query.all()
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "trainers": [trainer.get_details() for trainer in trainerList]
                    }
                }
            ), 200

        except Exception as e:
            
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue retrieving all trainers. " + str(e)
                }
            ), 500

    # Add more functions here 