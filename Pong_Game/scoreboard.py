from turtle import Turtle


class ScoreLeft(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score1 = 0
        self.score_left()

    def score_left(self):
        self.penup()
        self.goto(100, 230)
        self.write(f'{self.score1}', font=('Arial', 45, 'normal'))
        self.score1 += 1


class ScoreRight(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score2 = 0
        self.score_r()

    def score_r(self):
        self.penup()
        self.goto(-130, 230)
        self.write(f'{self.score2}', font=('Arial', 45, 'normal'))
        self.score2 += 1
