# Space SRE Lab – Terraform EKS Environment

This folder contains the Terraform configuration for the **Space SRE Lab** AWS environment.  
It is designed as a **learning-focused EKS lab**, not as production infrastructure.

The goal is to demonstrate how I would model:

- A VPC with private subnets across multiple AZs  
- An EKS cluster with a managed node group  
- IAM roles for the EKS control plane and worker nodes  
- Clean module boundaries between **network** and **cluster**  

---

## 🏗️ Architecture Overview

### **VPC**
- CIDR: `10.42.0.0/16`
- Two private subnets (AZ-a and AZ-b)

### **EKS Cluster**
- Kubernetes version: configurable (default `1.29`)
- Managed node group (t3.medium, 2–4 nodes)
- IAM roles for:
  - `eks_cluster_role`
  - `eks_node_role`

### **Terraform Outputs**
- VPC ID  
- Private subnet IDs  
- EKS cluster name  
- Cluster endpoint  
- Certificate authority data  
- Node group name  

---

## 📁 File Layout

infra/terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars.example
└── modules/
├── network/
│ ├── main.tf
│ └── variables.tf
└── eks/
└── main.tf


---

## 🧪 Usage (Safe Lab Mode)

This lab is **not meant to be applied by default**.  
It exists to demonstrate how I structure Terraform for AWS/EKS and to support technical discussions during interviews.  
All examples below operate in **non-destructive “plan-only” mode**, ensuring no AWS resources are created.

You can safely run the following Terraform commands:

```bash
terraform init
terraform validate
terraform plan -var-file="terraform.tfvars.example"
```

> These commands help validate the structure, variables, and module wiring of the
> lab environment without provisioning any infrastructure. This is the recommended
> mode for interview review and exploration.
