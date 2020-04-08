from flask import Flask, request, Response
from flask_restful import Resource, Api
from database.db import initialize_db
from routes.Fetch_Employees import Fetch_Employees

app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://127.0.0.1:27017/Paranuara',
}

db = initialize_db(app)

api.add_resource(Fetch_Employees, '/fetch_employees/<int:company_id>')

app.run()