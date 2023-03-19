#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        # create connection to database
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                               .format(username, password, db_name),
                               pool_pre_ping=True)

        # create all tables in the database
        Base.metadata.create_all(engine)

        # create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # create a new State object and add it to the session
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        # print the id of the newly created State object
        print(new_state.id)

        # close the session
        session.close()
