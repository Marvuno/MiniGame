from quiz_game.question_model import Question
from quiz_game.data import question_data
from quiz_game.quiz_brain import QuizBrain
from quiz_game.ui import Interface


def Quizzler_Game():
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = Interface(quiz)
