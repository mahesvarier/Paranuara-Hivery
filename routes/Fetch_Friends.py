from flask import request,jsonify
from flask_restful import Resource, Api
from database.models import Companies,People
import json

class Fetch_Friends(Resource):
    def get(self):
        keys = ["name", "address", "age", "phone"]
        
        person = request.args.getlist('person') 
        person_1 = person[0]
        person_2 = person[1]

        people_1 = People.objects(index=person_1).first()
        if(people_1 == None):
            return {'message': 'Person 1 is invalid'}
        # people_data_1 = people_1.to_json()
        # people_first = json.loads(people_data_1)
        # people_first_dict = {x: people_first[x] for x in keys}

        people_2 = People.objects(index=person_2).first()
        if(people_2 == None):
            return {'message': 'Person 2 is invalid'}
        # people_data_2 = people_2.to_json()
        # people_second = json.loads(people_data_2)
        # people_first_dict = {x: people_second[x] for x in keys}

        common_friends = list(filter(lambda p: p in people_1.friend_indexes(),
                                     people_2.friend_indexes()))
        mutual_friends = People.objects(index__in=common_friends, eyeColor='brown',has_died=False)
        mutual_friends = list(map(lambda p: p.as_dict(), mutual_friends))

        return dict(
            person_1= people_1.as_dict(),
            person_2= people_2.as_dict(),
            mutual_friends= special_friends)
        