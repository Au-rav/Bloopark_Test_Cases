import sqlite3
from sqlite3 import Error


def create_connection(db_file):
 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_students(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT COUNT(StudentId) FROM students where firstName = "John")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        print("Number of students with first name John")
        select_all_students(conn)


if __name__ == '__main__':
    main()