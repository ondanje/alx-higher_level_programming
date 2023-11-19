#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
vulnerable to SQL injection
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print('Usage: {} <username> <password> <database> <state name>'.format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
