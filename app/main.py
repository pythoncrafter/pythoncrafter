import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os 

class ResearchDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()

    @staticmethod
    def get_data_folder_path(file_path):
        current_directory = os.path.dirname(os.path.abspath(file_path))
        project_directory = os.path.dirname(current_directory)
        return os.path.join(project_directory, 'data', 'research_data.db')
    
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
        layout = BoxLayout(orientation='vertical')

        # Text input fields for user and admin
        user_input = TextInput(text='User input')
        admin_input = TextInput(text='Admin input')
        coach_input = TextInput(text='Coach input')
        trainer_input = TextInput(text='Trainer input')

        # Buttons for user and admin interactions
        user_button = Button(text='Submit User Input')
        admin_button = Button(text='Submit Admin Input')
        coach_button = Button(text='Submit Coach Input')
        trainer_button = Button(text='Submit Trainer Input')

        layout.add_widget(Label(text='User Input:'))
        layout.add_widget(user_input)
        layout.add_widget(user_button)

        layout.add_widget(Label(text='Admin Input:'))
        layout.add_widget(admin_input)
        layout.add_widget(admin_button)

        layout.add_widget(Label(text='Coach Input:'))
        layout.add_widget(coach_input)
        layout.add_widget(coach_button)

        layout.add_widget(Label(text='Trainer Input:'))
        layout.add_widget(trainer_input)
        layout.add_widget(trainer_button)

        return layout


if __name__ == '__main__':
    data_folder_path = ResearchDatabase.get_data_folder_path(__file__)
    research_db = ResearchDatabase(data_folder_path)
    user = User(data_folder_path)
    admin = Admin(data_folder_path)
    coach = Coach(data_folder_path)
    trainer = Trainer(data_folder_path)
    
    # Run the Kivy app
    ResearchApp().run()
    
    research_db.close_connection()

