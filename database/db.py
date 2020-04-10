from flask_mongoengine import MongoEngine

# ODM for MongoDB
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)