[![Build Status](https://travis-ci.com/jorge-3/flaskbook.svg?token=CpgTPHGMFe4PoRnkeQqo&branch=master)](https://travis-ci.com/jorge-3/flaskbook)

# Step 26
    
## Start Feed Module
    - Feed Blueprint
    - Create message model
        - from user is always filled
        - to user is optional and represents when a user posts a message in another user's wall
        - parent represents replies to a post
    - Create feed model
        - this is a fan out pattern, which allows each user to see messages personalized for them
            - on their homepage, users will see posts their friends have posted to all as well as messages friends have posted to common friends
            - we won't see comments by users we have blocked, but will see comments by people we're not friends with
            - this is called the fan out pattern. it allows fine control of content, even though it looks a bit repetitive. Twitter [uses a version of this model](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html)
    - Add the text input on the user's homepage
    