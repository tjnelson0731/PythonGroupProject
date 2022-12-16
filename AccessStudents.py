# title: Access Student Database
# Authors: Taylor Nelson, Kadin Meyers, Benjamin Eerkes

import sqlite3


# Function to update a student
def update_student(cursor):
    id = input('What is the ID of the student record you want to update? ')
    value = input('What value of the record do you want to update? ')
    update = input('What do you want to update it too? ')
    cursor.execute('UPDATE database SET ' + value + ' = ? WHERE Student_id = ?', (update, id))
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    print('Student I.D.   First_Name   Last_Name   Class_Name              Address              Phone_Number       '
          '  Email')
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:22}{row[4]:23}{row[5]:16}{row[6]:25}')


# Function to delete a student
def delete_student(cursor):
    id_delete = input('What is the ID of the student record you want to delete?')
    cursor.execute('DELETE FROM database WHERE Student_id = ?', id_delete)
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    print('Student I.D.   First_Name   Last_Name   Class_Name              Address              Phone_Number       '
          '  Email')
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:22}{row[4]:23}{row[5]:16}{row[6]:25}')


# Function to add a student to the table
def add_student(cursor):
    id = input('What is their ID? ')
    fn = input('What is their first name? ')
    ln = input('What is their last name? ')
    cl = input('What is their class? ')
    ad = input('What is their address? ')
    pn = input('What is their phone number? ')
    em = input('What is their email? ')
    cursor.execute("""INSERT INTO database (Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email) 
                    VALUES (?,?,?,?,?,?,?)""", (id, fn, ln, cl, ad, pn, em))
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    print('Student I.D.   First_Name   Last_Name   Class_Name              Address              Phone_Number       '
          '  Email')
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:22}{row[4]:23}{row[5]:16}{row[6]:25}')


def main():
# Connect to database
    connect = sqlite3.connect("Student_Base.db")
# Create Cursor
    cursor = connect.cursor()
    answer = True
# Ask if they want to edit the records
    question = input("Would you like to edit the records? (Y/N) ")
# Create loop
    while answer:
# Find what it is that the user wants to edit
        if question.lower() == "y":
            q2 = input("Would you like to update, delete, or add a record? ")
            if q2.lower() == 'update':
                update_student(cursor)

            if q2.lower() == 'delete':
                delete_student(cursor)

            if q2.lower() == 'add':
                add_student(cursor)
# Print everything
        if question.lower() == "n":
            cursor.execute('SELECT * FROM database')
            results = cursor.fetchall()
            print('Student I.D.   First_Name   Last_Name   Class_Name              Address              Phone_Number '
                  '        Email')
            for row in results:
                print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:22}{row[4]:23}{row[5]:16}{row[6]:25}')
# Ask if they want to continue
        q3 = input('Do you want to continue to edit the database? ')
        if q3.lower() == 'y':
            answer = True
        else:
            answer = False


# Call main
if __name__ == "__main__":
    main()
