import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/Users/aditinarayan/Downloads/Finance/data/finance.db')
c = conn.cursor()

# Create transactions table
c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                type TEXT,
                amount REAL,
                date TEXT
            )''')

# Create goals table
c.execute('''CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                goal TEXT,
                target_amount REAL,
                saved_amount REAL DEFAULT 0
            )''')

# Create investments table
c.execute('''CREATE TABLE IF NOT EXISTS investments (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                type TEXT,
                amount_invested REAL,
                date TEXT
            )''')

# Create retirement table
c.execute('''CREATE TABLE IF NOT EXISTS retirement (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                goal TEXT,
                target_amount REAL,
                current_savings REAL,
                retirement_age INTEGER
            )''')

# Insert example values into transactions table
transactions_values = [
    (1, 'Income', 500.00, '2024-05-19'),
    (1, 'Expense', 50.00, '2024-05-18'),
    (1, 'Expense', 30.00, '2024-05-17'),
    (1, 'Income', 600.00, '2024-05-16'),
    (1, 'Expense', 20.00, '2024-05-15'),
    (1, 'Income', 700.00, '2024-05-14'),
    (1, 'Expense', 100.00, '2024-05-13'),
    (1, 'Income', 800.00, '2024-05-12'),
    (1, 'Expense', 70.00, '2024-05-11'),
    (1, 'Income', 900.00, '2024-05-10')
]
c.executemany('''INSERT INTO transactions (user_id, type, amount, date) VALUES (?, ?, ?, ?)''', transactions_values)

# Insert example values into goals table
goals_values = [
    (1, 'Buy a new car', 20000.00, 0),
    (1, 'Save for vacation', 5000.00, 0),
    (1, 'Emergency fund', 10000.00, 0),
    (1, 'Home renovation', 30000.00, 0),
    (1, 'Invest in stocks', 15000.00, 0),
    (1, 'Save for education', 25000.00, 0),
    (1, 'Retirement savings', 100000.00, 0),
    (1, 'Pay off debt', 5000.00, 0),
    (1, 'Start a business', 20000.00, 0),
    (1, 'Donate to charity', 1000.00, 0)
]
c.executemany('''INSERT INTO goals (user_id, goal, target_amount, saved_amount) VALUES (?, ?, ?, ?)''', goals_values)

# Insert example values into investments table
investments_values = [
    (1, 'Stocks', 1000.00, '2024-05-19'),
    (1, 'Bonds', 2000.00, '2024-05-18'),
    (1, 'Mutual Funds', 3000.00, '2024-05-17'),
    (1, 'Real Estate', 4000.00, '2024-05-16'),
    (1, 'Other', 5000.00, '2024-05-15'),
    (1, 'Stocks', 6000.00, '2024-05-14'),
    (1, 'Bonds', 7000.00, '2024-05-13'),
    (1, 'Mutual Funds', 8000.00, '2024-05-12'),
    (1, 'Real Estate', 9000.00, '2024-05-11'),
    (1, 'Other', 10000.00, '2024-05-10')
]
c.executemany('''INSERT INTO investments (user_id, type, amount_invested, date) VALUES (?, ?, ?, ?)''', investments_values)

# Insert example values into retirement table
retirement_values = [
    (1, 'Retire comfortably', 500000.00, 100000.00, 65),
    (1, 'Travel during retirement', 20000.00, 5000.00, 60),
    (1, 'Buy retirement home', 300000.00, 50000.00, 65),
    (1, 'Start a hobby business', 10000.00, 2000.00, 70),
    (1, 'Support grandchildren', 5000.00, 1000.00, 70),
    (1, 'Cover healthcare costs', 100000.00, 20000.00, 65),
    (1, 'Leave inheritance', 50000.00, 10000.00, 70),
    (1, 'Travel the world', 100000.00, 20000.00, 60),
    (1, 'Invest in retirement account', 50000.00, 10000.00, 65),
    (1, 'Live debt-free in retirement', 20000.00, 5000.00, 65)
]
c.executemany('''INSERT INTO retirement (user_id, goal, target_amount, current_savings, retirement_age) VALUES (?, ?, ?, ?, ?)''', retirement_values)

# Commit changes and close connection
conn.commit()
conn.close()
