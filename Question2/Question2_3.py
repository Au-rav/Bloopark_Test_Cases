import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_year(conn):
    sql = UPDATE enrollements 
              SET year = 2015
              WHERE id between 20 and 100            
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_year(conn)


if __name__ == '__main__':
    main()



