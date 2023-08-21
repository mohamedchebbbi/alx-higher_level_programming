#!/usr/bin/python3
''' class of city '''

from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    '''Class City'''

    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)

    def __str__(self):
        '''str form class'''
        return "{}: ({}) {}".format(self.state_id, self.id, self.name)
