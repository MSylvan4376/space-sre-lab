# 🧭 Runbook: Deployment Rollback – Space SRE Lab

## Purpose
This runbook describes how to safely **roll back a faulty deployment**
of the `groundstation-api` service when a recent release causes errors,
latency spikes, or instability.

---

## Symptoms / Alerts
- Elevated 5xx error rate after deployment
- Sudden increase in latency
- Pods restarting or failing readiness checks
- Alerts triggered immediately following a release

---

## Severity
- **SEV-2** – Service degraded
- **SEV-1** – Service unavailable

---

## Initial Triage

### Confirm recent rollout
```bash
kubectl rollout history deploy/groundstation-api -n groundstation
