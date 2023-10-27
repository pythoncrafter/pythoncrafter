import random

# Function to generate random player data
def generate_random_player_data():
    player_data = {
        "PlayerName": f"Player{random.randint(1, 100)}",
        "Age": random.randint(18, 40),
        "Nationality": f"Country{random.randint(1, 10)}",
        "Sport": random.choice(["Soccer", "Basketball", "Tennis", "Golf", "Cricket"]),
        "TeamID": random.randint(1, 20),
        "TeamName": f"Team{random.randint(1, 10)}"
    }
    return player_data

# Generate and print 5 random player data entries
for _ in range(5):
    data = generate_random_player_data()
    print(data)
 
