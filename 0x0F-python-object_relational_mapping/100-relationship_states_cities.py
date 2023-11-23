#!/usr/bin/python3
"""
 script that creates the State “California” with the City
 “San Francisco” from the database hbtn_0e_100_usa:
 (100-relationship_states_cities.py)
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    california = State(name="California", cities=[City(name="San Francisco")])

    session.add(california)

    session.commit()

    session.close()
