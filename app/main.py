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
    db_name = 'research_data.db'
    def __init__(self, db_name):
        
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()
        self.validate_database()

    @staticmethod
    def get_data_folder_path(file_path):
        current_directory = os.path.dirname(os.path.abspath(file_path))
        project_directory = os.path.dirname(current_directory)
        return os.path.join(project_directory, 'data', 'research_data.db')

    def validate_database(self):
        if not os.path.isfile(self.db_name):
            print("Database file not found. Creating a new database.")
            self.conn = sqlite3.connect(self.db_name)
            self.c = self.conn.cursor()
            self.create_tables()
            print("Database created successfully.")
        else:
            print("Database exists.")
            
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
        player_name_input = TextInput(hint_text='Player Name')
        player_age_input = TextInput(hint_text='Player Age')
        nationality_input = TextInput(hint_text='Nationality')
        sport_input = TextInput(hint_text='Sport')
        team_id_input = TextInput(hint_text='Team ID')
        team_name_input = TextInput(hint_text='Team Name')

        # Button for adding player information
        add_player_button = Button(text='Add Player', on_press=self.add_player)

        layout.add_widget(Label(text='Add Player Information:'))
        layout.add_widget(player_name_input)
        layout.add_widget(player_age_input)
        layout.add_widget(nationality_input)
        layout.add_widget(sport_input)
        layout.add_widget(team_id_input)
        layout.add_widget(team_name_input)
        layout.add_widget(add_player_button)

        # Create an instance of the ResearchDatabase class
        data_folder_path = ResearchDatabase.get_data_folder_path(__file__)
        research_db = ResearchDatabase(data_folder_path)
        user = User(data_folder_path)
        admin = Admin(data_folder_path)
        coach = Coach(data_folder_path)
        trainer = Trainer(data_folder_path)

        self.research_db = research_db
        self.user = user
        self.admin = admin
        self.coach = coach
        self.trainer = trainer

        return layout

    def add_player(self, instance):
        # Get the player information from the input fields
        player_data = (
            player_name_input.text,
            player_age_input.text,
            nationality_input.text,
            sport_input.text,
            team_id_input.text,
            team_name_input.text
        )
        self.user.create_player_entry(player_data)

    def add_coach(self, instance):
        # Get the coach information from the input fields
        coach_data = (
            coach_name_input.text,
            coach_experience_input.text,
            coach_team_id_input.text,
            coach_team_name_input.text
        )
        coach.create_coach_entry(coach_data)

    def add_trainer(self, instance):
        # Get the trainer information from the input fields
        trainer_data = (
            trainer_name_input.text,
            trainer_specialization_input.text,
            trainer_team_id_input.text,
            trainer_team_name_input.text
        )
        trainer.create_trainer_entry(trainer_data)

    def add_admin(self, instance):
        # Get the admin information from the input fields
        admin_data = (
            admin_name_input.text,
            admin_experience_input.text,
            admin_team_id_input.text,
            admin_team_name_input.text
        )
        admin.create_admin_entry(admin_data)

    def on_stop(self):
        self.research_db.close_connection()

if __name__ == '__main__':
    data_folder_path = ResearchDatabase.get_data_folder_path(__file__)
    research_db = ResearchDatabase(data_folder_path)
    user = User(data_folder_path)
    admin = Admin(data_folder_path)
    coach = Coach(data_folder_path)
    trainer = Trainer(data_folder_path)
    
    research_db_instance = ResearchDatabase(data_folder_path)
    research_db_instance.validate_database()
    
    # Run the Kivy app
    app = ResearchApp()
    app.run()
    
    research_db.close_connection()

