# Space SRE Lab

This repository is a hands-on Site Reliability Engineering lab that showcases how I design and operate
reliable cloud infrastructure and applications.
## 🚀 Space SRE Platform Architecture

```markdown
```mermaid
flowchart LR

  %% Developer
  subgraph Dev["Developer Workflow"]
    A[Code change]
    B[Git push (main)]
    A --> B
  end

  %% CI
  subgraph CI["GitHub Actions - CI pipeline"]
    C[Build Docker image]
    D[Tag latest and SHA]
    E[Push image]
    C --> D --> E
  end

  %% Registry
  subgraph REG["GitHub Container Registry (GHCR)"]
    F[(groundstation-api:latest)]
  end

  %% AWS + EKS
  subgraph AWS["AWS (Terraform)"]
    subgraph VPC["VPC (private subnets)"]
      G1["Private subnet AZ-a"]
      G2["Private subnet AZ-b"]
    end

    subgraph EKS["EKS cluster"]
      H1[EKS control plane]
      H2["Managed node group\n2-4 nodes"]
      H1 --> H2
    end
  end

  %% Kubernetes
  subgraph K8S["Kubernetes layer"]
    I["Deployment: groundstation-api"]
    J["Service: ClusterIP"]
    K["HPA: 3-8 pods (CPU)"]
    I --> J
    I --> K
  end

  %% Observability
  subgraph OBS["Observability"]
    L["Prometheus (scrape /metrics)"]
    M["Grafana dashboards"]
    N["Logging (Loki / Vector)"]
  end

  %% SRE
  subgraph SRE["SRE layer"]
    O["SLOs and error budgets"]
    P["Alert rules"]
    Q["Runbooks and incident response"]
  end

  %% Wiring
  B --> C
  E --> F
  F --> I
  H2 --> I
  I --> L
  L --> M
  I --> N
  L --> O
  O --> P
  P --> Q

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
