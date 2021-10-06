"""Data models."""
from . import db # import db object created in __init__.py

class Learner(db.Model):
    __tablename__ = 'learner'
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def json(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password
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

    def json(self):
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

    def json(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password
        }

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.String(7), primary_key=True)
    course_name = db.Column(db.String(64), nullable=False)
    created_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, course_id, course_name, created_date):
        self.course_id = course_id
        self.course_name = course_name
        self.created_date = created_date

    def json(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "created_date": self.created_date
        }

class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer, primary_key=True)
    class_size = db.Column(db.Integer, nullable=False)
    trainer_email = db.Column(db.String(64),db.ForeignKey('trainer.email'), nullable=True)
    start_datetime = db.Column(db.DateTime, nullable=True)
    end_datetime = db.Column(db.DateTime, nullable=True)
    course_id = db.Column(db.String(7),db.ForeignKey('course.id'), primary_key=True)

    def __init__(self, class_id, class_size, trainer_email, start_datetime, end_datetime, course_id):
        self.class_id = class_id
        self.class_size = class_size
        self.trainer_email = trainer_email
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.course_id = course_id

    def json(self):
        return {
            "class_id": self.class_id,
            "class_size": self.class_size,
            "trainer_email": self.trainer_email,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "course_id": self.course_id
        }


class Enrolment(db.Model):
    __tablename__ = 'enrolment'
    learner_email = db.Column(db.String(64), db.ForeignKey('learner.email'), primary_key=True)
    enrolment_date = db.Column(db.DateTime, nullable=False)
    course_id = db.Column(db.String(7), db.ForeignKey('course.id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), primary_key=True)
    class_start_datetime = db.Column(db.DateTime, db.ForeignKey('class.start_datetime'), primary_key=True)
    hr_enroler_email = db.Column(db.String(64), db.ForeignKey('hr.email'), nullable=True)
    approver_email = db.Column(db.String(64), db.ForeignKey('hr.email'), nullable=False)

    def __init__(self, learner_email, enrolment_date, course_id, class_id, class_start_datetime, hr_enroler_email):
        self.learner_email = learner_email
        self.enrolment_date = enrolment_date
        self.course_id = course_id
        self.class_id = class_id
        self.class_start_datetime = class_start_datetime
        self.hr_enroler_email = hr_enroler_email
        

    def json(self):
        return {
            "learner_email": self.learner_email,
            "enrolment_date": self.enrolment_date,
            "course_id": self.course_id,
            "class_id": self.class_id,
            "class_start_datetime": self.class_start_datetime,
            "hr_enroler_email": self.hr_enroler_email
        }

class Prerequisite(db.Model):
    __tablename__ = 'prerequisite'
    prerequisite_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    postrequisite_id = db.Column(db.String(7), db.ForeignKey('course.course_id'), primary_key=True)
    created_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, prerequisite_id, postrequisite_id, created_date):
        self.prerequisite_id = prerequisite_id
        self.postrequisite_id = postrequisite_id
        self.created_date = created_date
    
    def json(self):
        return {
            "prerequisite_id": self.prerequisite_id,
            "postrequisite_id": self.postrequisite_id,
            "created_date": self.created_date
        }