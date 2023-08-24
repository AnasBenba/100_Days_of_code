from The_Number_Guessing_Game_art import logo
import random
from high_or_low import high_low

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number_to_guess = int(random.uniform(1, 100))
hard = 5
easy = 10
guess = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
    high_low(guess, number_to_guess, hard)
elif difficulty == 'easy':
    high_low(guess, number_to_guess, easy)