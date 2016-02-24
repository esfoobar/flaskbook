from application import db

from utilities.common import utc_now_ts as now

class User(db.Document):
    username = db.StringField(db_field="u", required=True, unique=True)
    password = db.StringField(db_field="p", required=True)
    email = db.EmailField(db_field="e", required=True, unique=True)
    first_name = db.StringField(db_field="fn", max_length=50)
    last_name = db.StringField(db_field="ln", max_length=50)
    bio = db.StringField(db_field="bio", max_length=50)
    created = db.IntField(db_field="c", default=now())
    
    meta = {
        'indexes': ['username', 'email', '-created']
        }
    
    