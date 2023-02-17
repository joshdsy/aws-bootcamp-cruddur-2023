resource "aws_sns_topic" "my_sns_topic" {
  name = "my_sns_topic"
}

resource "aws_sns_topic_subscription" "my_sns_subscription" {
  topic_arn = aws_sns_topic.my_sns_topic.arn
  protocol = "email"
  endpoint = "johndoe@example.com"
}