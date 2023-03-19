#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create engine. Args: [1] = username, [2] = password, [3] = database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete all states containing 'a'
    for state in states:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close session
    session.close()
