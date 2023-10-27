import sqlite3
import random
from faker import Faker
import pycountry

fake = Faker()
generated_data = []

# Function to generate random player data
def generate_random_player_data():
    countries = list(pycountry.countries)
    teams = ["Lions", "Tigers", "Bears", "Eagles", "Sharks", "Wolves", "Falcons", "Dragons", "Panthers", "Cobras"]
    player_data = {
        "PlayerName": fake.name(),
        "Age": random.randint(18, 40),
        "Nationality": random.choice(countries).name,
        "Sport": random.choice(["Soccer", "Basketball", "Tennis", "Golf", "Cricket"]),
        "TeamID": random.randint(1, 20),
        "TeamName": f"{random.choice(teams)}"
    }
    generated_data.append(player_data)
    return player_data

# Connect to the database
conn = sqlite3.connect('research_data.db')
c = conn.cursor()

# Generate and insert 5 random player data entries
for _ in range(5):
    data = generate_random_player_data()
    c.execute('''INSERT INTO Players (PlayerName, Age, Nationality, Sport, TeamID, TeamName) 
                 VALUES (?, ?, ?, ?, ?, ?)''', 
              (data["PlayerName"], data["Age"], data["Nationality"], data["Sport"], data["TeamID"], data["TeamName"]))

conn.commit()
conn.close()

# Print all the generated data
print(generated_data)
