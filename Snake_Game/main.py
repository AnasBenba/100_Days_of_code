import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from random import randint

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

# store the parts of the snake
segments = []

# creates snakes

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving the snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extand()
        score.clearscore()
        score.scorechange()
    
    #Detect collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() >290 or snake.segments[0].ycor() < -290:
        score.game_over()
        game_is_on = False

    #Detect collision with the snake body
    
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            score.game_over()
            game_is_on = False
    


screen.exitonclick()
