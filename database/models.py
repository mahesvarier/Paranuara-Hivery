from .db import db

# Creating Modal class for Companies Collection
class Companies(db.Document):
    # Defining the collection
    meta = {'collection': 'companies'}

    Index = db.IntField(required=True)
    Company = db.StringField(required=True)

# Embedded Document for People Collection
class FriendRef(db.EmbeddedDocument):
    index = db.IntField(required=True)

# Modal class for People Collection
class People(db.Document):
    # Defining the collection
    meta = {'collection': 'People'}

    index = db.IntField(required=True)
    has_died = db.BooleanField(required=True)
    eyeColor = db.StringField(required=True)
    name = db.StringField(required=True)
    age = db.IntField(required=True)
    address = db.StringField(required=True)
    phone = db.StringField(required=True)
    # Emdedded Document declaration
    friends = db.EmbeddedDocumentListField(FriendRef)
    favouriteFood = db.ListField(db.StringField())
    tags = db.ListField(db.StringField())
    company_id = db.IntField(required=True)
    registered = db.StringField()
    greeting = db.StringField()
    email = db.EmailField()
    about = db.StringField()
    guid = db.StringField()
    balance = db.StringField()
    picture = db.URLField()
    gender = db.StringField(required=True, choices=['male', 'female'])

    #Creating function to fetch all friends list in a document 
    def friend_indexes(self):
        return [friend_ref.index for friend_ref in self.friends]

    # Creating function to convert document into a dictionary to serialize to JSON.
    def as_dict(self):
        return dict(name=self.name, age=self.age, address=self.address, phone=self.phone)
