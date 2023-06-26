import os
from art import logo

# Print the logo and welcome message
print(logo)
print("Welcome to the secret auction program.")

# Create an empty dictionary to store the bidders and their bids
my_dict = {}

# Initialize variables to track the maximum bid and the corresponding bidder's name
max_bid = 0
name_bid = ''

# Start a loop to collect bids from bidders
while True:
    # Prompt the user to enter their name
    name = input("What is your name?: ")
    # Prompt the user to enter their bid
    bid = int(input("What's your bid?: $"))
    
    # Add the bidder's name and bid to the dictionary
    my_dict[name] = bid
    
    # Ask if there are any other bidders
    continue_or_not = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    # If there are no other bidders, exit the loop
    if continue_or_not == 'no':
        break
    else:
        os.system('clear') # Clear the console to hide previous bidder's information

# Find the bidder with the highest bid
for key in my_dict:
    if max_bid < my_dict[key]:
        max_bid = my_dict[key]
        name_bid = key

# Print the winner's name and bid
print(f"The winner is {name_bid} with a bid of ${max_bid}")