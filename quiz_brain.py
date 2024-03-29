class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        length = len(self.question_list)
        i = self.question_number
        return i < length

    def next_question(self):
        text = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {text.text} (True/False)?: ').capitalize()
        self.check_answer(answer, text.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print('You got it right!')
        else:
            print('You got it wrong!')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')

