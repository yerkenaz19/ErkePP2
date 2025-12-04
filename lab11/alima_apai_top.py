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
cur.execute(r'''
CREATE TABLE IF NOT EXISTS phone_book(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256),
    phone VARCHAR(256)
);
''')
cur.execute('DROP FUNCTION IF EXISTS search_by_pattern(VARCHAR);')
cur.execute('DROP FUNCTION IF EXISTS get_phones_with_pagination(INTEGER, INTEGER);')
cur.execute('DROP PROCEDURE IF EXISTS insert_or_update_phone(VARCHAR, VARCHAR);')
cur.execute('DROP PROCEDURE IF EXISTS insert_many_users(VARCHAR[], VARCHAR[]);')
cur.execute('DROP PROCEDURE IF EXISTS delete_by_name_or_phone(VARCHAR);')
cur.execute(r'''
CREATE OR REPLACE FUNCTION search_by_pattern(pattern VARCHAR)
RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.phone
    FROM phone_book pb
    WHERE pb.name ILIKE '%' || pattern || '%'
       OR pb.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
''')
cur.execute(r'''
CREATE OR REPLACE PROCEDURE insert_or_update_phone(username VARCHAR, userphone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phone_book WHERE name = username) THEN
        UPDATE phone_book
        SET phone = userphone
        WHERE name = username;
    ELSE
        INSERT INTO phone_book(name, phone)
        VALUES (username, userphone);
    END IF;
END;
$$ LANGUAGE plpgsql;
''')
cur.execute(r'''
CREATE OR REPLACE PROCEDURE insert_many_users(usernames VARCHAR[], userphones VARCHAR[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER := 1;
    incorrect_data TEXT := '';
BEGIN
    WHILE i <= array_length(usernames, 1) LOOP
        IF userphones[i] ~ E'^\\d{5,15}$' THEN
            CALL insert_or_update_phone(usernames[i], userphones[i]);
        ELSE
            incorrect_data := incorrect_data || usernames[i] || ':' || userphones[i] || ', ';
        END IF;
        i := i + 1;
    END LOOP;

    IF incorrect_data <> '' THEN
        RAISE NOTICE 'Incorrect data: %', incorrect_data;
    END IF;
END;
$$;
''')
cur.execute(r'''
CREATE OR REPLACE FUNCTION get_phones_with_pagination(lim INTEGER, off INTEGER)
RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phone_book ORDER BY id LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
''')
cur.execute(r'''
CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(value VARCHAR)
AS $$
BEGIN
    DELETE FROM phone_book
    WHERE name = value OR phone = value;
END;
$$ LANGUAGE plpgsql;
''')
con.commit()
def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute('CALL insert_or_update_phone(%s, %s)', (name, phone))
    con.commit()
    print("User inserted/updated!")

def insert_many_users():
    n = int(input("How many users to insert? "))
    usernames = []
    userphones = []
    for i in range(n):
        name = input(f"Enter name #{i+1}: ")
        phone = input(f"Enter phone #{i+1}: ")
        usernames.append(name)
        userphones.append(phone)
    cur.execute('CALL insert_many_users(%s, %s)', (usernames, userphones))
    con.commit()
    print("Users processed! Check console for any incorrect data notices.")

def insert_from_csv():
    with open('phones.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        users = [(row[0], row[1]) for row in reader]
    for user in users:
        cur.execute('CALL insert_or_update_phone(%s, %s)', (user[0], user[1]))
    con.commit()
    print("Users from CSV inserted!")

def search():
    pattern = input("Enter search pattern: ")
    cur.execute('SELECT * FROM search_by_pattern(%s)', (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')

def get_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute('SELECT * FROM get_phones_with_pagination(%s, %s)', (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')

def delete_user():
    value = input("Enter name or phone to delete: ")
    cur.execute('CALL delete_by_name_or_phone(%s)', (value,))
    con.commit()
    print("Deleted if exists!")

def print_all():
    cur.execute('SELECT * FROM phone_book ORDER BY id')
    rows = cur.fetchall()
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')

while True:
    choice = input("""
Choose option:
1 - Insert or update user
2 - Insert many users 
3 - Insert users from CSV
4 - Search by pattern
5 - Paginated output
6 - Delete by name or phone
7 - Print all users
0 - Exit
> """)
    if choice == '1':
        insert_or_update()
    elif choice == '2':
        insert_many_users()
    elif choice == '3':
        insert_from_csv()
    elif choice == '4':
        search()
    elif choice == '5':
        get_paginated()
    elif choice == '6':
        delete_user()
    elif choice == '7':
        print_all()
    elif choice == '0':
        break
    else:
        print("Invalid option")

cur.close()
con.close()
