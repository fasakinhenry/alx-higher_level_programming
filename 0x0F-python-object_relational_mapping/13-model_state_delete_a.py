#!/usr/bin/python3
""""
A script that deletes all State objects with a name containin
the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    dbEngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=dbEngine)
    session = InstanceSession()

    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
