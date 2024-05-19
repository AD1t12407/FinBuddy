import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            email TEXT,
            password TEXT,
            full_name TEXT,
            age INTEGER,
            country TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, email, password, full_name, age, country):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (username, email, password, full_name, age, country) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, email, password, full_name, age, country))
    conn.commit()
    conn.close()

# Function to check if a username exists
def user_exists(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user

# Function to validate login credentials
def validate_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user
