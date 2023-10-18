def report(money, reso):
    for key, value in reso.items():
        res = key.capitalize()
        if res == 'Coffee':
            print(res + ':', value, end='')
            print('g')
        else:
            print(res + ':', value, end='')
            print('ml')
    print('Money: $', end='')
    print('{:.1f}'.format(money))


def report_updated(res, coffee):
    new_dict = {}
    if coffee == 'espresso':
        new_dict['water'] = res['water'] - 50
        new_dict['coffee'] = res['coffee'] - 18
        new_dict['milk'] = res['milk']
    elif coffee == 'latte':
        new_dict['water'] = res['water'] - 200
        new_dict['coffee'] = res['coffee'] - 24
        new_dict['milk'] = res['milk'] - 150
    elif coffee == 'cappuccino':
        new_dict['water'] = res['water'] - 250
        new_dict['coffee'] = res['coffee'] - 24
        new_dict['milk'] = res['milk'] - 100
    return new_dict


def is_enough(money_inserted, coffee_cost, coffee, a_dict):
    money = 0
    my_dict = {}
    if money_inserted > coffee_cost:
        change = money_inserted - coffee_cost
        money = coffee_cost
        print('Here is ${:.1f} dollars in change.'.format(change))
        print('Here is your {} ☕. Enjoy!'.format(coffee))
        my_dict = report_updated(a_dict, coffee)
    elif money_inserted == coffee_cost:
        money = coffee_cost
        print('Here is your {} ☕. Enjoy!'.format(coffee))
        my_dict = report_updated(a_dict, coffee)
    else:
        print('Sorry that\'s not enough money. Money refunded.')
    return money, my_dict
