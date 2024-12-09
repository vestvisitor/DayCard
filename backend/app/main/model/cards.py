import mongoengine as me


class Quote(me.EmbeddedDocument):
    text = me.StringField(required=True)
    author = me.StringField(required=True)
