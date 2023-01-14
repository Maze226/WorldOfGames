def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).' \
           f'Here you can find many cool games to play.'


def load_game():
    games = input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
Enter your choice: """)

    if games.isdigit() and int(games) in range(1, 4):
        difficulty = input("Please choose game difficulty from 1 to 5:")
        if difficulty.isdigit() and int(difficulty) in range(1, 6):
            print(games, difficulty)
            return games, difficulty
        else:
            print('Nope')
    else:
        load_game()
