from flask import request
from flask_restful import Resource, Api
from database.models import Companies,People
import json
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import InternalServerError, SchemaValidationError, WrongParameterError
import werkzeug

class No_Records():
    def __init__(self):
        message = 'No Employees'

class Fetch_Employees(Resource):
    def get(self):
        try:
            company_id = request.args['company_id'] 
            people = People.objects(company_id=company_id)
            people_data = people.to_json()
            dicts = json.loads(people_data)
            if len(dicts) == 0:
                no_records = No_Records()
                print(no_records.message)
                return {'message': 'No Employees'}
            return dicts
        except (ValueError):
            raise WrongParameterError
        except (werkzeug.exceptions.BadRequestKeyError):
            raise SchemaValidationError
        except:
            raise InternalServerError