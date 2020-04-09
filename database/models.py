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
    balance = db.StringField()
    picture = db.URLField()
    gender = db.StringField(required=True, choices=['male', 'female'])

    def friend_indexes(self):
        """Return indexes for friend from associated FriendRefs"""
        # note: in `people` collection there are circular references, i.e. a person
        # is a friend with him/herself
        return [friend_ref.index for friend_ref in self.friends]

    def as_dict(self):
        """Helper to render a person as dict with basic attributes"""
        return dict(name=self.name, age=self.age, address=self.address, phone=self.phone)
