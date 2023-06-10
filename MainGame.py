from Live import load_game, welcome
from database.Database_actions import create_user, get_user

while True:
    name = input("What is your name?")
    check = get_user(name)
    if check is None and name != '':
        create_user(name)
        break


welcome(name)
load_game(name)
