from flask import Flask
from Utils import SCORES_FILE_NAME
from Utils import BAD_RETURN_CODE as ERROR
from os.path import exists

app = Flask('__main__')


@app.route('/')
def show_score():
    file = SCORES_FILE_NAME
    if exists(file):
        with open(file, 'r', encoding='utf8') as score_file:
            score = score_file.readline()
            return f'''<html>
                       <head>
                           <title>Scores Game</title>
                       </head>
                       <body>
                           <h1>The score is 
                               <div id="score">{score}</div>
                           </h1>
                       </body>
                       </html>''', 200
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
                   </html>''', ERROR


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
