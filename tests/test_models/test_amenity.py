#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.__init__ import storage
import os


storage_type = os.getenv('HBNB_TYPE_STORAGE')
class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(storage_type == "fs", "not using DBStorage")
    def test_db_save(self):
        """DB save"""
        attributes = {
            "name" : "Mina"
        }
        new_item = self.value(**attributes)
        new_item.save()
        all_items = storage.all(self.value)
        self.assertTrue(len(all_items) > 0)