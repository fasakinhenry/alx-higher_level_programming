#!/usr/bin/python3
"""
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    dbEngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(dbEngine)
    InstanceSession = sessionmaker(bind=dbEngine)
    session = InstanceSession()

    newState = State(name='California')
    newCity = City(name='San Francisco', state=newState)
    session.add(newCity)
    session.commit()

    session.close()
