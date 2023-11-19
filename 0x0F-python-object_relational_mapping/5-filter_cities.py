#!/usr/bin/python3
"""
 a script that takes in the name of a state
 as an argument and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage:{}\
            <username> <password> <database> <state name>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()

    query = "SELECT cities.name\
        FROM cities JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s ORDER BY cities.id"

    executed_rows = cur.execute(query, (state_name,))

    rows = cur.fetchall()

    x = 1
    for row in rows:
        print(row[0], end='')
        if x < executed_rows:
            print(end=', ')
        x += 1
        
    print()
    cur.close()
    db.close()
