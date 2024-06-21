import boto3
s3 = boto3.client('s3')
response = s3.upload_file('springbootapp.zip', 'springapp-bucket', 'application.zip')
print("Uploaded application to s3.")