#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, null
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import relationship
import os


metadata = MetaData()


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenity = Table(
            'place_amenity',
            metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                    primary_key=True, nullable=False),
            Column('amenity_id', String(60),
                   ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
        )

        city_id = Column(String(60),
                         ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default=null())
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=null())
        longitude = Column(Float, nullable=True, default=null())
        amenity_ids = []

        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, overlaps="place_amenities")

    else:
        @property
        def reviews(self):
            """
            Getter attribute to return a list of Review instances with place_id
            equals to the current Place.id
            """
            from models import storage
            review_dict = storage.all(Review)
            review_list = []
            for key, value in review_dict.items():
                if self.id == value.place_id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains all
            Amenity.id linked to the Place
            """
            from models import storage
            amenity_dict = storage.all(Amenity)
            amenity_list = []
            for key, value in amenity_dict.items():
                if self.id == value.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for adding
            an Amenity.id to the attribute amenity_ids. This method should
            accept only Amenity object, otherwise, do nothing.
            """
            from models import storage
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
