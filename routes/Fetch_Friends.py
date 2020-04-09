from flask import request,jsonify
from flask_restful import Resource, Api
from database.models import Companies,People
import json

class Invalid_Person():
    def get_message(self,id):
        message = 'Parameter person_' + str(id) + ' is invalid'
        return message
    def as_dict(self, id):
        message = self.get_message(id)
        return dict(message=message)

class Fetch_Friends(Resource):
    def get(self):
        person = request.args.getlist('person') 
        person_1 = person[0]
        person_2 = person[1]

        people_1 = People.objects(index=person_1).first()
        if(people_1 == None):
            result = Invalid_Person()
            return result.as_dict(1) 

        people_2 = People.objects(index=person_2).first()
        if(people_2 == None):
            result = Invalid_Person()
            print(result.as_dict(2))
            return result.as_dict(2) 

        common_friends = list(filter(lambda p: p in people_1.friend_indexes(),
                                     people_2.friend_indexes()))
        mutual_friends = People.objects(index__in=common_friends, eyeColor='brown',has_died=False)
        mutual_friends = list(map(lambda p: p.as_dict(), mutual_friends))

        return dict(
            person_1= people_1.as_dict(),
            person_2= people_2.as_dict(),
            mutual_friends= mutual_friends)
        