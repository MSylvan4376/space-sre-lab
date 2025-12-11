terraform {
  required_version = ">= 1.4.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "network" {
  source   = "./modules/network"
  vpc_cidr = "10.42.0.0/16"
  region   = var.region
}

module "eks" {
  source             = "./modules/eks"
  cluster_name       = var.cluster_name
  vpc_id             = module.network.vpc_id
  private_subnet_ids = module.network.private_subnet_ids
}
