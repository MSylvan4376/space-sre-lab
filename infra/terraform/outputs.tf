########################################
# Top-level Terraform Outputs
########################################

output "vpc_id" {
  description = "ID of the created VPC"
  value       = module.network.vpc_id
}

output "private_subnet_ids" {
  description = "Private subnet IDs used by EKS nodes"
  value       = module.network.private_subnet_ids
}

output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "EKS API server endpoint"
  value       = module.eks.cluster_endpoint
}

output "cluster_certificate_authority_data" {
  description = "CA data for configuring kubectl access"
  value       = module.eks.cluster_certificate_authority_data
}

output "node_group_name" {
  description = "Name of the default managed node group"
  value       = module.eks.node_group_name
}
