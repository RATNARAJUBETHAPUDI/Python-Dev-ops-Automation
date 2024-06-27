import boto3
from botocore.exceptions import NoCredentialsError
def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name =file_name
        s3_client= boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name,bucket,object_name)
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("credentials not available")
            return False
        return True
    