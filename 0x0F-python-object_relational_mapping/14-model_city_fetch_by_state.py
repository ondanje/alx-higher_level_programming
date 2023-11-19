#!/usr/bin/python3
"""
script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    cities = session.query(State.name, City.id, City.name)\
                    .join(City, City.state_id == State.id)\
                    .order_by(City.id)

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
