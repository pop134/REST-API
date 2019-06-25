import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


user_query = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(user_query)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, 'tri', 'pop'),
    (2, 'tri1', 'pop')
]
cursor.executemany(insert_query, users)


item_query = 'CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text, price float)'
cursor.execute(item_query)

connection.commit()
connection.close()