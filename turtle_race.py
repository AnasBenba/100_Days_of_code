from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
i = 0
race_is_on = False

my_list = []
random.shuffle(colors)

for ob in range(6):
    new_ob = Turtle(shape='turtle')
    new_ob.penup()
    new_ob.color(colors[i])
    new_ob.goto(x=-230, y=y)
    y += 40
    i += 1
    my_list.append(new_ob)

if user_bet:
    race_is_on = True
    winner = ''
    while race_is_on:
        for ob in my_list:
            move = random.randint(0, 10)
            if ob.xcor() > 230:
                winner = ob.pencolor()
                race_is_on = False
            ob.forward(move)
    if user_bet == winner:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost! The {winner} turtle is the winner!")


screen.exitonclick()

