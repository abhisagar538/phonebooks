import sqlite3
from datetime import datetime

# Generate a unique table name based on the current timestamp
def generate_table_name():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'contacts_{timestamp}'

# Create a SQLite database and a new table to store contacts
def create_table():
    table_name = generate_table_name()
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            cell_number TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
    return table_name

# Add a new contact to the specified table
def add_contact(table_name, id, name, cell_number, email):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute(f'''
        INSERT OR REPLACE INTO {table_name} (id, name, cell_number, email)
        VALUES (?, ?, ?, ?)
    ''', (id, name, cell_number, email))
    connection.commit()
    connection.close()

# Insert 5 sample rows of data into a new table
def insert_sample_data(table_name):
    sample_data = [
        ('1', 'sagar', '123-456-7890', 'sagar@example.com'),
        ('2', 'navya', '987-654-3210', 'nav@example.com'),
        ('3', 'pooja ', '555-123-4567', 'poo@example.com'),
        ('4', 'keerthan', '999-888-7777', 'keerthi@example.com'),
        ('5', 'raj ', '444-555-6666', 'raj@example.com')
    ]

    for data in sample_data:
        add_contact(table_name, *data)

# Display all contacts in the specified table
def display_contacts(table_name):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    contacts = cursor.fetchall()
    connection.close()

    if contacts:
        print("\nContacts:")
        print("{:<5} {:<20} {:<15} {:<30}".format("\u001b[4mID\u001b[0m", "\u001b[4mName\u001b[0m", "\u001b[4mCell Number\u001b[0m", "\u001b[4mEmail\u001b[0m"))
        print("-" * 75)
        for contact in contacts:
            print("{:<5} {:<20} {:<15} {:<30}".format(contact[0], contact[1], contact[2], contact[3]))
    else:
        print("No contacts found.")

# Main function to interact with the contact book
def main():
    table_name = create_table()
    insert_sample_data(table_name)

    while True:
        print("\nPhone Contact Book")
        print("1. Display Contacts")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            display_contacts(table_name)

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()