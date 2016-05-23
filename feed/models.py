from mongoengine import CASCADE

from application import db
from utilities.common import utc_now_ts as now
from user.models import User

class Message(db.Document):
    user = db.ReferenceField(User, db_field="u", reverse_delete_rule=CASCADE)
    text = db.StringField(db_field="t", max_length=1024)
    live = db.BooleanField(db_field="l", default=True)
    create_date = db.IntField(db_field="c", default=now())
    parent = db.ObjectIdField(db_field="p", default=None)
    image = db.StringField(db_field="i", default=None)
    
    meta = {
        'indexes': [('user', '-create_date', 'parent', 'live')]
    }
    
class Feed(db.Document):
    to_user = db.ReferenceField(User, db_field="tu", reverse_delete_rule=CASCADE)
    message = db.ReferenceField(Message, db_field="m", reverse_delete_rule=CASCADE)
    create_date = db.IntField(db_field="c", default=now())
    parent = db.ObjectIdField(db_field="p", default=None)
    
    meta = {
        'indexes': [('to_user', '-create_date', 'parent')]
    }