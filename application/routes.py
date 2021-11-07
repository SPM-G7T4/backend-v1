from flask import render_template
from flask import current_app as app
from flask import request
import json

# Routes to files

# learner
from .learner import LearnerController
# hr
from .hr import HrController
# trainer
from .trainer import TrainerController

# course
from .course import CourseController

# enrolment
from .enrolment import EnrolmentController

# completed
from .completed import CompletedController

# quiz
from .quiz import QuizController


# Endpoints
# def configure_routes(app):
class MainController():
    @app.route("/", methods=['GET'])
    def hello_world():
        return "<h1>Greetings from SPM-G7T4</h1>"

    # learner
    @app.route("/learners", methods=['GET'])
    def return_all_learners():
        learnerController = LearnerController()
        return learnerController.view_all_learners()

    @app.route("/learners/eligibility", methods=['POST'])
    def return_eligibility():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        extracted_learner_email =  jsonResponse["learner_email"]
        extracted_course_id =  jsonResponse["course_id"]
        extracted_class_id =  jsonResponse["class_id"]

        learnerController = LearnerController()
        return learnerController.check_eligibility(extracted_learner_email, extracted_course_id, extracted_class_id)

    # hr
    @app.route("/hr", methods=['GET'])
    def return_all_hr():
        hrController = HrController()
        return hrController.view_all_hr()

    # trainer
    @app.route("/trainers", methods=['GET'])
    def return_all_trainers():
        trainerController = TrainerController()
        return trainerController.view_all_trainers()

    # course
    @app.route("/courses", methods=['GET'])
    def return_all_courses():
        courseController = CourseController()
        return courseController.view_all_courses()

    @app.route("/courses/<course_id>", methods=['GET'])
    def return_course_details(course_id):
        courseController = CourseController()
        return courseController.view_course_details(course_id)

    # enrolment
    @app.route("/enrolments/create", methods=['POST'])
    def return_enrolment_creation_status():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        
        enrolmentController = EnrolmentController()
        return enrolmentController.create_enrolment(jsonResponse)

    @app.route("/enrolments/view", methods=['POST'])
    def return_learner_enrolment():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        extracted_learner_email =  jsonResponse["learner_email"]

        enrolmentController = EnrolmentController()
        return enrolmentController.view_enrolment(extracted_learner_email)

    @app.route("/enrolments/approve", methods=['PUT'])
    def return_enrolment_approval_status():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        
        enrolmentController = EnrolmentController()
        return enrolmentController.change_enrolment_status(jsonResponse)

    @app.route("/enrolments/view", methods=['GET'])
    def return_all_enrolment():
        enrolmentController = EnrolmentController()
        return enrolmentController.view_enrolment()

    # completed
    @app.route("/completed/view", methods=['POST'])
    def return_completed_courses():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        extracted_learner_email =  jsonResponse["learner_email"]

        completedController = CompletedController()
        return completedController.view_completed_courses(extracted_learner_email)

    # quiz
    @app.route("/quiz/view", methods=['GET'])
    def return_all_quiz():
        quizController = QuizController()
        return quizController.view_quiz()

    @app.route("/quiz/create", methods=['POST'])
    def return_quiz_creation_status():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        
        quizController = QuizController()
        return quizController.create_quiz(jsonResponse)

    @app.route("/quiz/update", methods=['POST'])
    def return_quiz_update_status():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        
        quizController = QuizController()
        return quizController.update_quiz(jsonResponse)

    @app.route("/quiz/view/<quiz_id>", methods=['GET'])
    def return_all_quiz_details(quiz_id):
        quizController = QuizController()
        return quizController.view_quiz_details(quiz_id)

    @app.route("/quiz/attach", methods=['POST'])
    def return_quiz_attach_status():
        data = request.data
        jsonResponse = json.loads(data.decode('utf-8'))
        
        quizController = QuizController()
        return quizController.attach_quiz(jsonResponse)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    # @app.route("/database/up", methods=['GET'])
    # def return_up_database():
    #     databaseController = DatabaseController()
    #     return databaseController.up_database()

    # @app.route("/database/down", methods=['GET'])
    # def return_down_database():
    #     databaseController = DatabaseController()
    #     return databaseController.down_database()



