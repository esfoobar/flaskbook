# Step 16
    
## Image uploading
    - Picture thumbnail library
        - `sudo apt-get install imagemagick libmagickcore-dev`
        - `pip install wand` (from requirements.txt)
        - Test the installation:
```
python manage.py shell
from wand.image import Image
with Image(filename='static/assets/flaskbook-logo-sm.png') as img:
    print(img.size)
```
        - Add `UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flaskbook/static/images'` to settings
    - Modify user's model to take a picture using timestamp (explain the thinking)
    - Modify edit profile to allow adding a picture

    - Setup AWS S3
    