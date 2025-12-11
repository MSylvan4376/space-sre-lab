# 🧭 Runbook: Incident Response – Space SRE Lab

## 1. Purpose

This runbook defines a lightweight incident response process for the Space SRE Lab,
focusing on issues with the `groundstation-api` service and its supporting
Kubernetes/EKS infrastructure.

It is optimized for:
- Fast triage
- Clear communication
- Safe stabilization steps
- Actionable follow-up

---

## 2. Severity Levels (SEV)

- **SEV1 – Critical**
  - `groundstation-api` is down or returning 5xx for most traffic
  - No telemetry available for primary users
- **SEV2 – Major**
  - Elevated errors or latency outside SLOs, but partial functionality remains
- **SEV3 – Minor**
  - Degraded performance, non-critical feature impact, or noisy alerts

For this lab, SEV is mainly for *structure* and interview discussion.

---

## 3. Initial Triage (First 5–10 Minutes)

1. **Confirm impact**
   - Is the API reachable?
   - Are health endpoints returning OK?
     ```bash
     curl -sSf http://<endpoint>/healthz || echo "health check failed"
     ```

2. **Check Kubernetes status**
   ```bash
   kubectl get pods -n groundstation
   kubectl get hpa -n groundstation
   kubectl get nodes
```
**Check metrics (Prometheus)**

- **Request rate**
```promql
sum(rate(http_requests_total{service="groundstation-api"}[5m]))
```

- **Error rate**
```promql
sum(rate(http_requests_total{service="groundstation-api",status=~"5.."}[5m]))
```

- **Latency (p95)**
```promql
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{service="groundstation-api"}[5m])) by (le))
```

**Check logs (Loki)**

- Filter logs by:
  - `service="groundstation-api"`
  - Recent timestamp window
- Look for:
  - Stack traces
  - Timeouts
  - Dependency failures
  - Configuration errors

---

## 4. Stabilization Actions

> ⚠️ Prefer **reversible, low-risk actions** first.

### Restart deployment
```bash
kubectl rollout restart deploy/groundstation-api -n groundstation
``` 
