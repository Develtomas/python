class QuizBrain:
    def __init__(self, q_lister):
        self.question_number = 0
        self.question_list = q_lister
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        num = self.question_number
        self.question_number += 1
        answ = input(f'Q.{self.question_number}: {self.question_list[num].text} (True/False)?: ')
        self.check_score(answ, self.question_list[num].answer)

    def check_score(self, inp_answer, correct_answer):
        if inp_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You are right!')
        else:
            print(f'Wrong!')
        print(f'Current score {self.score}/{self.question_number}\n')

    def final_score_print(self):
        print(f"You've finished quiz. Scores: {self.score}/{self.question_number}")
