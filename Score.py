from database.Database_actions import get_user, update_score


def add_score(difficulty, username):
    print(difficulty)
    score = (difficulty * 3) + 5
    update_score(score, username)
    return get_user(username)
