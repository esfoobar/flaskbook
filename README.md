[![Build Status](https://travis-ci.com/jorge-3/flaskbook.svg?token=CpgTPHGMFe4PoRnkeQqo&branch=master)](https://travis-ci.com/jorge-3/flaskbook)

# Step 28
    
## Adding images to posts
- Create static/images/posts folder locally and aws s3
- Add images ListField on feed/model
- Add images multiple field on form
- Add form field on templates/home/feed_home and templates/user/profile
- Create a resize helper on utilities/imaging that only scales vertically and keeps horizontal ratio and sends back size (to be stored on db)