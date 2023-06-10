import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='wog-score-data',
    port='3306',
    database="games"
)
connect = db.connect
db_cursor = db.cursor()


def create_user(name):
    db.connect()
    query='INSERT INTO users_scores (name, score) VALUES (%s, %s)'
    val=(name, 0)
    db_cursor.execute(query, val)
    db.commit()
    db.close()
    
    
def get_user(name):
    db.connect()
    query = 'SELECT score FROM users_scores WHERE name= %s'
    val = (name,)
    db_cursor.execute(query, val)

    myresult = db_cursor.fetchall()

    for u in myresult:
        for i in u:
            return i

def get_all():
    db.connect()
    query='SELECT * FROM users_scores'
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db.close()
    return result


def update_score(score, name):
    db.connect()
    query="UPDATE users_scores SET score = %s WHERE name = %s"
    val=(score, name)
    db_cursor.execute(query, val)
    db.commit()
    db.close()
