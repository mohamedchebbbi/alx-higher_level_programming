#!/usr/bin/python3
''' contain the class city '''

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''Class def for City'''

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
        '''str form of the class'''
        return "{}: {}".format(self.id, self.name)
