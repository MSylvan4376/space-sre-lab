# Space SRE Lab – Observability Layer

The observability layer for this lab is designed to show how I would monitor a
mission-critical service like a groundstation API using **metrics**, **logs**, and **dashboards**.

The goal is not to run a full production observability stack here, but to show
how I would structure Prometheus, Grafana, Loki, and Vector configurations and
how they tie back to SRE concepts like **SLIs**, **SLOs**, and **error budgets**.

---

## Components

- **Prometheus**
  - Scrapes metrics from the `groundstation-api` at `/metrics`
  - Can be extended to scrape Kubernetes pods or services
  - Uses recording rules and alerting rules for latency and error-rate SLOs

- **Grafana**
  - Dashboards for request rate, error rate, latency percentiles, and saturation
  - Visualizes SLO burn rate and error budget consumption

- **Loki + Vector**
  - Vector agents ship logs to Loki
  - Loki stores and indexes logs for correlation with metrics
  - Used to drill into error spikes or latency anomalies

---

## How It Fits Together

1. **groundstation-api** exposes:
   - `/metrics` (Prometheus format)
   - `/healthz` and `/livez` for readiness/liveness

2. **Prometheus** scrapes `/metrics` and evaluates:
   - Request rate and error rate
   - Latency distributions (p90, p95, p99)
   - SLO-related burn-rate alerts

3. **Grafana** visualizes:
   - Golden signals: latency, traffic, errors, saturation
   - SLO status and error budget remaining

4. **Loki** receives logs (optionally via Vector):
   - Application logs
   - Kubernetes pod logs (if deployed on EKS)
   - Used for root cause analysis during incidents

5. **SRE Practices**
   - SLIs: request_success_ratio, latency under threshold
   - SLOs: e.g., 99% of requests under 500ms over 30 days
   - Alerts: fast burn / slow burn detection
   - Runbooks: documented procedures for common failure modes

This folder is meant to be a **conversation starter** in interviews about how I
design observability for a real system, not just how to read metrics from a toy app.
