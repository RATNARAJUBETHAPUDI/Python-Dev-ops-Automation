import boto3
#starting an ec2 instance
ec2 = boto3.client('ec2')
response = ec2.start_instances(InstanceIds=['ami-08a0d1e16fc3f61ea'])
print(response)