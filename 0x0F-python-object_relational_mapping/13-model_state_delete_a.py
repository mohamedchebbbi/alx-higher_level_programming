#!/usr/bin/python3
''' print state obj from db '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).\
        filter(State.name.like('%a%')).all()
    for delete_record in record:
        session.delete(delete_record)

    session.commit()

    session.close()
