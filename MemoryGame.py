import random
import time
import re


def generate_sequence(difficulty):
    generated_list = []
    for i in range(int(difficulty)):
        generated_list.append(random.randint(1, 101))
    print(generated_list, end='\r')
    time.sleep(0.7)
    print('                    ')
    return generated_list


def get_list_from_user(difficulty):
    users_list = []
    for i in range(int(difficulty)):
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


def play(difficulty):
    return is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
