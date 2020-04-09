from flask import request
from flask_restful import Resource, Api
from database.models import People
import json

fruits = set(['apple', 'strawberry', 'orange', 'banana'])
vegetable = set(['beetroot', 'celery', 'carrot', 'cucumber'])

class Fetch_Fruits(Resource):
    def get(self):
        company_id = request.args.getlist('person_id') 
        if len(company_id) == 0:
            return {"message": "Person Id is required"}
        company_id = company_id[0]
        people = People.objects(index=company_id).first()

        set_items = set(people.favouriteFood)
        fruits_list = list(set_items & fruits)
        vegetable_list = list(set_items & vegetable)
        result = {
            "username": people.name,
            "age": people.age,
            "fruits": fruits_list,
            "vegetables": vegetable_list
            # "items_test": people.favouriteFood
        }
        
        return result