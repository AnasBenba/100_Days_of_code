from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x = 0
        self.y = 0
        self.penup()

    def move(self, arg1, arg2, arg3):
        if arg1 == 1:
            self.y -= 13
        else:
            self.y += 13
        if arg2 == 1:
            self.x -= 13 + arg3
        else:
            self.x += 13 + arg3
        self.goto(self.x, self.y)

    def refresh(self):
        self.x = 0
        self.y = 0
        self.goto(self.x, self.y)
