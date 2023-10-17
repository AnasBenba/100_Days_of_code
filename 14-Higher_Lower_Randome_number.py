from random import randint

def random_list(data, data_len):
    my_list = []
    for num in data:
        my_list = []
        number_A = randint(0, data_len - 1)
        my_list.append(number_A)
        number_B = randint(0, data_len - 1)
        my_list.append(number_B)
        if number_A is not number_B:
            break
    return my_list

def random_number(number_A, data_len):
    number = 0
    i = 0
    while i <= data_len - 1:
        number = randint(0, data_len - 1)
        if number is not number_A:
            break
        i += 1
    return number