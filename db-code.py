import sqlite3

# connection to DB
con=sqlite3.connect("contacts.db")

# DB Cursor to execute Queries and Fetch results
cur=con.cursor()

# Cursor to execute commands
# cur.execute("CREATE TABLR move(title, year, score)")

# Passing a string into cur.execute line is better

