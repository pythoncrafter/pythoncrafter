import sqlite3

conn = sqlite3.connect('research_data.db')
c = conn.cursor()

# Example of reading and displaying data from the Players table
c.execute("SELECT * FROM Players")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()
