import sqlite3

conn = sqlite3.connect('research_data.db')
c = conn.cursor()

# Create the necessary tables
c.execute('''CREATE TABLE IF NOT EXISTS Players (
                     PlayerID INTEGER PRIMARY KEY,
                     PlayerName TEXT,
                     Age INTEGER,
                     Nationality TEXT,
                     Sport TEXT,
                     TeamID INTEGER,
                     TeamName TEXT
                     )''')

c.execute('''CREATE TABLE IF NOT EXISTS TrainingActivities (
                     ActivityID INTEGER PRIMARY KEY,
                     Sport TEXT,
                     Description TEXT
                     )''')

c.execute('''CREATE TABLE IF NOT EXISTS DecisionMaking (
                     DecisionID INTEGER PRIMARY KEY,
                     PlayerID INTEGER,
                     ActivityID INTEGER,
                     Sport TEXT,
                     Question TEXT,
                     Response TEXT,
                     FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
                     FOREIGN KEY (ActivityID) REFERENCES TrainingActivities(ActivityID)
                     )''')

c.execute('''CREATE TABLE IF NOT EXISTS PlayerTraining (
                     PlayerID INTEGER,
                     ActivityID INTEGER,
                     FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
                     FOREIGN KEY (ActivityID) REFERENCES TrainingActivities(ActivityID)
                     )''')

c.execute('''CREATE TABLE IF NOT EXISTS Coaches (
                     CoachID INTEGER PRIMARY KEY,
                     CoachName TEXT,
                     Experience TEXT,
                     TeamID INTEGER,
                     TeamName TEXT
                     )''')

c.execute('''CREATE TABLE IF NOT EXISTS Trainers (
                     TrainerID INTEGER PRIMARY KEY,
                     TrainerName TEXT,
                     Specialization TEXT,
                     TeamID INTEGER,
                     TeamName TEXT
                     )''')

conn.commit()
conn.close()

