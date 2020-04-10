from flask import request
from flask_restful import Resource, Api
from database.models import People
import json
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import InternalServerError, SchemaValidationError, WrongParameterError
import werkzeug

fruits = set(['apple', 'strawberry', 'orange', 'banana'])
vegetable = set(['beetroot', 'celery', 'carrot', 'cucumber'])

class Fetch_Fruits(Resource):
    def get(self):
        try:
            company_id = request.args.getlist('person_id') 
            if len(company_id) == 0:
                return {
                        "message": "Person Id is required"
                        }
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
                }
            return result
        except (ValueError):
            raise WrongParameterError
        except (werkzeug.exceptions.BadRequestKeyError, IndexError):
            raise SchemaValidationError
        except:
            raise InternalServerError