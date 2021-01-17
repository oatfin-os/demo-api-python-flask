import datetime

from mongoengine import Document, StringField, DateTimeField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    created = DateTimeField(default=datetime.datetime.utcnow)
    updated = DateTimeField(required=False)

    def json(self):
        return {
            'user_id': str(self['id']),
            'username': self['username'],
            'created': self['created'],
            'updated': self['updated'],
        }
