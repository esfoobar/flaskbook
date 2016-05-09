# Step 18
    
## Relationship model
    - Start the relationship Blueprint module
        - Create the folder
        - Create __init__.py, views.py, models.py
        - Register the blueprint on application.py
        - Test the "add_friend" route
        
    - Work on models
        - Define a friend as two records -- the from and the to
        - Explain the compound indexes
        
    - Do some tests on python terminal
```
python manage.py shell
from user.models import *
from relationship.models import *
user1 = User.objects.get(username='jorge')
user2 = User.objects.get(username='javier')
friends = Relationship(from_user=user1, to_user=user2, rel_type=Relationship.FRIENDS, status=Relationship.PENDING).save()
rel = Relationship.objects.first()
rel.to_json()
rel.from_user.username
```
    - On MongoDB terminal
```
db.relationship.find()
db.relationship.getIndexes()
```
