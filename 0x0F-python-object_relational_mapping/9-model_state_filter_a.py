#!/usr/bin/python3
"""
A script that prints all states that contain letter a in the database
hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {}\
              <username> <password> <database_name>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(State.name.contains('a')).order_by(State.id)

    if results:
        for result in results:
            print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')

    session.close()
