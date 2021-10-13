from flask import render_template
from flask import current_app as app
from flask import request
import json

# Routes to files

# learner
from .learner import view_all_learners
# hr
from .hr import view_all_hr
# trainer
from .trainer import view_all_trainers

# course
from .course import view_all_courses
from .course import view_course_details

# enrolment
from .enrolment import create_enrolment
from .enrolment import view_enrolment_test

# completed
from .completed import view_completed_courses



# Endpoints

@app.route("/", methods=['GET'])
def hello_world():
    return "<h1>Greetings from SPM-G7T4</h1>"

# learner
@app.route("/learners", methods=['GET'])
def return_all_learners():
    return view_all_learners()

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
def return_all_enrolment():
    return view_enrolment_test()

# completed
@app.route("/completed/view", methods=['POST'])
def return_completed_courses():
    data = request.data
    jsonResponse = json.loads(data.decode('utf-8'))
    extracted_learner_email =  jsonResponse["learner_email"]

    return view_completed_courses(extracted_learner_email)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
