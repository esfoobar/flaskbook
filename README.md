# Step 19
    
## Relationship frontend
    - Create methods on user model to check if a user is a friend
    - Test it:
```
python manage.py shell
from user.models import *
from relationship.models import *
Relationship.objects.delete()
user1 = User.objects.get(username='jorge')
user2 = User.objects.get(username='javier')
friends = Relationship(from_user=user1, to_user=user2, rel_type=Relationship.FRIENDS, status=Relationship.APPROVED).save()
Relationship.get_relationship(user1,user2)
```
    - Add rel object to user.views

