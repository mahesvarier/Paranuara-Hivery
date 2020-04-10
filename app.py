from flask import Flask, request, Response
from flask_restful import Resource, Api
from database.db import initialize_db
from routes.Fetch_Employees import Fetch_Employees
from routes.Fetch_Friends import Fetch_Friends
from routes.Fetch_Fruits import Fetch_Fruits
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://127.0.0.1:27017/Paranuara',
}

db = initialize_db(app)

api.add_resource(Fetch_Employees, '/fetch_employees')
api.add_resource(Fetch_Friends, '/fetch_friends')
api.add_resource(Fetch_Fruits,'/fetch_fruits')

if __name__ == "__main__":
    app.run()
# app.run()