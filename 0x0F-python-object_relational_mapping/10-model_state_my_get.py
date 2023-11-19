#!/usr/bin/python3

"""a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name == state_name)\
                    .order_by(State.id)
    if states is not None and states.count() > 0:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
