# title: Student Database
# Authors: Taylor Nelson, Kadin Meyers, Benjamin Eerkes

import sqlite3


# Mainline
def main():
    # Starts connection to database
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    # Makes new table if it does not exist containing fields related to a student
    cur.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY NOT NULL, 
                                            First_Name TEXT, 
                                            Last_Name TEXT, 
                                            Phone_Number TEXT,  
                                            Address TEXT,
                                            Major TEXT,
                                            Email TEXT)''')

    # Adds data to the table (for 1 student)
    cur.execute('''INSERT INTO students  (First_Name , Last_Name, Phone_Number, Address, Major, Email) VALUES ('Bob',
    'Smith','746-465-0495','12454 456th Ave Nw','Engineering', 'bob.smith@gmail.com') ''')

    # Selects the data from the table and outputs it
    cur.execute('SELECT student_id, First_Name, Last_Name, Phone_Number, Address, Major, Email FROM students')
    results = cur.fetchall()
    print('Student I.D.   First_Name   Last_Name   Phone_Number   Address               Major           Email')
    for row in results:
        print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')

    conn.commit()
    conn.close()


# Calls main function and begins execution
if __name__ == "__main__":
    main()
