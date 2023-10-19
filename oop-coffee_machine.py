from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
report = CoffeeMaker()
profit = MoneyMachine()
order = ''
drink_orderd = Menu()
drink = None
while True:
    order = input(f"What would you like? ({items.get_items()}): ").lower()
    if order == 'off':
        break
    if order == 'report':
        report.report()
        profit.report()
    else:
        drink = drink_orderd.find_drink(order)
        if report.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                report.make_coffee(drink)
