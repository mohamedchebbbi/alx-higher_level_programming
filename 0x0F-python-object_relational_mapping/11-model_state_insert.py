#!/usr/bin/python3
''' add new satte obj to db '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    session.add(State(name='Louisiana'))
    session.commit()
    print(session.query(State).filter(State.name == 'Louisiana')[0].id)
    session.close()
