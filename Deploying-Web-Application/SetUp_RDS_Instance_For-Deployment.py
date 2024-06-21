import boto3
rds = boto3.client('rds',region_name='us-west-2')

response = rds.create_db_instance(
    DBInstanceIdentifier='devdbinstance',
    MasterUsername='admin'
    MasterUserPassword='root',
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    AllocatedStorage=20
    
)
print("Creating RDS Instance:", response['DBInstance']['DBInstanceIdentifier'])