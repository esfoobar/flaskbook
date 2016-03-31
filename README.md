# Step 17
    
## Image uploading to S3
    - Set up the S3 bucket in AWS
        - Mimic the same path of static
        - Set the bucket to public read
        - Make sure you add `AmazonS3FullAccess` as a policy to your user in IAM
    - Modify the imaging library to use S3 if Debug=False
    
    