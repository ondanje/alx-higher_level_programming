#!/usr/bin/python3
"""Script that lists all City objects
from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {}\
            <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()

    for city in result:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
