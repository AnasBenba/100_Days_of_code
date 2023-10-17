from Higher_Lower_art import logo, vs
from Higher_Lower_game_data import data
from Higher_Lower_Random_number import random_number, random_list
import os
from Higher_Lower_generate_result import generate_result

data_len = len(data)
my_list = random_list(data, data_len)
number_A = my_list[0]
number_B = my_list[1]
score = 0
result_list = ['', f"You\'re right! Current score: {score}.", f"Sorry, that\'s wrong. Final score: {score}"]
result = 0

while True:
    if result == 0:
        print(logo)
    elif result == 1:
        print(logo + '\n', result_list[result])
    elif result == 2:
        print(logo + '\n', result_list[result])
        break
    Compare = data[number_A]
    A = Compare['follower_count']
    print(f"Compare A: {Compare['name']}, {Compare['description']}, {Compare['country']}")
    print(vs)
    Against = data[number_B]
    B = Against['follower_count']
    print(f"Against B: {Against['name']}, {Against['description']}, {Against['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
        if A > B:
            score += 1
            result_list = generate_result(score)
            number_A = number_B
            number_B = random_number(number_A, data_len)
            os.system('clear')
            result = 1
        else:
            os.system('clear')
            result = 2
    
    if answer == 'B':
        if B > A:
            score += 1
            result_list = generate_result(score)
            number_A = number_B
            number_B = number_B = random_number(number_A, data_len)
            os.system('clear')
            result = 1
        else:
            os.system('clear')
            result = 2