import time
from turtle import Screen
from player import Player
from car_manager import CarManager, increment_speed, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

cars_list = []
flag = 0
to_create = 8
speed = STARTING_MOVE_DISTANCE

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if flag == to_create:
        flag = 0
    if flag == 0 or to_create == 0:
        car_manager = CarManager()
        cars_list.append(car_manager)
    flag += 1
    if player.next():
        speed += increment_speed()
        if to_create != 0:
            to_create -= 1
        scoreboard.level_up()
    for car in cars_list:
        car.move(speed)
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
