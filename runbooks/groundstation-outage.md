# 🛰️ Runbook: Groundstation API Outage – Space SRE Lab

## 1. Purpose
This runbook documents the response to a **complete or near-complete outage**
of the `groundstation-api` service.

It focuses on restoring service quickly while maintaining clear operational
decision-making.

---

## 2. Symptoms / Alerts
- API unreachable (timeouts or connection refused)
- 5xx error rate near 100%
- No successful telemetry ingestion
- Prometheus reports target down
- Kubernetes readiness probes failing across all pods

---

## 3. Severity
- **SEV-1** – Full service outage

---

## 4. Initial Triage (First 5 Minutes)

### Confirm outage
```bash
curl -sSf http://<endpoint>/healthz || echo "Service unreachable"
