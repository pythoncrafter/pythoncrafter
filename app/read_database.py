import os
import sqlite3
from tabulate import tabulate
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def read_data():
    root = Tk()
    root.withdraw()  # Hide the main window

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    # Prompt the user to select a file within the data folder
    db_path = askopenfilename(initialdir=data_dir, title="Select Database file", filetypes=[("SQLite Database files", "*.db")])

    if not db_path:
        print("No file selected. Exiting...")
        return

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('SELECT * FROM Players')
        players = c.fetchall()
        print(tabulate(players, headers=[i[0] for i in c.description]))

        c.execute('SELECT * FROM TrainingActivities')
        activities = c.fetchall()
        print(tabulate(activities, headers=[i[0] for i in c.description]))

        c.execute('SELECT * FROM DecisionMaking')
        decision_making = c.fetchall()
        print(tabulate(decision_making, headers=[i[0] for i in c.description]))

        c.execute('SELECT * FROM Coaches')
        coaches = c.fetchall()
        print(tabulate(coaches, headers=[i[0] for i in c.description]))

        c.execute('SELECT * FROM Trainers')
        trainers = c.fetchall()
        print(tabulate(trainers, headers=[i[0] for i in c.description]))

    except sqlite3.OperationalError as e:
        print(f"Error: {e}")

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    read_data()
