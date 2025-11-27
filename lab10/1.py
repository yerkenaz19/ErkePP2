import psycopg2
import csv
con = psycopg2.connect(
    dbname='phonebook',
    user='erkenaz',
    password='12345',
    host='localhost',
    port='5432'
)
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS phone_book(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256),
    phone VARCHAR(256)
);
''')
con.commit()
def insert(name, phone):
    cur.execute('INSERT INTO phone_book(name, phone) VALUES (%s, %s)', (name, phone))
    con.commit()

def update(id, name, phone):
    cur.execute('UPDATE phone_book SET name=%s, phone=%s WHERE id=%s', (name, phone, id))
    con.commit()

def getById(id):
    cur.execute('SELECT * FROM phone_book WHERE id=%s', (id,))
    return cur.fetchone()

def getAll(asc=True):
    order = 'ASC' if asc else 'DESC'
    cur.execute(f'SELECT * FROM phone_book ORDER BY name {order}')
    return cur.fetchall()

def getByName(name):
    cur.execute('SELECT * FROM phone_book WHERE name=%s', (name,))
    return cur.fetchall()

def delete(value):
    cur.execute('DELETE FROM phone_book WHERE name=%s OR phone=%s', (value, value))
    con.commit()
def insertFromConsole():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    insert(name, phone)
    print('New phone added!')

def insertFromCSV(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    print(f"Skipping invalid row: {row}")
                    continue
                name, phone = row
                insert(name.strip(), phone.strip())
        print("Data from CSV imported successfully!")
    except FileNotFoundError:
        print("CSV file not found. Check the path!")

def updateFromConsole():
    id = input("Enter id to update: ")
    row = getById(id)
    if row is None:
        print("No such ID.")
        return
    name = input("Enter new name (leave blank to keep old): ")
    if name == "":
        name = row[1]
    phone = input("Enter new phone (leave blank to keep old): ")
    if phone == "":
        phone = row[2]
    update(id, name, phone)
    print("Updated successfully!")

def printPhoneBook():
    direction = input("Sort (1-ASC, 2-DESC): ")
    asc = False if direction == "2" else True
    rows = getAll(asc)
    for r in rows:
        print(f"ID: {r[0]}, Name: {r[1]}, Phone: {r[2]}")

def searchByName():
    name = input("Enter name to search: ")
    result = getByName(name)
    if result:
        for r in result:
            print(f"ID: {r[0]}, Name: {r[1]}, Phone: {r[2]}")
    else:
        print("Not found")

def deleteByName():
    value = input("Enter name or phone to delete: ")
    delete(value)
    print("Deleted!")
def safe_menu_choice():
    while True:
        try:
            choice = int(input(
                "\n------ PHONEBOOK MENU ------\n"
                " 1 - Insert by console\n"
                " 2 - Insert from CSV\n"
                " 3 - Update from console\n"
                " 4 - Search by name\n"
                " 5 - Delete by name or phone\n"
                " 6 - Sort and show phone book\n"
                " 0 - Exit\n"
                "Choose option: "
            ))
            if choice in range(0, 7):
                return choice
            else:
                print("Enter number from 0 to 6!")
        except ValueError:
            print("Invalid input! Enter a NUMBER.")
while True:
    user_input = safe_menu_choice()

    if user_input == 1:
        insertFromConsole()
    elif user_input == 2:
        file_path = input("Enter CSV file path: ")
        insertFromCSV(file_path)
    elif user_input == 3:
        updateFromConsole()
    elif user_input == 4:
        searchByName()
    elif user_input == 5:
        deleteByName()
    elif user_input == 6:
        printPhoneBook()
    elif user_input == 0:
        print("Goodbye!")
        break
con.close()
