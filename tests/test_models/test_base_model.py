#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


class TestDatabaseStorage(unittest.TestCase):
    """Test cases for the DatabaseStorage class"""
    @classmethod
    def setUpClass(cls):
        os.environ["HBNB_ENV"] = "test"
        os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
        os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
        if hasattr(storage, '_DBStorage__session'):
            storage._DBStorage__session.close()
        else:
            None
        storage.reload()

    @classmethod
    def tearDownClass(cls):
        os.environ["HBNB_ENV"] = "production"
        storage.reload()

    def setUp(self):
        storage.reload()
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        if isinstance(storage, DBStorage):
            storage._DBStorage__session.close()
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_save(self):
        i = self.value()
        i.save()
        key = "{}.{}".format(type(i).__name__, i.id)
        obj = storage.all()[key]
        self.assertEqual(obj.to_dict(), i.to_dict())

    def test_delete(self):
        i = self.value()
        i.save()
        i_id = i.id
        key = "{}.{}".format(type(i).__name__, i_id)
        i.delete()
        self.assertNotIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
