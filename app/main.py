# main.py

from create_database import create_tables
from read_database import read_data
from write_database import generate_random_player_data
from edit_view_entries import edit_view_entries

def main():
    create_tables()

    generate_random_player_data()
    
'''
    read_data()
    print("Data read from the database.")

    edit_view_entries()
    print("Entries edited and viewed from the database.")
'''

if __name__ == '__main__':
    main()
