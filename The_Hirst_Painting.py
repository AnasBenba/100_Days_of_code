from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()
my_colors = [(207, 160, 82), (54, 88, 130), (140, 26, 49), (221, 207, 105), (132, 177, 203),
             (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
             (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
             (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
screen.colormode(255)
tim.hideturtle()
tim.penup()
y = -200
tim.goto(-250, y)


def draw_dots(colors):
    for i in range(10):
        tim.speed(6)
        tim.dot(20, random.choice(colors))
        tim.penup()
        if i != 9:
            tim.forward(50)
        tim.pendown()


def new_position(u):
    pos = 50
    tim.speed(0)
    tim.penup()
    if u != 250:
        for _ in range(2):
            tim.left(90)
            tim.forward(50)
    return pos


for _ in range(10):
    tim.goto(-250, y)
    draw_dots(my_colors)
    y += new_position(y)
    tim.right(180)


screen.exitonclick()
