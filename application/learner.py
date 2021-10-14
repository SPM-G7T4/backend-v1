from datetime import datetime
from application.models import Learner, Course, Prerequisite, Enrolment, Completed, Class
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

def check_eligibility(input_learner_email, input_course_id, input_class_id):
    
    try :
        [eligibility, reason] = get_eligibility_and_reason(input_learner_email, input_course_id, input_class_id)

        return jsonify(
            {
                "code": 200,
                "message": "Success",
                "data": {
                    "eligibility" : eligibility,
                    "reason": reason
                }
            }
        )

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "There was an issue viewing the eligibility. " + str(e)
            }
        )

def get_eligibility_and_reason(input_learner_email, input_course_id, input_class_id):
    eligibility = True
    reason = None

    # Check Completed Courses
    dbCompletedList = Completed.query.with_entities(Completed.course_id).filter_by(learner_email = input_learner_email).all()
    dbCompletedList = [course for course, in dbCompletedList]

    if input_course_id in dbCompletedList:
        eligibility = False
        reason = "Completed Course"
        return [eligibility, reason]

    # Test Case
    # {
    #     "learner_email" : "sean@smu.edu.sg",
    #     "course_id" : "REP1101",
    #     "class_id" : 1
    # }
    
    # Check Prerequisite
    dbPrerequisiteList = Prerequisite.query.with_entities(Prerequisite.prerequisite_id).filter_by(postrequisite_id = input_course_id).all()
    for c in dbPrerequisiteList:
        if c not in dbCompletedList:
            eligibility = False
            reason = "Prerequisite not met"
            return [eligibility, reason]
    
    # Test Case
    # {
    #     "learner_email" : "niankai@smu.edu.sg",
    #     "course_id" : "REP1301",
    #     "class_id" : 1
    # }

    # Check whether within Enrolment Period
    dbClassDetails = Class.query.with_entities(Class.enrol_start_datetime, Class.enrol_end_datetime).filter_by(course_id = input_course_id, class_id = input_class_id).first() # Assume 1 semester
    enrol_start_datetime = dbClassDetails[0]
    enrol_end_datetime = dbClassDetails[1]
    if datetime.now() < enrol_start_datetime:
        eligibility = False
        reason = "Enrolment starts on " + enrol_start_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return [eligibility, reason]
    
    # Test Case - Needs to create 1 more additional class with enrol_start_datetime later than today 
    # {
    #     "learner_email" : "niankai@smu.edu.sg",
    #     "course_id" : "REP1301",
    #     "class_id" : 1
    # }

    # Check Pending and Approved
    dbEnrolmentApproved = Enrolment.query.with_entities(Enrolment.approved).filter_by(learner_email = input_learner_email, course_id = input_course_id, class_id = input_class_id).first()[0]
    if dbEnrolmentApproved == "approved":
        eligibility = False
        reason = "Approved"
        return [eligibility, reason]

    elif dbEnrolmentApproved == "pending":
        eligibility = False
        reason = "Requested"
        return [eligibility, reason]

    if datetime.now() > enrol_end_datetime:
        eligibility = False
        reason = "Enrolment period over"
        return [eligibility, reason]

    # Test Case - Pending
    # {
    #     "learner_email" : "sean@smu.edu.sg",
    #     "course_id" : "REP2101",
    #     "class_id" : 1
    # }

    # Test Case -Approved (need to create test case for approved too)
    # {
    #     "learner_email" : "",
    #     "course_id" : "",
    #     "class_id" : 
    # }

    # Test Case -Approved (need to create test case for class that I can enrol now -> Success test case)
    # {
    #     "learner_email" : "",
    #     "course_id" : "",
    #     "class_id" : 
    # }

    # Check Enrol Before -> Isn't the enrolled before case accounted for by both "Approved" and "Completed" 

    # Account for case where learners applied but rejected.
    #  - Need to allow enrolment attempt even after learner gets rejected -> Currently we don't. DB don't allow.
    #  - Option 1: Search for learner's enrolment, if approved status is "rejected", allow them to apply again. PUT request to change "rejected" to "pending"
    #  - Option 2: Add another field (application_try) with primary key constraint. Autoincrement. Only allow enrolment if previous approved statuses are all "rejected"