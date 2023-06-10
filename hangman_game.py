import os
import random
import hangman_art as art
import hangman_words as word

# Select a random word from the word list
chosen_word = random.choice(word.word_list)

# Print the hangman ASCII art
print(art.logo)

# Set the initial number of lives
lives = 6

# Initialize a flag variable to track the game state
flag = 1

# Create a list to store the current display of letters
display = ['_'] * len(chosen_word)

# Variables to store guessed and not-in-the-word letters
you_guess_it = ''
it_not_in = ''

# Main game loop, continues until all letters are guessed or lives run out
while '_' in display:
  flag = 1

  # Ask the user to input a letter guess
  guess = input("Guess a letter:  ").lower()
  os.system('clear') # Clear the console screen

  if guess in you_guess_it:
    # Check if the letter has already been guessed
    print(f"You've already guessed {guess}")
    
  # Iterate through each character in the chosen word
  for i in range(len(chosen_word)):
    if guess in chosen_word[i]:
      # If the guessed letter is in the chosen word, update the display
      flag = 0
      display[i] = guess
      you_guess_it += guess

  # Print the current display of letters
  print("".join(display))

  if flag == 0:
    # If the guessed letter is correct, print the corresponding hangman stage
    print(art.stages[lives])
  
  if flag == 1:
    # If the guessed letter is incorrect, reduce a life and print the corresponding hangman stage
    print(art.stages[lives])
    it_not_in = guess
    print(f"You guessed {it_not_in}, that's not in the word. You lose a life.")
    lives -= 1

  if lives < 0:
    # If lives run out, end the game and print he lose
    flag = 1
    print("You Lose!")
    break

# Game ended, and the player won
if flag == 0:
  print("You Win!")