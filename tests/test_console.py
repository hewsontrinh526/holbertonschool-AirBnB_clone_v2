#!/usr/bin/python3
"""Testing console"""
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Setting it up for tests"""
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Tearing it down after each test"""
        storage.reload()

    def capture_output(self, command):
        """Help us capture"""
        saved_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            self.cmd.onecmd(command)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = saved_stdout

    def test_do_create(self):
        """Testing do_create"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
        create_id = output
        created_key = "BaseModel." + create_id
        self.assertIn(created_key, storage.all())

if __name__ == "__main__":
    unittest.main()
