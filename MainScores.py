from flask import Flask, render_template
from Utils import BAD_RETURN_CODE as ERROR
from database.Database_actions import get_all, get_user, db

app = Flask('__main__')


@app.route('/')
def show_score(name):
    if db.connect():
        return render_template('/my_score.html', game_score=get_user(name)), 200
    else: 
        return render_template('error.html', error=ERROR), ERROR


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
