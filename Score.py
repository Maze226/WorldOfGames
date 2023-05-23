from database.Database_actions import get_score, update


def add_score(difficulty, username):
    print(difficulty)
    score = (difficulty * 3) + 5
    update(score, username)
    return get_score(username)
