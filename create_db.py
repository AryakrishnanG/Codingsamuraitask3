import sqlite3

# Database Connection
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

# Create the Expenses table if it doesn't exist
cur.execute("""CREATE TABLE IF NOT EXISTS Expenses (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Date DATE,
                Description TEXT,
                Category TEXT,
                Price REAL
            )""")
conn.commit()
conn.close()

print("Expenses table created successfully.")
