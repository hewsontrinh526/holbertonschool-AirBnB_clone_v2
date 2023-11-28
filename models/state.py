#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Gets cities and returns list of City instances"""
            city_instance = storage.all(City)
            return [city for city in city_instance.values()
                    if city.state_id == self.id]
    else:
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
