"""Data models."""
from . import db # import db object created in __init__.py
from datetime import datetime

class Learner(db.Model):
    __tablename__ = 'learner'
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    designation = db.Column(db.String(64), nullable=False)
    department = db.Column(db.String(64), nullable=False)

    def __init__(self, email, name, password, designation, department):
        self.email = email
        self.name = name
        self.password = password
        self.designation = designation
        self.department = department

    def get_details(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "designation": self.designation,
            "department": self.department
        }

class HR(db.Model):
    __tablename__ = 'hr'
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def get_details(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password
        }

class Trainer(db.Model):
    __tablename__ = 'trainer'
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def get_details(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password
        }

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.String(7), primary_key=True)
    course_name = db.Column(db.String(64), nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String(512), nullable=False)


    def __init__(self, course_id, course_name, created_datetime, description):
        self.course_id = course_id
        self.course_name = course_name
        self.created_datetime = created_datetime
        self.description = description

    def get_details(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "created_datetime": self.created_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "description": self.description
        }

class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer, primary_key=True)
    class_size = db.Column(db.Integer, nullable=False)
    trainer_email = db.Column(db.String(64),db.ForeignKey('trainer.email'), nullable=True)
    enrol_start_datetime = db.Column(db.DateTime, nullable=False)
    enrol_end_datetime = db.Column(db.DateTime, nullable=False)
    start_datetime = db.Column(db.DateTime, primary_key=True)
    end_datetime = db.Column(db.DateTime, nullable=False)
    course_id = db.Column(db.String(7),db.ForeignKey('course.id'), primary_key=True)

    def __init__(self, class_id, class_size, trainer_email, start_datetime, end_datetime, course_id, enrol_start_datetime, enrol_end_datetime):
        self.class_id = class_id
        self.class_size = class_size
        self.trainer_email = trainer_email
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.course_id = course_id
        self.enrol_start_datetime = enrol_start_datetime
        self.enrol_end_datetime = enrol_end_datetime

    def get_details(self):
        return {
            "class_id": self.class_id,
            "class_size": self.class_size,
            "trainer_email": self.trainer_email,
            "start_datetime": self.start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "end_datetime": self.end_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "course_id": self.course_id,
            "enrol_start_datetime": self.enrol_start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "enrol_end_datetime": self.enrol_end_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }


class Enrolment(db.Model):
    __tablename__ = 'enrolment'
    learner_email = db.Column(db.String(64), db.ForeignKey('learner.email'), primary_key=True)
    enrolment_datetime = db.Column(db.DateTime, nullable=False)
    course_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), primary_key=True)
    class_start_datetime = db.Column(db.DateTime, db.ForeignKey('class.start_datetime'), primary_key=True)
    hr_enroler_email = db.Column(db.String(64), db.ForeignKey('hr.email'), nullable=True)
    approver_email = db.Column(db.String(64), db.ForeignKey('hr.email'), nullable=True)
    status = db.Column(db.String(10), nullable=False)

    def __init__(self, learner_email, course_id, class_id, class_start_datetime, hr_enroler_email, status, enrolment_datetime = datetime.now()):
        self.learner_email = learner_email
        self.enrolment_datetime = enrolment_datetime
        self.course_id = course_id
        self.class_id = class_id
        self.class_start_datetime = class_start_datetime
        self.hr_enroler_email = hr_enroler_email
        self.status = status
        

    def get_details(self):
        return {
            "learner_email": self.learner_email,
            "enrolment_datetime": self.enrolment_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "course_id": self.course_id,
            "class_id": self.class_id,
            "class_start_datetime": self.class_start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "hr_enroler_email": self.hr_enroler_email,
            "status": self.status
        }

class Prerequisite(db.Model):
    __tablename__ = 'prerequisite'
    prerequisite_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    postrequisite_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    created_datetime = db.Column(db.DateTime, nullable=True)

    def __init__(self, prerequisite_id, postrequisite_id, created_datetime):
        self.prerequisite_id = prerequisite_id
        self.postrequisite_id = postrequisite_id
        self.created_datetime = created_datetime
    
    def get_details(self):
        return {
            "prerequisite_id": self.prerequisite_id,
            "postrequisite_id": self.postrequisite_id,
            "created_datetime": self.created_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }

class Completed(db.Model):
    __tablename__ = 'completed'
    learner_email = db.Column(db.String(64), db.ForeignKey('learner.email'), primary_key=True)
    course_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    completion_datetime = db.Column(db.DateTime, nullable=True)

    def __init__(self, learner_email, course_id, completion_datetime = datetime.now()):
        self.learner_email = learner_email
        self.course_id = course_id
        self.completion_datetime = completion_datetime
    
    def get_details(self):
        return {
            "learner_email": self.learner_email,
            "course_id": self.course_id,
            "completion_datetime": self.completion_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }

class Quiz(db.Model):
    __tablename__ = 'quiz'
    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(64), nullable=False)
    
    def __init__(self, quiz_id, quiz_name):
        self.quiz_id = quiz_id
        self.quiz_name = quiz_name
    
    def get_details(self):
        return {
            "quiz_id": self.quiz_id,
            "quiz_name": self.quiz_name
        }

class Section(db.Model):
    __tablename__ = 'section'
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(64), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), primary_key=True)
    course_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    class_start_datetime = db.Column(db.DateTime, db.ForeignKey('class.start_datetime'), primary_key=True)

    def __init__(self, section_id, section_name, quiz_id, class_id, course_id, class_start_datetime):
        self.section_id = section_id
        self.section_name = section_name
        self.quiz_id = quiz_id
        self.class_id = class_id
        self.course_id = course_id
        self.class_start_datetime = class_start_datetime
    
    def get_details(self):
        return {
            "section_id": self.section_id,
            "section_name": self.section_name,
            "quiz_id": self.quiz_id,
            "class_id": self.class_id,
            "course_id": self.course_id,
            "class_start_datetime": self.class_start_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }

class Material(db.Model):
    __tablename__ = 'course_material'
    material_id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.section_id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('section.class_id'), primary_key=True)
    course_id = db.Column(db.String(7), db.ForeignKey('section.course_id'), primary_key=True)
    class_start_datetime = db.Column(db.DateTime, db.ForeignKey('section.class_start_datetime'), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    view_link = db.Column(db.String(256), nullable=False)
    download_link = db.Column(db.String(256), nullable=False)
    
    def __init__(self, material_id, section_id, class_id, course_id, class_start_datetime, title, view_link, download_link):
        self.material_id = material_id
        self.section_id = section_id
        self.class_id = class_id
        self.course_id = course_id
        self.class_start_datetime= class_start_datetime
        self.title = title
        self.view_link = view_link
        self.download_link = download_link

    def get_details(self):
        return {
            "material_id": self.material_id,
            "section_id": self.section_id,
            "class_id": self.class_id,
            "course_id": self.course_id,
            "class_start_datetime": self.class_start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "title": self.title,
            "view_link": self.view_link,
            "download_link": self.download_link
        }

class Question(db.Model):
    __tablename__ = 'question'
    question_id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(128), nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, question_id, quiz_id, question_text, answer_id):
        self.question_id = question_id
        self.quiz_id = quiz_id
        self. question_text =  question_text
        self.answer_id = answer_id

    def get_details(self):
        return {
            "question_id": self.question_id,
            "quiz_id": self.quiz_id,
            "question_text": self.question_text,
            "answer_id": self.answer_id
        }

class Option(db.Model):
    __tablename__ = 'option'
    option_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, primary_key=True)
    option_value = db.Column(db.String(128), nullable=False)
    
    def __init__(self, option_id, question_id, quiz_id, option_value):
        self.option_id = option_id
        self.question_id = question_id
        self.quiz_id = quiz_id
        self.option_value = option_value

    def get_details(self):
        return {
            "option_id": self.option_id,
            "question_id": self.question_id,
            "quiz_id": self.quiz_id,
            "option_value": self.option_value
        }