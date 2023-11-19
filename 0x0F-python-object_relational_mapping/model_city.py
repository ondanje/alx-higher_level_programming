#!/usr/bin/python3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base


class City(Base):
    """
    State class the links to MySQL TABLE  states
    """
    __tablename__ = 'cities'

    id = Column(Integer, Sequence('state_id_seq'),
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
