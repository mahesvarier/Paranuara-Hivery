from .db import db

class Companies(db.Document):
    meta = {'collection': 'companies'}

    Index = db.IntField(required=True)
    Company = db.StringField(required=True)

class FriendRef(db.EmbeddedDocument):
    """Holds a friend reference."""
    index = db.IntField(required=True)

class People(db.Document):
    meta = {'collection': 'People'}

    index = db.IntField(required=True)
    has_died = db.BooleanField(required=True)
    eyeColor = db.StringField(required=True)
    name = db.StringField(required=True)
    age = db.IntField(required=True)
    address = db.StringField(required=True)
    phone = db.StringField(required=True)
    friends = db.EmbeddedDocumentListField(FriendRef)
    favouriteFood = db.ListField(db.StringField())
    tags = db.ListField(db.StringField())
    company_id = db.IntField(required=True)
    registered = db.StringField()
    greeting = db.StringField()
    email = db.EmailField()
    about = db.StringField()
    guid = db.StringField()
    balance = db.DecimalField()
    picture = db.URLField()
    gender = db.StringField(required=True, choices=['male', 'female'])