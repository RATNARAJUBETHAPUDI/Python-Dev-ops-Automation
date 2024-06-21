import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')

response = clouwatch.put_metric_alarm(
AlarmName='HighCPUUsage',
MetricName='CPUUtilization',
Namespace='AWS/EC2',
Statistic='Average',
Period=300, # 5 MINUTES
EvaluationPeriods=1,
Threshold=80.0,
ComparisionOperator='GreaterThanThreshold',
AlramAction=[
    'arn:aws:sns:us-west-2:123456789012:NotifyMe'
    
],
Dimensions=[
    {'Name': 'InstanceId', 'Value': 'ami-08a0d1e16fc3f61ea'}
        
    ]
)

print("Alarm created:", response)