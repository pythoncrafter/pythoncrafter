import sqlite3

# Function to view and edit entries
def view_edit_entries():
    conn = sqlite3.connect('research_data.db')
    c = conn.cursor()

    print("1. View all players")
    print("2. View all coaches")
    print("3. Edit a player's age")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nViewing all players:")
        c.execute("SELECT * FROM Players")
        players = c.fetchall()
        for player in players:
            print(player)
    elif choice == "2":
        print("\nViewing all coaches:")
        c.execute("SELECT * FROM Coaches")
        coaches = c.fetchall()
        for coach in coaches:
            print(coach)
    elif choice == "3":
        player_id = input("Enter the PlayerID of the player you want to edit: ")
        new_age = input("Enter the new age for the player: ")
        c.execute("UPDATE Players SET Age = ? WHERE PlayerID = ?", (new_age, player_id))
        print("\nPlayer's age updated.")
    else:
        print("Invalid choice.")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Call the function to view and edit entries
    view_edit_entries)
