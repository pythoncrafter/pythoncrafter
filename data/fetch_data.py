import os
import sqlite3
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
import random
import string

def select_database_file():
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a file starting from the current directory
    file_path = filedialog.askopenfilename(initialdir=current_directory)

    return file_path

def get_table_names(file_path):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    connection.close()

    return [table[0] for table in tables]

def view_table_structure(file_path, table_name):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")
    structure = cursor.fetchall()

    connection.close()

    formatted_structure = [(col[1], col[2]) for col in structure]

    return formatted_structure

def view_table_entries(file_path, table_name):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    entries = cursor.fetchall()

    if entries:
        headers = [i[0] for i in cursor.description]
        print(tabulate(entries, headers=headers))
    else:
        print(f"No entries found for {table_name}.")

    connection.close()


def generate_random_data(data_type):
    if data_type == 'INTEGER':
        return random.randint(0, 100)
    elif data_type == 'REAL':
        return round(random.uniform(0, 100), 2)
    elif data_type == 'TEXT':
        return ''.join(random.choices(string.ascii_letters, k=10))
    elif data_type == 'BOOLEAN':
        return random.choice([True, False])
    else:
        return None

def generate_random_coach_id(cursor):
    while True:
        coach_id = random.randint(1000, 9999)  # Example range for the CoachID
        cursor.execute(f"SELECT * FROM Coaches WHERE CoachID = ?", (coach_id,))
        if not cursor.fetchone():
            return coach_id

def add_entry_to_table(file_path, table_name, values, is_random=False, quantity=1):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    if is_random:
        for _ in range(quantity):
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_info = cursor.fetchall()
            new_values = []

            for column in columns_info:
                if column[1] == "CoachID":
                    new_values.append(generate_random_coach_id(cursor))
                else:
                    new_values.append(generate_random_data(column[2]))

            values = new_values

            columns = ', '.join(['?' for _ in values])
            columns_names = ', '.join([col[1] for col in columns_info])

            cursor.execute(f"INSERT INTO {table_name}({columns_names}) VALUES ({columns})", values)

    else:
        columns = ', '.join(['?' for _ in values])
        columns_names = ', '.join([col[1] for col in cursor.execute(f"PRAGMA table_info({table_name})")])

        cursor.execute(f"INSERT INTO {table_name}({columns_names}) VALUES ({columns})", values)

    connection.commit()

    if is_random:
        print("Random entries added successfully.")
    else:
        print("Entry added successfully.")

    connection.close()

# Main program
file_path = select_database_file()
if file_path:
    while True:
        print("1. View table structure")
        print("2. View table entries")
        print("3. Add entry to table")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # View table structure logic
            pass
        elif choice == '2':
            table_names = get_table_names(file_path)
            print("Select a table to view its entries:")
            for index, name in enumerate(table_names, start=1):
                print(f"{index}. {name}")
            print("0. Back")

            while True:
                try:
                    table_choice = int(input("Enter the number of the table: "))
                    if 0 <= table_choice <= len(table_names):
                        if table_choice == 0:
                            break
                        chosen_table = table_names[table_choice - 1]
                        view_table_entries(file_path, chosen_table)
                        break
                    else:
                        print("Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '3':

            table_names = get_table_names(file_path)
            print("Select a table to add an entry:")
            for index, name in enumerate(table_names, start=1):
                print(f"{index}. {name}")
            print("0. Back")

            while True:
                try:
                    table_choice = int(input("Enter the number of the table: "))
                    if 0 <= table_choice <= len(table_names):
                        if table_choice == 0:
                            break
                        chosen_table = table_names[table_choice - 1]
                        is_random = input("Do you want to add a random data entry? (yes or no): ").lower()
                        if is_random == 'yes':
                            quantity = int(input("Enter the quantity of random entries to add: "))
                            add_entry_to_table(file_path, chosen_table, [], is_random=True, quantity=quantity)
                        else:
                            entry_values = []
                            structure = view_table_structure(file_path, chosen_table)
                            for col in structure:
                                value = input(f"Enter the value for {col[0]} ({col[1]}): ")
                                entry_values.append(value)
                            add_entry_to_table(file_path, chosen_table, entry_values)
                        break
                    else:
                        print("Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")