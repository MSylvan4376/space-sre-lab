variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region for the cluster"
}

variable "cluster_name" {
  type        = string
  default     = "space-sre-eks"
  description = "Name of the EKS cluster"
}
