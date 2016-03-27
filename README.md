# Step 13
    
## Emailing when user registers
    - We need to generate a confirmation code
        - On user.models add email_confirmed and email_configuration
        - On user.views add a UUID and store on the database
    - We need a view to confirm the email
        - Create a confirm route on user.views
        - Register a new user and check on mongodb the code
        - Hit /confirm/<username>/<code> with a bad username and a good username
        - Check on mongodb
        - Hit the correct username again, you should get a 404
    - Now send the email when user registers
        - Create a HOSTNAME on settings.py (explain dev vs prod)
        - Change the URLs on the email templates
        - Send the email from register views
    -> We need to skip sending email when running test
    - Write a test for new confirm functionality
    
## If user changes emails
    - Need to set email_confirmed to False and send confirmation email
    