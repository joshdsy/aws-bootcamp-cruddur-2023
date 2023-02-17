resource "aws_budgets_budget" "my_budget" {
  budget_type = "COST"
  limit_amount = 100.0
  limit_unit = "USD"
  time_period_start = "2023-01-01_00:00"
  time_period_end = "2023-01-31_23:59"
  time_unit = "MONTHLY"

  // The following filters will track the costs of all Amazon S3 buckets
  cost_filters = {
    Service = "Amazon S3"
  }

  notification {
    threshold_percent = 80
    comparison_operator = "GREATER_THAN"
    notification_type = "FORECASTED"
    subscriber_email_addresses = ["johndoe@example.com"]
  }
}
