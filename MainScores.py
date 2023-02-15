from flask import Flask
from Utils import SCORES_FILE_NAME
from Utils import BAD_RETURN_CODE as ERROR

app = Flask('__main__')


@app.route('/')
def show_score():
    with open(SCORES_FILE_NAME, 'r', encoding='utf8') as file:
        if file:
            score = file.readline()
            return f'''<html>
                       <head>
                           <title>Scores Game</title>
                       </head>
                       <body>
                           <h1>The score is 
                               <div id="score">{score}</div>
                           </h1>
                       </body>
                       </html>'''
        else:
            return f'''<html> 
                       <head>
                           <title>Scores Game</title>
                       </head>
                       <body>
                           <h1>
                               <div id="score" style="color:red">{ERROR}</div>
                           </h1>
                       </body>
                       </html>'''


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
