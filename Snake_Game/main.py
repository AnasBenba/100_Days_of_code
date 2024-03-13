import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

# store the parts of the snake
segments = []

# creates snakes

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving the snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1mkdir)
    snake.move()
screen.exitonclick()
