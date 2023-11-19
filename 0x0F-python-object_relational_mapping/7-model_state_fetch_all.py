#!/usr/bin/python3
"""
 a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {}\
            <username> <password> <database_name>".format(argv[0]))
        exit(1)
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))

    session.close()
