# main.py

from create_database import create_tables
from read_database import read_data
from write_database import write_data
from edit_view_entries import edit_entries

def main():
    create_tables()
    print("Tables created.") 

    write_data()
    print("Data written to the database.")

    read_data()
    print("Data read from the database.")

    edit_entries()
    print("Entries edited and viewed from the database.")

if __name__ == '__main__':
    main()
