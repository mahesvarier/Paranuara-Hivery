from flask import request,jsonify
from flask_restful import Resource, Api
from database.models import Companies,People
import json
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import InternalServerError, SchemaValidationError, WrongParameterError
import werkzeug

# Return for a parameter that is not valid.
class Invalid_Person():
    def get_message(self,id):
        message = 'Parameter person_' + str(id) + ' is invalid'
        return message

    # Serializing to JSON. 
    def as_dict(self, id):
        message = self.get_message(id)
        return dict(message=message)


class Invalid_Params():
    def get_message(self):
        message = 'Parameter person_1 and parameter person_2 cannot be the same'
        return message

    # Serializing to JSON. 
    def as_dict(self):
        message = self.get_message()
        return dict(message=message)        

class Fetch_Friends(Resource):
    def get(self):
        try:
            # Fetching the parameters.
            person_1_param = request.args['person_1'] 
            person_2_param = request.args['person_2'] 
            
            if(person_1_param == person_2_param):
                result = Invalid_Params()
                return result.as_dict() 

            people_1 = People.objects(index=person_1_param).first()
            if(people_1 == None):
                result = Invalid_Person()
                return result.as_dict(1) 

            people_2 = People.objects(index=person_2_param).first()
            if(people_2 == None):
                result = Invalid_Person()
                return result.as_dict(2) 

            # Fetching common friends
            common_friends = list(filter(lambda p: p in people_1.friend_indexes(),
                                        people_2.friend_indexes()))

            # Fetching Mutual friends who are not dead and have brown eye color.
            mutual_friends = People.objects(index__in=common_friends, eyeColor='brown',has_died=False)
            mutual_friends = list(map(lambda p: p.as_dict(), mutual_friends))

            return dict(
                person_1= people_1.as_dict(),
                person_2= people_2.as_dict(),
                mutual_friends= mutual_friends
                )
        except (ValueError):
            raise WrongParameterError
        except (werkzeug.exceptions.BadRequestKeyError, IndexError):
            raise SchemaValidationError
        except:
            raise InternalServerError

        