output "url" {
  value = "https://${aws_cloudfront_distribution.app.domain_name}"
}

output "instance_id" {
  value = aws_instance.app.id
}
