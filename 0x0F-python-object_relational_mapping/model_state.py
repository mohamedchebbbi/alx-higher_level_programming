#!/usr/bin/python3
''' python file that contains the class definition of a State '''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    '''Class for State'''

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)

    def __str__(self):
        '''str form class'''
        return "{}: {}".format(self.id, self.name)
