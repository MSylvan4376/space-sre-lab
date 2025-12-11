# Space SRE Lab

This repository is a hands-on Site Reliability Engineering lab that showcases how I design and operate
reliable cloud infrastructure and applications.
## 🚀 Space SRE Platform Architecture

```mermaid
flowchart LR

    subgraph Dev["Developer Workflow"]
        A[Code Change]
        B[Git Push - main]
        A --> B
    end

    subgraph CI["GitHub Actions - CI Pipeline"]
        C[Build Docker Image]
        D[Tag Latest + SHA]
        E[Push to GHCR]
        C --> D --> E
    end

    subgraph Registry["GitHub Container Registry (GHCR)"]
        F[(groundstation-api:latest)]
        E --> F
    end

    subgraph AWS["AWS Infrastructure (Provisioned via Terraform)"]
        
        subgraph VPC["VPC (Private Subnets)"]
            G1[Private Subnet (AZ A)]
            G2[Private Subnet (AZ B)]
        end

        subgraph EKS["EKS Cluster"]
            H1[EKS Control Plane]
            H2[Managed Node Group<br/>t3.medium (2–4 nodes)]
            H1 --> H2
        end
        
        VPC --> EKS
    end

    subgraph K8s["Kubernetes Layer"]
        I[Deployment: groundstation-api]
        J[Service (ClusterIP)]
        K[HPA: CPU-based auto-scaling 3–8 pods]
        I --> J
        I --> K
    end

    F --> I
    H2 --> I

    subgraph OBS["Observability Stack"]
        L[Prometheus<br/>Scrape /metrics]
        M[Grafana Dashboards<br/>SLO Visualization]
        N[Loki / Vector for Logging]
        I --> L
        L --> M
        I --> N
    end

    subgraph SRE["SRE Layer"]
        O[SLOs & Error Budget Policies]
        P[Alerting Rules<br/>Fast & Slow Burn Alerts]
        Q[Runbooks<br/>Incident Response]
        L --> O
        O --> P
        P --> Q
    end

It includes:

- **Groundstation API** – a FastAPI-based demo service that simulates a satellite/groundstation
  telemetry endpoint. It exposes:
  - `/healthz` – readiness probe
  - `/livez` – liveness probe
  - `/telemetry` – simulated telemetry calls with variable latency
  - `/metrics` – Prometheus-compatible metrics for requests and latency
- **Kubernetes manifests** (`k8s/`) to run the service on a cluster:
  - Namespace: `groundstation`
  - Deployment with probes and resource requests/limits
  - Service (ClusterIP)
  - Horizontal Pod Autoscaler (HPA) scaling between 3–8 replicas
- **Skeletons for SRE capabilities**:
  - Terraform-based AWS infrastructure (`infra/terraform`)
  - Observability stack configuration for Prometheus, Grafana, Loki, Vector (`observability/`)
  - Service Level Objectives (SLOs) (`slo/`)
  - Runbooks for incident response (`runbooks/`)
  - CI/CD configuration (`ci-cd/`)
  - Utility scripts (`scripts/`)

The goal of this repo is to demonstrate how I approach SRE work end-to-end:
from application instrumentation and Kubernetes deployment to observability, SLOs, and operational runbooks
for mission-critical systems such as groundstation or satellite communication services.

## Repo Structure

- `groundstation-api/` – application code + Dockerfile
- `k8s/` – Kubernetes Deployment, Service, HPA, Namespace
- `infra/` – (to be expanded) Terraform for AWS VPC/EKS and related infra
- `observability/` – Prometheus/Grafana/Loki/Vector configuration samples
- `slo/` – SLO definitions for key user journeys
- `runbooks/` – operational procedures for common failure modes
- `ci-cd/` – pipelines for build/publish/deploy
- `scripts/` – helper scripts (e.g., SLO checks)

This is not meant to be production-ready, but to be a conversation starter in interviews
about tradeoffs, design choices, and how I would extend and harden a real-world SRE platform.
