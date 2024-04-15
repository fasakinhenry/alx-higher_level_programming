#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    dbEngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(dbEngine)
    InstanceSession = sessionmaker(bind=dbEngine)
    session = InstanceSession()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()
