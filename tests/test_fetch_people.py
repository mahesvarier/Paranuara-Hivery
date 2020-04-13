import unittest
import json

from app import app
from database.db import db

class Test_Fetch_Fruits(unittest.TestCase):

    test_client = app.test_client()
    get_db = db.get_db()

    def test_fetch_people(self):
        response = self.test_client.get('fetch_person?person_id=6')
        self.assertEqual(200, response.status_code)

    def test_fetch_people_400_URL(self):
        response = self.test_client.get('fetch_person')
        self.assertEqual(200, response.status_code)

    def test_fetch_people_400_TYPE(self):
        response = self.test_client.get('fetch_person?person_id=type')
        print(response)
        self.assertEqual(400, response.status_code)

    if __name__ == "__main__":
        unittest.main()