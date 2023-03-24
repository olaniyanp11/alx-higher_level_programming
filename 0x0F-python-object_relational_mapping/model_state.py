#!/usr/bin/python3
# importing the neccesary modules to work with!!!
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """
    a python file that contains the class 
    definition of a State and an instance 
    Base = declarative_base():
    """
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

