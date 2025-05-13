from datetime import datetime, timedelta
import boto3

def find_idle_instances(threshold_hours=24, threshold_cpu=5):
    ec2 = boto3.client('ec2')
    cw = boto3.client('cloudwatch')
    response = ec2.describe_instances()
    idle_instances = []

    for res in response['Reservations']:
        for inst in res['Instances']:
            instance_id = inst['InstanceId']
            metrics = cw.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.utcnow() - timedelta(hours=threshold_hours),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            datapoints = metrics.get('Datapoints', [])
            if datapoints:
                avg_cpu = sum([dp['Average'] for dp in datapoints]) / len(datapoints)
                if avg_cpu < threshold_cpu:
                    idle_instances.append((instance_id, round(avg_cpu, 2)))
    return idle_instances
