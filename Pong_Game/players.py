from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape('square')
        self.shapesize(1, 5)
        self.seth(90)
        self.color('white')

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)
