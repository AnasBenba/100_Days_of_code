from Blackjack_Art import logo
import os
import random
from Calculate_score import calculate_score

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    me = []
    me_1 = random.choice(cards)
    me.append(me_1)
    comp = []
    start = input("do you want to play a game of Blackjack? type 'y' or 'n': ")
    as_long_as = True
    os.system('clear')
    print(logo)
    
    if start == 'n':
        os.system('clear')
        break
    elif start == 'y':
        while as_long_as:
            current_score = 0
            comp_score = 0
            if start == 'y': 
                if current_score <= 21 and comp_score <= 21:
                    me_1 = random.choice(cards)
                    me.append(me_1)
                    comp_1 = random.choice(cards)
                    comp.append(comp_1)
                    current_score = calculate_score(me)
                    print(f"Your cards: {me}, current score: {current_score}")
                    print(f"Computer's first card: {comp[0]}")
                if current_score > 21 :
                    comp_score = calculate_score(comp)
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("You went over. You lose 😭")
                    as_long_as = False
                if comp_score > 21:
                    comp_score = calculate_score(comp)
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("Opponent went over. You win 😁")
                    as_long_as = False
            
            elif start == 'n':
                comp_score = calculate_score(comp)
                current_score = calculate_score(me)
                while comp_score < 16:
                    comp_1 = random.choice(cards)
                    comp.append(comp_1)
                    comp_score += comp_1
                
                if current_score > comp_score and current_score <= 21:
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("You win 😁")
                    as_long_as = False
                
                elif current_score < comp_score and comp_score <= 21:
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("You lose 😭")
                    as_long_as = False
                    
                elif current_score > 21 :
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("You went over. You lose 😭")
                    as_long_as = False
                    
                elif comp_score > 21:
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("Opponent went over. You win 😁")
                    as_long_as = False
                
                else:
                    print(f"Your final hand: {me}, final score: {current_score}")
                    print(f"Computer's final hand: {comp}, final score: {comp_score}")
                    print("Draw")
                    as_long_as = False
            if as_long_as == True:
                start = input("Type 'y' to get another card, type 'n' to pass: ")