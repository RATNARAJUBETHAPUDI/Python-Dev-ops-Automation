import boto3
# uploading a file to s3
s3 = boto3.client('s3')
response = s3.upload_file('terraformstate.tf','terraformbucket','terraformstatefile.txt')
print(response)