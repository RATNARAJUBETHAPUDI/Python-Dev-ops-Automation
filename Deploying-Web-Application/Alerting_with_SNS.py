import boto3
sns = boto3.client('sns', region_name='us-west-2')

response= sns.create_topic(Name='NotifyMe')
topic_arn =response['TopicArn']

sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='ratnaesi008@gamil.com'
)
print("SNS topic and subscription created:", topic_arn)