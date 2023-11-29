#!/usr/bin/python3
"""Testing DBStorage"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import os


storage = DBStorage()
storage_type = os.getenv('HBNB_TYPE_STORAGE')

@unittest.skipIf(storage_type == "fs", "not using DBStorage")
class test_DBStorage(unittest.TestCase):
    """ Class test of the DBStorage"""

    def setUp(self):
        """"Setting it up"""
        del_list = []
        for key in storage._DBStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._DBStorage__objects[key]
