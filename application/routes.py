from flask import render_template
from flask import current_app as app
from flask import request
import json

# Routes to files

# learner
from .learner import view_all_learners
from .learner import check_eligibility
# hr
from .hr import view_all_hr
# trainer
from .trainer import view_all_trainers

# course
from .course import view_all_courses
from .course import view_course_details

# enrolment
from .enrolment import create_enrolment
from .enrolment import view_enrolment
from .enrolment import change_enrolment_status

# completed
from .completed import view_completed_courses

# quiz
from .quiz import view_quiz
from .quiz import create_quiz
from .quiz import update_quiz
from .quiz import view_quiz_details
from .quiz import attach_quiz


# Endpoints
# def configure_routes(app):
@app.route("/", methods=['GET'])
def hello_world():
    return "<h1>Greetings from SPM-G7T4</h1>"

# learner
@app.route("/learners", methods=['GET'])
def return_all_learners():
    return view_all_learners()

@app.route("/learners/eligibility", methods=['POST'])
def return_eligibility():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    extracted_learner_email =  jsonResponse["learner_email"]
    extracted_course_id =  jsonResponse["course_id"]
    extracted_class_id =  jsonResponse["class_id"]

    return check_eligibility(extracted_learner_email, extracted_course_id, extracted_class_id)

# hr
@app.route("/hr", methods=['GET'])
def return_all_hr():
    return view_all_hr()

# trainer
@app.route("/trainers", methods=['GET'])
def return_all_trainers():
    return view_all_trainers()

# course
@app.route("/courses", methods=['GET'])
def return_all_courses():
    return view_all_courses()

@app.route("/courses/<course_id>", methods=['GET'])
def return_course_details(course_id):
    return view_course_details(course_id)

# enrolment
@app.route("/enrolments/create", methods=['POST'])
def return_enrolment_creation_status():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    
    return create_enrolment(jsonResponse)

@app.route("/enrolments/view", methods=['POST'])
def return_learner_enrolment():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    extracted_learner_email =  jsonResponse["learner_email"]

    return view_enrolment(extracted_learner_email)

@app.route("/enrolments/approve", methods=['PUT'])
def return_enrolment_approval_status():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    
    return change_enrolment_status(jsonResponse)

@app.route("/enrolments/view", methods=['GET'])
def return_all_enrolment():
    return view_enrolment()

# completed
@app.route("/completed/view", methods=['POST'])
def return_completed_courses():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    extracted_learner_email =  jsonResponse["learner_email"]

    return view_completed_courses(extracted_learner_email)

# quiz
@app.route("/quiz/view", methods=['GET'])
def return_all_quiz():
    return view_quiz()
@app.route("/quiz/create", methods=['POST'])
def return_quiz_creation_status():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    
    return create_quiz(jsonResponse)
@app.route("/quiz/update", methods=['POST'])
def return_quiz_update_status():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    
    return update_quiz(jsonResponse)

@app.route("/quiz/view/<quiz_id>", methods=['GET'])
def return_all_quiz_details(quiz_id):
    return view_quiz_details(quiz_id)

@app.route("/quiz/attach", methods=['POST'])
def return_quiz_attach_status():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    
    return attach_quiz(jsonResponse)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
