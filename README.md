# Step 6

## User Registration
    - Implement the form error
    - Install py-bcrypt
    - Do the user registration with the salted password
    - Try regitering with user "jorge" -- you will get a duplicate key error
    
## Add model validation on user.form for username and email (unique fields)
    - Add `from wtforms.validators import ValidationError` and the individual field validators
    
## Reset the User database since we have a good user model
    - db.user.remove({})