[![Build Status](https://travis-ci.com/jorge-3/flaskbook.svg?token=CpgTPHGMFe4PoRnkeQqo&branch=master)](https://travis-ci.com/jorge-3/flaskbook)

# Step 30

## Getting user's messages only if friends
- Modify user/views/profile to grab POSTs (not COMMENTS or LIKES)
- Check if friends to display posts
- Fix issue with posting on user's profile

## Adding likes to posts
- Add a like route on feed views
- Add a get likes method on feed model
- List likes on the message

## Comment cleanup
- Add the comment hyperlink to anchor on comment form
- Clear the comment text bug