from flask import Flask, request, Response
from flask_restful import Resource, Api
from database.db import initialize_db
from routes.Fetch_Employees import Fetch_Employees
from routes.Fetch_Friends import Fetch_Friends
from routes.Fetch_Person import Fetch_Person
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://127.0.0.1:27017/Paranuara',
}

# Initializing the mongo db instance.
db = initialize_db(app)

# API for Feature 1:
api.add_resource(Fetch_Employees, '/fetch_employees')

# API for Feature 2:
api.add_resource(Fetch_Friends, '/fetch_friends')

# API for Feature 3:
api.add_resource(Fetch_Person,'/fetch_person')

if __name__ == "__main__":
    app.run()