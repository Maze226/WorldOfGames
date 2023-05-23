from Live import load_game, welcome
from database.Database_actions import create, get_user
from MainScores import show_score

while True:
    name = input("What is your name?")
    check = get_user(name)
    if check is None and name != '':
        create(name)
        break


welcome(name)
load_game(name)
