from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question obj list
question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

# init
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
# final score
quiz.final_score_print()