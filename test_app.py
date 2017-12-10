import os
import main
import unittest
import tempfile
from db import database
import json

db = database.Database()

class TestApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        print(db)

    def test_get_all(self):
        rt = self.app.get('/risk_types')
        data = json.loads(rt.data)
        assert len(data) == 2

    def test_get_valid(self):
        rt = self.app.get('/risk_types/1')
        data = json.loads(rt.data)
        assert data['name'] == 'Car Insurance'

    def test_get_invalid(self):
        rt = self.app.get('/risk_types/3')
        data = json.loads(rt.data)
        assert data == None

if __name__ == '__main__':
    unittest.main()