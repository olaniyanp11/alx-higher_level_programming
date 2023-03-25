#!/usr/bin/python3
"""
i a script that lists all State objects from the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # create a engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a new Session instance bound to the engine we created
    Session = sessionmaker(bind=engine)
    session = Session()
    # query the database
    table = State(
            name='Louisiana'
            )
    session.add(table)
    session.commit()
    print(table.id)
    session.close()
