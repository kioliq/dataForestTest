variable "region" {
  type    = string
  default = "us-east-1"
}

variable "project" {
  type    = string
  default = "dataforest-test"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "instance_type" {
  type    = string
  default = "t3.small"
}

variable "repo_url" {
  description = "Repo that will be cloned using user_data"
  type        = string
  default     = "https://github.com/kioliq/dataForestTest.git"
}
