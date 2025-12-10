# Space SRE Lab

This repository is a hands-on Site Reliability Engineering lab that showcases how I design and operate
reliable cloud infrastructure and applications.

It includes:

- **Groundstation API** – a FastAPI-based demo service with `/healthz`, `/livez`, `/telemetry`, and `/metrics`,
  including Prometheus instrumentation.
- Skeleton structure for:
  - **Terraform-based AWS infrastructure** (`infra/terraform`)
  - **Kubernetes workloads** (`k8s/`)
  - **Observability stack** (`observability/`)
  - **Service Level Objectives (SLOs)** (`slo/`)
  - **Runbooks for incident response** (`runbooks/`)
  - **CI/CD configuration** (`ci-cd/`)
  - **Utilities & scripts** (`scripts/`)

This repo serves as a portfolio project demonstrating my SRE approach:
infrastructure as code, observability, SLO-based reliability, and automation for mission-critical systems.
