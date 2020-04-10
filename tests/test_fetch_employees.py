import unittest
import json

from app import app
from database.db import db

class Test_Fetch_Employees(unittest.TestCase):

    test_client = app.test_client()
    get_db = db.get_db()

    def test_fetch_employees(self):
        response = self.test_client.get('fetch_employees?company_id=1')
        self.assertEqual(200, response.status_code)
    
    def test_fetch_employees_400_URL(self):
        response = self.test_client.get('fetch_employees')
        self.assertEqual(400, response.status_code)

    def test_fetch_employees_400_TYPE(self):
        response = self.test_client.get('fetch_employees?company_id=type')
        print(response)
        self.assertEqual(200, response.status_code)

    if __name__ == "__main__":
        unittest.main()