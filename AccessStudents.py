# title: Access Student Database
# Authors: Taylor Nelson, Kadin Meyers, Benjamin Eerkes

import sqlite3


def update_student(cursor):
    id = input('What is the ID of the student record you want to update? ')
    value = input('What value of the record do you want to update? ')
    update = input('What do you want to update it too? ')
    cursor.execute('UPDATE database SET ' + value + ' = ? WHERE Student_id = ?', (update, id))
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def delete_student(cursor):
    id_delete = input('What is the ID of the student record you want to delete?')
    cursor.execute('DELETE FROM database WHERE Student_id = ?', id_delete)
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def add_student(cursor):
    ID = input('What is their ID? ')
    FN = input('What is their first name? ')
    LN = input('What is their last name? ')
    CL = input('What is their class? ')
    AD = input('What is their address? ')
    PN = input('What is their phone number? ')
    EM = input('What is their email? ')
    cursor.execute("""INSERT INTO database (Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email) 
                    VALUES (?,?,?,?,?,?,?)""", (ID, FN, LN, CL, AD, PN, EM))
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def main():
    connect = sqlite3.connect("Student_Base.db")
    cursor = connect.cursor()

    question = input("Would you like to edit the records? (Y/N) ")

    if question.lower() == "y":
        q2 = input("Would you like to update, delete, or add a record? ")
        if q2.lower() == 'update':
            update_student(cursor)

        if q2.lower() == 'delete':
            delete_student(cursor)

        if q2.lower() == 'add':
            add_student(cursor)

    if question.lower() == "n":
        cursor.execute('SELECT * FROM database')
        results = cursor.fetchall()
        for row in results:
            print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


if __name__ == "__main__":
    main()
