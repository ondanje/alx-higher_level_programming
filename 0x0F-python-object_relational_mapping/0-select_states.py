#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: {} <username> <password> <database>'.format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()

    cur.execute('SELECT *FROM states ORDER BY states.id')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()