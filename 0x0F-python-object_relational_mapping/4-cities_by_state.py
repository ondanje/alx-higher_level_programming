#!/usr/bin/python3
"""
 a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states\
             ON cities.state_id=states.id\
                 ORDER BY cities.id;")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
