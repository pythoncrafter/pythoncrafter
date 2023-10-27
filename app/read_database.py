import sqlite3

def read_data():
    conn = sqlite3.connect('research_data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Players')
    print(c.fetchall())

    c.execute('SELECT * FROM TrainingActivities')
    print(c.fetchall())

    c.execute('SELECT * FROM DecisionMaking')
    print(c.fetchall())

    c.execute('SELECT * FROM Coaches')
    print(c.fetchall())

    c.execute('SELECT * FROM Trainers')
    print(c.fetchall())

    conn.close()

if __name__ == '__main__':
    # Call the function to read data
    read_data()
