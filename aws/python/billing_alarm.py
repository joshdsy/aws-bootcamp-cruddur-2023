import boto3

cloudwatch = boto3.client('cloudwatch')
paginator = cloudwatch.get_paginator('describe_alarms')
for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])

cloudwatch.put_metric_alarm(
    AlarmName='bootcamp-billing-alarm',
    AlarmDescription='bootcamp cruddur-2023',
    ActionsEnabled=True,
    EvaluationPeriods=1,
    Threshold=2000,
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    TreatMissingData='missing',
    Metrics=[
        {
            'Id': 'bootcamp-2023',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/Billing',
                    'MetricName': 'EstimatedCharges',
                    'Dimensions': [
                        {
                            'Name':'Currency',
                            'Value':'USD'
                        },
                        {
                            'Name':'LinkedAccount',
                            'Value':'AWSACCOUNTIDHERE'
                        }
                    ]
                },
                'Period': 21600,
                'Stat': 'Maximum',
                'Unit': 'Seconds'
            },
            'Label': 'EstimatedCharges > 1000 for 1 datapoints within 6 hours',
            'ReturnData': True,
        },
    ],
)

