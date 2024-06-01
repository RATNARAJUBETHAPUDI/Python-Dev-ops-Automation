import boto3
import datetime

# configuration
INSTANCE_ID = 'ami-00beae93a2d981137'
THRESHOLD = 80
ALARM_NAME = 'HighCPUUtilization'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:687292992592:alram'
REGION = 'us-east-1'

#Intialize boto3 clients
cloudwatch = boto3.client('cloudwatch' , region_name=REGION)
ec2 = boto3.client('ec2', region_name=REGION) 

def create_alarm(instance_id, threshold, alarm_name, sns_topic_arn):
    cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        AlarmDescription='Alarm when CPU exceeds {}%' .format(threshold),
        ActionsEnabled=True,
        AlarmActions='CPUUtilization',
        Namespace='AWS/EC2',
        statistic='Average',
        Dimentions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
                
            },
        ],
        Period=300,
        EvaluationPeriod=1,
        Threshold=threshold,
        comparisonOperator='GreatorThenThreshold'
    )
    print(f'Created alarm {alarm_name} for instance {instance_id}.')
    
def get_cpu_utilization(instance_id):
    end_time = datetime.datetime.estnow()
    start_time = end_time - datetime.timedelta(minutes=60)
    
    response= cloudwatch.get_metric_statistics(
        Namespace = 'AWS/EC2',
        MetricName='CPUUtilization',
        Dimentions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
        
    )
    data_points = response['Datapoints']
    if data_points:
        latest_data_point = sorted(data_points, key=lambda x: x['Timestamp'])[-1]
        cpu_utilization = latest_data_point['Average']
        print(f'cpu Utilization for{instance_id}: {cpu_utilization:.2f}%')
        return cpu_utilization
    else:
        print(f'No cpu utilization data available for instance {instance_id}.')
        return None
    
    if __name__ == "__main__":
        #monitor cpu utilization
        cpu_utilization = get_cpu_utilization(INSTANCE_ID)
        
        # Create cloudwatch alarm if CPU utilization exceeds threshold
        if cpu_utilization is not None and cpu_utilization > THRESHOLD:
            create_alarm(INSTANCE_ID, THRESHOLD,ALARM_NAME,SNS_TOPIC_ARN)