import sqlite3
from tabulate import tabulate

def read_data():
    conn = sqlite3.connect('research_data.db')
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

    conn.close()

if __name__ == '__main__':
    # Call the function to read data
    read_data()
