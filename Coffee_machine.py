import sys
from my_functions_coffee_machine import report, is_enough
from my_data_coffee_machine import MENU, resources, coins

to_add = 0
money = 0
money_inserted = 0
espresso_cost = MENU['espresso']['cost']
latte_cost = MENU['latte']['cost']
cappuccino_cost = MENU['cappuccino']['cost']
a_dict = resources

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'report':
        report(money, a_dict)
    elif choice == 'off':
        sys.exit()

    elif choice == 'espresso':
        if a_dict['water'] < 50:
            print('Sorry there is not enough water.')
        elif a_dict['coffee'] < 18:
            print('Sorry there is not enough coffee.')
        else:
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickels?: '))
            pennies = int(input('how many pennies?: '))
            money_inserted = coins['quarter'] * quarters + coins['dime'] * dimes + coins['nickel'] * nickles + coins['penny'] * pennies
            to_add, a_dict = is_enough(money_inserted, espresso_cost, "espresso", a_dict)
            money += to_add

    elif choice == 'latte':
        if a_dict['water'] < 200:
            print('Sorry there is not enough water.')
        elif a_dict['coffee'] < 24:
            print('Sorry there is not enough coffee.')
        elif a_dict['milk'] < 150:
            print('Sorry there is not enough milk.')
        else:
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickels?: '))
            pennies = int(input('how many pennies?: '))
            money_inserted = coins['quarter'] * quarters + coins['dime'] * dimes + coins['nickel'] * nickles + coins['penny'] * pennies
            to_add, a_dict = is_enough(money_inserted, latte_cost, "latte", a_dict)
            money += to_add

    elif choice == 'cappuccino':
        if a_dict['water'] < 250:
            print('Sorry there is not enough water.')
        elif a_dict['coffee'] < 24:
            print('Sorry there is not enough coffee.')
        elif a_dict['milk'] < 100:
            print('Sorry there is not enough milk.')
        else:
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickels?: '))
            pennies = int(input('how many pennies?: '))
            money_inserted = coins['quarter'] * quarters + coins['dime'] * dimes + coins['nickel'] * nickles + coins['penny'] * pennies
            to_add, a_dict = is_enough(money_inserted, cappuccino_cost, "cappuccino", a_dict)
            money += to_add
