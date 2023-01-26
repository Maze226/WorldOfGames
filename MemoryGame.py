import random
import time
import re


def generate_sequence(diff):
    generated_list = []
    for i in range(int(diff)):
        generated_list.append(random.randint(1, 101))
    print(generated_list, end='\r')
    time.sleep(0.7)
    print('                    ')
    return generated_list


def get_list_from_user(diff):
    users_list = []
    for i in range(int(diff)):
        enter_item = input(f'Please enter the {i + 1} item:')
        while not re.match(r"^([1-9]|[1-9][0-9]|100|101)$", enter_item):
            enter_item = input(f'Please enter the {i + 1} item:')
        users_list.append(int(enter_item))
    return users_list


def is_list_equal(generated_list, users_list):
    if generated_list == users_list:
        return True
    else:
        return False


def play(diff):
    print(is_list_equal(generate_sequence(diff), get_list_from_user(diff)))
