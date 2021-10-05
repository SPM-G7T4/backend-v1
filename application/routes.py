from flask import render_template
from flask import current_app as app

# Routes to files
from .course import view_all_courses_test
from .course import view_course_details_test

from .course import view_course_details_test

from .learner import view_all_learners
from .hr import view_all_hr
from .trainer import view_all_trainers


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
    return view_all_courses_test()

@app.route("/courses/<course_id>", methods=['GET'])
def return_course_details(course_id):
    return view_course_details_test(course_id)

# enrolment
@app.route("/enrolment/create", methods=['POST'])
def return_enrolment_creation_status():
    return create_enrolment()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
