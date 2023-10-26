import sqlite3
from kivy.app import App
from kivy.uix.label import Label


class ResearchDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS Players (
                         PlayerID INTEGER PRIMARY KEY,
                         PlayerName TEXT,
                         Age INTEGER,
                         Nationality TEXT,
                         Sport TEXT,
                         TeamID INTEGER,
                         TeamName TEXT
                         )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS TrainingActivities (
                         ActivityID INTEGER PRIMARY KEY,
                         Sport TEXT,
                         Description TEXT
                         )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS DecisionMaking (
                         DecisionID INTEGER PRIMARY KEY,
                         PlayerID INTEGER,
                         ActivityID INTEGER,
                         Sport TEXT,
                         Question TEXT,
                         Response TEXT,
                         FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
                         FOREIGN KEY (ActivityID) REFERENCES TrainingActivities(ActivityID)
                         )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS PlayerTraining (
                         PlayerID INTEGER,
                         ActivityID INTEGER,
                         FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
                         FOREIGN KEY (ActivityID) REFERENCES TrainingActivities(ActivityID)
                         )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS Coaches (
                         CoachID INTEGER PRIMARY KEY,
                         CoachName TEXT,
                         Experience TEXT,
                         TeamID INTEGER,
                         TeamName TEXT
                         )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS Trainers (
                         TrainerID INTEGER PRIMARY KEY,
                         TrainerName TEXT,
                         Specialization TEXT,
                         TeamID INTEGER,
                         TeamName TEXT
                         )''')

    def close_connection(self):
        self.conn.close()

    def insert_data(self, query, data_tuple):
        try:
            self.c.execute(query, data_tuple)
            self.conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")

    def execute_query(self, query):
        try:
            self.c.execute(query)
            result = self.c.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


class User(ResearchDatabase):
    def create_player_entry(self, player_data):
        query = "INSERT INTO Players (PlayerName, Age, Nationality, Sport, TeamID, TeamName) VALUES (?, ?, ?, ?, ?, ?)"
        self.insert_data(query, player_data)
        print("Player entry created successfully.")

    def answer_question(self, response_data):
        query = "INSERT INTO DecisionMaking (PlayerID, ActivityID, Sport, Question, Response) VALUES (?, ?, ?, ?, ?)"
        self.insert_data(query, response_data)
        print("Response recorded successfully.")


class Admin(ResearchDatabase):
    def create_training_activity(self, activity_data):
        query = "INSERT INTO TrainingActivities (Sport, Description) VALUES (?, ?)"
        self.insert_data(query, activity_data)
        print("Training activity description created successfully.")

    def create_question(self, question_data):
        query = "INSERT INTO DecisionMaking (ActivityID, Sport, Question) VALUES (?, ?, ?)"
        self.insert_data(query, question_data)
        print("Question added successfully.")


class Coach(ResearchDatabase):
    def create_coach_entry(self, coach_data):
        query = "INSERT INTO Coaches (CoachName, Experience, TeamID, TeamName) VALUES (?, ?, ?, ?)"
        self.insert_data(query, coach_data)
        print("Coach entry created successfully.")


class Trainer(ResearchDatabase):
    def create_trainer_entry(self, trainer_data):
        query = "INSERT INTO Trainers (TrainerName, Specialization, TeamID, TeamName) VALUES (?, ?, ?, ?)"
        self.insert_data(query, trainer_data)
        print("Trainer entry created successfully.")


class ResearchApp(App):
    def build(self):
        return Label(text='Welcome to ResearchApp')


if __name__ == '__main__':
    research_db = ResearchDatabase('research_data.db')
    user = User('research_data.db')
    admin = Admin('research_data.db')
    coach = Coach('research_data.db')
    trainer = Trainer('research_data.db')
    ResearchApp().run()
