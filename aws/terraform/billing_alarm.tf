resource "aws_cloudwatch_metric_alarm" "my_budget_alarm" {
  alarm_name = "my_budget_alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods = 1
  metric_name = "BudgetedCost"
  namespace = "AWS/Budgets"
  period = 86400
  statistic = "Maximum"
  threshold = 80
  alarm_description = "Alarm when budget exceeds 80% of limit"
  alarm_actions = [aws_sns_topic.my_sns_topic.arn]
}