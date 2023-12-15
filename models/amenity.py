#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   primary_key=True, nullable=False),
            Column('amenity_id', String(60),
                   ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
              )
        name = Column(String(128), nullable=False)

        places = relationship("Place",
                              secondary=place_amenity,
                              back_populates='amenities'
                              )
    else:
        name = ""