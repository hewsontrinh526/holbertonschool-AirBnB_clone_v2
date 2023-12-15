#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", back_populates="cities",
                              cascade="delete, delete-orphan")
        state = relationship("State", back_populates="cities")
    else:
        state_id = ""
        name = ""
