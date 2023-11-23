#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {}\
            <username> <password> <database name>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State).order_by(State.id)

    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
