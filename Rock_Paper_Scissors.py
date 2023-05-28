# import the random module and sys
import random
import sys

# Define the ASCII art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Declare a list that contains the variables rock, paper, and scissors
List_RPS = [rock, paper, scissors]
# Get the user's choice and generate a random number for the computer's choice
number_to_use = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_number = random.randint(0, 2)
# Check if the user entered the wrong number and exit the program
if number_to_use > 2:
  print("wrong choice")
  sys.exit()
# Print the choices of the user and the computer 
print('\n')
print("You chose:")
print(List_RPS[number_to_use])
print("Computer chose:")
print(List_RPS[computer_number])
# Check if it's a draw, lose, or win
if number_to_use == computer_number:
  print("It's a draw")
elif number_to_use == 0 and computer_number == 1:
  print("You lose")
elif number_to_use == 1 and computer_number == 2:
  print("You lose")
elif number_to_use == 2 and computer_number == 0:
  print("You lose")
else:
  print("You win")