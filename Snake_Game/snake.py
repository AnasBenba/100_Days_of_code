# This class is responsible for creating the snake and its movement.
from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.x = 0
        self.y = 0
        self.position = (self.x, self.y)
        self.create_snake()

    def create_snake(self):
        for _ in range(0, 3):
            self.add_segment(self.position)
    
    def add_segment(self, position):
        s = Turtle(shape="square")
        s.color("white")
        s.penup()
        my_list = list(position)
        s.goto(my_list[0], my_list[1])
        my_list[0] += -20
        self.segments.append(s)
    
    def extand(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)
