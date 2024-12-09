import mongoengine as me

from .cards import Quote


class User(me.Document):
    username = me.StringField(required=True)
    email = me.StringField(required=True)
    hashed_password = me.StringField(required=True)

    quote = me.EmbeddedDocumentField(Quote)
