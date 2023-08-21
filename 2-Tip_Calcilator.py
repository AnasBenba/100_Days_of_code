print("Welcome to the tip calculator!")

# get the user input and convert it to a float

total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# calculate how much each person should pay

tip = total_bill * (percentage_tip / 100)
bill_per_person = (total_bill + tip) / number_of_people
result = "{:.2f}".format(bill_per_person)

# print the result

print(f"Each person should pay: ${result}")
