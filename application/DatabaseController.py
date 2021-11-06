from flask import jsonify
import os
import sqlalchemy 
from flask_sqlalchemy import SQLAlchemy

class DatabaseController():
    def up_database(self,app):

        db = SQLAlchemy(app)
        dirname = os.path.dirname(os.path.dirname( __file__ ))
        fd = open(os.path.join(dirname, "sql\\main_test.sql"), 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            print("starting")
            try:
                if command.strip() != '':
                    print(command)
                    db.engine.execute(command)
            except IOError as msg:
                print("Command skipped: ", msg)

    def down_database(self,app):
        db = SQLAlchemy(app)
        dirname = os.path.dirname(os.path.dirname( __file__ ))
        fd = open(os.path.join(dirname, "sql\\end_test.sql"), 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            print("starting")
            try:
                if command.strip() != '':
                    print(command)
                    db.engine.execute(command)
            except IOError as msg:
                print("Command skipped: ", msg)

    # Add more functions here 