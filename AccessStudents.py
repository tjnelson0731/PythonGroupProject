import sqlite3


def update_student():
    conn = sqlite3.connect("Students_Base.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS database(Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email)")
    id = input('What is the ID of the student record you want to update? ')
    value = input('What value of the record do you want to update? ')
    update = input('What do you want to update it too? ')
    cursor.execute('UPDATE database SET ' + value + ' = ? WHERE Student_id = ?', (update, id))
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def delete_student():
    conn = sqlite3.connect("Students_Base.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS database(Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email)")
    id_delete = input('What is the ID of the student record you want to delete?')
    cursor.execute('DELETE FROM database WHERE Student_id = ?', id_delete)
    cursor.execute('SELECT * FROM database')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def add_student():
    conn = sqlite3.connect("Students_Base.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS database(Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email)")
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
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


def main():
    connect = sqlite3.connect("Student_Base.db")
    cursor = connect.cursor()

    question = input("Would you like to edit the records? (Y/N) ")

    if question.lower() == "y":
        q2 = input("Would you like to update, delete, or add a record? ")
        if q2.lower() == 'update':
            update_student()

        if q2.lower() == 'delete':
            delete_student()

        if q2.lower() == 'add':
            add_student()

    if question.lower() == "n":
        cursor.execute("CREATE TABLE IF NOT EXISTS database(Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email)")
        cursor.execute('SELECT * FROM database')
        results = cursor.fetchall()
        for row in results:
            print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')


if __name__ == "__main__":
    main()
