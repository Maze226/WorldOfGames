import random
import re


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        guess = input(f'guess a number from 1 to {difficulty}:')
        if not re.match(r"^(?![1-5]$)|^$", guess):
            break
    return int(guess)


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))
