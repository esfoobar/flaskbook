# Step 12

## Password work
    - Change password functionality
        - New view/template
    
## Emailing with AWS SES
    - Explain how to send email via SES
        - Create an AWS account
        - Create a user on IAM
        - Go to IAM/Policies and attach AmazonSESFullAccess to your user
    - Install boto
    - Test sending an email:
        - `python manage.py shell`
        - `import boto.ses`
        - For the next step, check the SMTP settings to see what region to use
        - `conn = boto.ses.connect_to_region('us-east-1',aws_access_key_id=‘xxx’,aws_secret_access_key=‘xxx’)`
        - `conn`
        - `conn.verify_email_address(‘webmaster@fromzero.io’)`
        - `conn.list_verified_email_addresses()`
        - `conn.send_email('webmaster@fromzero.io','Test subject','Can you read this?’,[jorge@example.com])`
    
## Forgot username / password
    - Add a link on login page
    - Add a view with a form