import boto3

client = boto3.client('budgets')
response = client.create_budget(
    AccountId='string',
    Budget={
        'BudgetName': 'string',
        'BudgetLimit': {
            'Amount': 'string',
            'Unit': 'string'
        },
        'PlannedBudgetLimits': {
            'string': {
                'Amount': 'string',
                'Unit': 'string'
            }
        },
        'CostFilters': {
            'string': [
                'string',
            ]
        },
        'CostTypes': {
            'IncludeTax': True,
            'IncludeSubscription': True,
            'UseBlended': False,
            'IncludeRefund': True,
            'IncludeCredit': False,
            'IncludeUpfront': False,
            'IncludeRecurring': True,
            'IncludeOtherSubscription': True,
            'IncludeSupport': False,
            'IncludeDiscount': True,
            'UseAmortized': True
        },
        'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
        'TimePeriod': {
            'Start': datetime(2015, 1, 1),
            'End': datetime(2015, 1, 1)
        },
        'CalculatedSpend': {
            'ActualSpend': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'ForecastedSpend': {
                'Amount': 'string',
                'Unit': 'string'
            }
        },
        'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
        'LastUpdatedTime': datetime(2015, 1, 1),
        'AutoAdjustData': {
            'AutoAdjustType': 'HISTORICAL'|'FORECAST',
            'HistoricalOptions': {
                'BudgetAdjustmentPeriod': 123,
                'LookBackAvailablePeriods': 123
            },
            'LastAutoAdjustTime': datetime(2015, 1, 1)
        }
    },
    NotificationsWithSubscribers=[
        {
            'Notification': {
                'NotificationType': 'ACTUAL'|'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                'Threshold': 123.0,
                'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                'NotificationState': 'OK'|'ALARM'
            },
            'Subscribers': [
                {
                    'SubscriptionType': 'SNS'|'EMAIL',
                    'Address': 'string'
                },
            ]
        },
    ]
)
