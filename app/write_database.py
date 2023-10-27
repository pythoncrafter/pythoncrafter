import sqlite3

conn = sqlite3.connect('research_data.db')
c = conn.cursor()

# Example of writing data to the Players table
c.execute("INSERT INTO Players (PlayerName, Age, Nationality, Sport, TeamID, TeamName) VALUES (?, ?, ?, ?, ?, ?)", 
          ('John Doe', 25, 'USA', 'Basketball', 1, 'Team A'))

conn.commit()
conn.close()
