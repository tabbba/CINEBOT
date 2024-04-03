import sqlite3

DATABASE_NAME = "movie_ratings.db"

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    
    # Create Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE)''')
    
    # Create Ratings table
    c.execute('''CREATE TABLE IF NOT EXISTS ratings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, movie_name TEXT, rating INTEGER,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    conn.commit()
    conn.close()

def insert_user(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO users (username) VALUES (?)', (username,))
    user_id = c.lastrowid
    conn.commit()
    conn.close()
    return user_id

def insert_rating(user_id, movie_name, rating):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO ratings (user_id, movie_name, rating) VALUES (?, ?, ?)', (user_id, movie_name, rating))
    conn.commit()
    conn.close()

def submit_survey(username, movie_ratings):
    user_id = insert_user(username)
    for movie_name, rating in movie_ratings.items():
        insert_rating(user_id, movie_name, rating)

if __name__ == "__main__":
    init_db()