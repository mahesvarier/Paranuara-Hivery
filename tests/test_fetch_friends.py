import unittest
import json

from app import app
from database.db import db

class Test_Fetch_Friends(unittest.TestCase):

    test_client = app.test_client()
    get_db = db.get_db()

    def test_fetch_friends(self):
        # When
        response = self.test_client.get('fetch_friends?person_1=1&person_2=5')
        # Then
        self.assertEqual(200, response.status_code)

    if __name__ == "__main__":
        unittest.main()