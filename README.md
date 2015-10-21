# Step 2

## Create virtualenv and install packages
- We setup the virtualenv: `virtualenv -p python3 venv` and initialize `source venv/bin/activate`
- Install the requirements: `pip install -r requirements.txt`

## Create basic structure
- The factory pattern for Flask applications
 - Create settings.py
 - Create application
 - Create manage.py
 - Run the app `python manage.py runserver`. You will see a 404, since we don't have views.


