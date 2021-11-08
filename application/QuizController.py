from application.models import Quiz, Question, Option, Section
from flask import jsonify
from application import db

class QuizController():
    def view_quiz(self):
        try:
            listOfQuizzes = []

            dbQuizList = Quiz.query.all()

            for q in dbQuizList:
                quizJSON = q.get_details()
                eachQuiz = {
                    "quiz_id": quizJSON["quiz_id"],
                    "quiz_name": quizJSON["quiz_name"]
                }
                listOfQuizzes.append(eachQuiz)
                
            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": {
                        "quiz": listOfQuizzes
                    }
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue viewing the quizzes. " + str(e)
                }
            ), 500
            
    def create_quiz(self, request_body):
        try:
            lastQuiz = Quiz.query.order_by(-Quiz.quiz_id).first().get_details()
            lastQuizId = lastQuiz["quiz_id"]

            new_quiz = Quiz(
                quiz_id = lastQuizId + 1,
                quiz_name = request_body["quiz_name"]
            )

            db.session.add(new_quiz)
            db.session.commit()

            return jsonify(
                {
                    "code": 201,
                    "message": "Success",
                    "quiz_id": lastQuizId + 1
                }
            ), 201

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue creating quiz. " + str(e)
                }
            ), 500

    def update_quiz(self, request_body):
        try:
            quiz_id = request_body["quiz_id"]
            quiz_name = request_body["quiz_name"]

            # Update Quiz Name 
            quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
            quiz.quiz_name = quiz_name
            db.session.commit()

            # Delete
            Option.query.filter(Option.quiz_id == quiz_id).delete()
            Question.query.filter(Question.quiz_id == quiz_id).delete()
            db.session.commit()
            
            # Re-populate
            questions_list = request_body["questions"]

            for question_diction in questions_list:
                question_id = question_diction["question_id"]
                new_question = Question(
                    question_id = question_id,
                    quiz_id = quiz_id,
                    question_text = question_diction["question_text"],
                    answer_id = question_diction["answer_id"]
                )
                
                db.session.add(new_question)
                db.session.commit()
                
                for option_diction in question_diction["options"]:
                    new_option = Option(
                        option_id = option_diction["option_id"],
                        question_id = question_id,
                        quiz_id = quiz_id,
                        option_value = option_diction["option_value"]
                    )

                    db.session.add(new_option)
                    db.session.commit()        

            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "quiz_id": quiz_id
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue updating quiz. " + str(e)
                }
            ), 500



    def view_quiz_details(self, quiz_id):
        try:
            quiz_details = {}
            quiz_details["quiz_id"] = quiz_id

            # Get Quiz Name 
            quiz = Quiz.query.filter_by(quiz_id=quiz_id).first().get_details()
            quiz_details["quiz_name"] = quiz["quiz_name"]

            # Get Question
            list_of_questions = []
            DB_questions_list = Question.query.filter_by(quiz_id=quiz_id).all()

            for DB_question_obj in DB_questions_list:
                DB_question_diction = DB_question_obj.get_details()
                
                question_id = DB_question_diction["question_id"]
                question_obj = {
                    "question_id": question_id,
                    "question_text": DB_question_diction["question_text"],
                    "answer_id": DB_question_diction["answer_id"]
                }
                
                DB_options_list = Option.query.filter_by(quiz_id=quiz_id, question_id=question_id).all()
                options_list = []
                for DB_option_obj in DB_options_list:
                    DB_option_diction = DB_option_obj.get_details()

                    option_obj = {
                        "option_id": DB_option_diction["option_id"],
                        "option_value": DB_option_diction["option_value"]
                    }

                    options_list.append(option_obj)
                
                question_obj["options"] = options_list
                list_of_questions.append(question_obj)

            quiz_details["questions"] = list_of_questions

            return jsonify(
                {
                    "code": 200,
                    "message": "Success",
                    "data": quiz_details
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue viewing quiz. " + str(e)
                }
            ), 500

    def attach_quiz(self, request_body):
        try:
            course_id = request_body["course_id"]
            class_id = request_body["class_id"]
            class_start_datetime = request_body["class_start_datetime"]
            section_id = request_body["section_id"]
            quiz_id = request_body["quiz_id"]

            section_obj = Section.query.filter_by(
                course_id=course_id, 
                class_id=class_id, 
                class_start_datetime=class_start_datetime,
                section_id = section_id
                ).first()

            
            section_obj.quiz_id = quiz_id
            db.session.commit()

            return jsonify(
                {
                    "code": 200,
                    "message": "Success"
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "There was an issue attaching quiz. " + str(e)
                }
            ), 500







            # Query quiz id from the quiz name
            # quiz_id = ???
            # new_question = Question(   
            #     question_id = request_body["question_id"],
            #     quiz_id = request_body["quiz_id"],
            #     question_text = request_body["question_text"],
            #     answer_id = request_body["answer_id"]
            # )

            # new_option = Option(
            #     option_id = request_body["option_id"],
            #     question_id = request_body["question_id"],
            #     quiz_id = request_body["quiz_id"],
            #     option_value = request_body["option_value"]
            # )

            # Input: Quiz name, question_id, question_text, answer_id, option_id, option_value

            # Create quiz, Create question, Create option
            # Attach option to question, attach question to quiz, attach quiz to section