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


