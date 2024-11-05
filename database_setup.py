import sqlite3

# Connect to database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create contacts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')

# Commit and close connection
conn.commit()
conn.close()
