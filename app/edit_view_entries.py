import sqlite3

conn = sqlite3.connect('research_data.db')
c = conn.cursor()

# Example of editing data in the Players table
c.execute("UPDATE Players SET PlayerName = ? WHERE PlayerID = ?", ('Jane Doe', 1))

# Example of viewing an entry in the Players table
c.execute("SELECT * FROM Players WHERE PlayerID = ?", (1,))
row = c.fetchone()
print(row)

conn.commit()
conn.close()
