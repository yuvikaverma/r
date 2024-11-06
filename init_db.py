import sqlite3

# Connect to the database (will create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table for books (id, title, author, status)
cur.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
