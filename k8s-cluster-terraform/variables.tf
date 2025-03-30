variable "aws_access_key" {
  description = "Clé d'accès AWS"
  type        = string
  sensitive   = true
}

variable "aws_secret_access_key" {
  description = "Clé secrète AWS"
  type        = string
  sensitive   = true
}

variable "instance_type" {
  description = "Type de l'instance EC2"
  default     = "t2.micro"
}
