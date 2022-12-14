# title: Access Student Database
# Authors: Taylor Nelson, Kadin Meyers, Benjamin Eerkes

import sqlite3


def update_student(cursor):
    id = input('What is the ID of the student record you want to update? ')
    value = input('What value of the record do you want to update? ')
    update = input('What do you want to update it too? ')
    cursor.execute('UPDATE database SET ' + value + ' = ? WHERE Student_id = ?', (update, id))


def delete_student(cursor):
    id_delete = input('What is the ID of the student record you want to delete?')
    cursor.execute('DELETE FROM database WHERE Student_id = ?', id_delete)


def main():
    connect = sqlite3.connect("Student_Base.db")
    cursor = connect.cursor()

    question = input("Would you like to edit the records? (Y/N) ")

    if question.lower() == "y":
        q2 = input("Would you like to update or delete a record? ")
        if q2.lower() == 'update':
            update_student(cursor)

        if q2.lower() == 'delete':
            delete_student(cursor)

    if question.lower() == "n":
        # Print info
        pass


if __name__ == "__main__":
    main()
