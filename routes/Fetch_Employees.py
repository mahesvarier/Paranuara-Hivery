from flask_restful import Resource, Api
from database.models import Companies,People
import json

class Fetch_Employees(Resource):
    def get(self, company_id):
        people = People.objects(company_id=company_id)
        people_data = people.to_json()
        dicts = json.loads(people_data)
        if len(dicts) == 0:
            return {'message': 'No Employee'}
        return dicts