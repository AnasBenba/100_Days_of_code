import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


def increment_speed():
    return MOVE_INCREMENT


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 2)
        self.goto(random.randint(330, 400), random.randint(-230, 230))
        self.color(COLORS[random.randint(0, 5)])

    def move(self, arg):
        self.bk(arg)
