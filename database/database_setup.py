import sqlite3

# Step 1: Connect to SQLite database (creates STORAGE.db if it doesn't exist)
connection = sqlite3.connect("STORAGE.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Define the SQL command to create the 'books' table
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
title TEXT,
author TEXT,
year INTEGER
);
"""

# Step 4: Execute the SQL command
cursor.execute(create_table_query)

# Step 5: Commit changes and close the connection
connection.commit()
connection.close()

print("Database and table created successfully.")
