import random
import re


def generate_number(diff):
    secret_number = random.randint(1, diff)
    return secret_number


def get_guess_from_user(diff):
    guess = input(f'guess a number from 1 to {diff}:')
    while re.match(r"^(?![1-5]$)|^$", guess):
        guess = input(f'guess a number from 1 to {diff}:')
    return int(guess)


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    else:
        return False


def play(diff):
    return compare_results(generate_number(diff), get_guess_from_user(diff))
