import sqlite3

# Function to simulate user authentication
def authenticate(username, password):
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash(password)))
    user = c.fetchone()
    conn.close()
    return user

# Function to insert user registration data into the database
def register_user(username, email, password, full_name, age, country):
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Hash the password (you should use a proper password hashing function)
    hashed_password = hash(password)

    # Insert user data into the database
    c.execute("INSERT INTO users (username, email, password, full_name, age, country) VALUES (?, ?, ?, ?, ?, ?)",
              (username, email, hashed_password, full_name, age, country))

    conn.commit()
    conn.close()
