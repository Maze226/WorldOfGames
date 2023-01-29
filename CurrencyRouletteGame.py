import requests
import random
import re


def get_money_interval(d):
    usd_amount = random.randint(1, 100)
    req = requests.get('https://v6.exchangerate-api.com/v6/615ee5a543815d1e4d0f04da/latest/USD')
    res = req.json()
    convert_rates = res['conversion_rates']
    currency = convert_rates['ILS']
    interval = (currency * usd_amount - (5 - d), currency * usd_amount + (5 - d))
    print(f'How much ILS you will get from ${usd_amount} if the currency rate is {currency}?')
    return interval


def get_guess_from_user(interval):
    user_guess = input(f'What is your guess:')
    while re.match("^[a-zA-Z0-9]*$", user_guess):
        user_guess = input(f'What is your guess:')
    if interval[0] <= float(user_guess) <= interval[1]:
        return True
    else:
        return False


def play(d):
    return get_guess_from_user(get_money_interval(d))
