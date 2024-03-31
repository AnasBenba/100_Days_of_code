from turtle import Screen, Turtle
from players import Player
from ball import Ball
from scoreboard import ScoreLeft, ScoreRight
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
game_on = True
wall_up_down = 0
with_player = 0
speed = 1


player1 = Player((-350, 0))
player2 = Player((350, 0))
ball = Ball()
score_left = ScoreLeft()
score_right = ScoreRight()
score_left.hideturtle()
score_right.hideturtle()

screen.listen()
screen.onkey(player1.up, 'w')
screen.onkey(player1.down, 's')
screen.onkey(player2.up, 'Up')
screen.onkey(player2.down, 'Down')

while game_on:
    screen.update()
    if ball.distance(player2) < 50 and ball.xcor() < 340:
        speed += 1
        with_player = 1
    elif ball.distance(player1) < 50 and ball.xcor() < -330:
        speed += 1
        with_player = 0
    if ball.ycor() > 285:
        wall_up_down = 1
    elif 0 > ball.ycor() < -285:
        wall_up_down = 0

    ball.move(wall_up_down, with_player, speed)
    time.sleep(0.1)

    if ball.xcor() > 380:
        speed = 0
        ball.refresh()
        wall_up_down = 1
        with_player = 1
        score_right.clear()
        score_right.score_r()
    elif ball.xcor() < -380:
        speed = 0
        ball.refresh()
        wall_up_down = 0
        with_player = 0
        score_left.clear()
        score_left.score_left()

screen.exitonclick()
