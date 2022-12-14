# title: Student Database
# Authors: Taylor Nelson, Kadin Meyers, Benjamin Eerkes

import sqlite3


# Mainline
def main():
    # Starts connection to database
    conn = sqlite3.connect("Student_Base.db")
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE database (Student_id INTEGER PRIMARY KEY NOT NULL, First_Name TEXT,
                       Last_Name TEXT, Class TEXT, Address TEXT, Phone_Number REAL, Email TEXT) """)
    students = [
        (1, "Ben", "John", "Intro to coding", "47483 454th NW", "756-374-3734", "Ben.John@gmail.com"),
        (2, "Mike", "Willing", "World History", "P.O. Box 301", "218-216-7548", "mikewilling@yahoo.com"),
        (3, "Andrea", "Williams", "Lifespan Psychology", "206 Bell Ave", "218-428-7654", "andreawilliams@gmail.com"),
        (4, "Henry", "Johnson", "Mathmatics", "5702 Potato Street", "218-966-3232", "henryjohnson@outlook.com"),
        (5, "Ronald", "Weasley", "Statistics", "4744 Carrot Street", "218-523-8723", "ronweasley@gmail.com"),
        (6, "Jerry", "Foreman", "Farming", "8457 Green Bean Ave", "218-631-6245", "jerryforeman@yahoo.com"),
        (7, "Conway", "Smith", "Intro to Spreadsheets", "206 Corn Cove", "218-986-7854", "conwaysmith@gmail.com"),
        (8, "Daniel", "Brown", "Composition", "3524 Zucchini Street", "218-974-6657", "danielbrown@outlook.com"),
        (9, "Jalen", "Miller", "Intro to Speech", "202 Cucumber Ave", "218-965-9842", "jalenmiller@gmail.com"),
        (10, "Gracie", "Truman", "Statistics", "288 Broccoli Street", "218-958-2115", "gracietruman@gmail.com")
    ]

    cur.executemany(""" INSERT INTO database (Student_id, First_Name, Last_Name, Class, Address, Phone_Number, Email) VALUES
                        (?,?,?,?,?,?,?) """, students)

    # Selects the data from the table and outputs it
    # cur.execute('SELECT student_id, First_Name, Last_Name, Phone_Number, Address, Major, Email FROM students')
    # results = cur.fetchall()
    # print('Student I.D.   First_Name   Last_Name   Phone_Number   Address               Major           Email')
    # for row in results:
    #     print(f'{row[0]:<15}{row[1]:<13}{row[2]:<12}{row[3]:<15}{row[4]:<22}{row[5]:<16}{row[6]}')

    conn.commit()
    conn.close()


# Calls main function and begins execution
if __name__ == "__main__":
    main()
