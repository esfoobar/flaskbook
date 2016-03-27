# Step 12
    
## Emailing with AWS SES
    - Explain how to send email via SES
        - Create an AWS account
        - Create a user on IAM
        - Go to IAM/Policies and attach AmazonSESFullAccess to your user
    - Install boto3
    - Set credentials in ~/.aws/credentials
        - Important: No quotes around your values
        - `[default]`
            `aws_access_key_id = <your access key>`
            `aws_secret_access_key = <your secret key>`
    - Set region in ~/.aws/config (you can set the region on the upper right nav on SES console)
        - `[default]`
        - `region=us-east-1`
    
## Send an email when user registers
    - Create a mail folder on templates
    - Create a base for html and text
    - Create register email both text and html
    - Add email to utilities/common
    - Send a test email
```
from flask import render_template
from user.models import User
user = User.objects.first()
body_html = render_template('mail/user/register.html', user=user)
body_text = render_template('mail/user/register.txt', user=user)
from utilities.common import email
email('j@jorge3.com', 'Welcome to Flaskbook', body_html, body_text)
```
    - Teach that this is an async job and that we'll see more of those soon