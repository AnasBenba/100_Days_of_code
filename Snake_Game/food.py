from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        Random_x = random.randint(-280, 280)
        Random_y = random.randint(-280, 280)
        self.goto(Random_x, Random_y)