(AMI,instance type, security groups )

import boto3
ec2 = boto3.client('ec2', region_name ='us-west-2')

response = ec2.run_instances(
    ImageId='ami-08a0d1e16fc3f61ea',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    keyName='dev-instance'
)
instance_ids= [instance['InstanceId'] for instance in response['instances']]
print("Launched EC2 Instances:" , instance_ids)
