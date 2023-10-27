import sqlite3

# Function to edit and view entries
def edit_view_entries():
    conn = sqlite3.connect('research_data.db')
    c = conn.cursor()

    print("Viewing all players:")
    c.execute("SELECT * FROM Players")
    players = c.fetchall()
    for player in players:
        print(player)

    print("\nViewing all coaches:")
    c.execute("SELECT * FROM Coaches")
    coaches = c.fetchall()
    for coach in coaches:
        print(coach)

    print("\nEditing a player's age:")
    c.execute("UPDATE Players SET Age = 25 WHERE PlayerID = 1")

    print("\nViewing all players after edit:")
    c.execute("SELECT * FROM Players")
    players = c.fetchall()
    for player in players:
        print(player)

    conn.commit()
    conn.close()

# Call the function to edit and view entries
edit_view_entries()
