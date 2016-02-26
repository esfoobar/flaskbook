# Step 5

## Adding new fields and indexes to models
- Modify the user model and talk about how we can add fields to user models in mongodb
 - Add a bio
 - Add a couple of users

- Indexes
 - Do `db.user.find({'u': 'jorge'}).explain()` and explain how indexes are used (`"cursor" : "BasicCursor", "nscannedObjects" : 3,`)
 - Set username and email as unique, explain unique
 - Add indexes (explain why indexes)
 - Do `python manage.py shell` and update the user and then check `db.user.getIndexes()`
 - Do `db.user.find({'u': 'jorge'}).explain()` and explain how indexes are used (`"cursor" : "BtreeCursor u_1", "nscannedObjects" : 1,`)

## The register form
- Register User
 - Create templates folder
 - Create base, flashmessages, formhelpers (copy and paste from github, not important to explain this)
 - Add requirement.txt > flask-wtf and pip install -r
 - Create user forms.py and add registration form
 - Create templates > user > register.html (note the url_for ".register", for blueprints)
 - Add user > views register