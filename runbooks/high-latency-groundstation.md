# Runbook: High Latency on Groundstation API

## Symptoms
- p95 latency > 500ms for more than 10 minutes
- SLO burn alerts firing in Grafana/Prometheus
- Users or upstream systems reporting delayed telemetry

## First Checks
1. Confirm alert details and timeframe in Grafana.
2. Check HPA status:
   `kubectl -n groundstation get hpa groundstation-api-hpa`
3. Check pod resource usage:
   `kubectl -n groundstation top pods`
4. Check recent deploys (Git/ArgoCD/GitLab).

## Common Causes
- Insufficient replicas or CPU/memory limits too low.
- New release introducing a slow code path.
- Upstream dependency degradation (database, external API).
- Node-level resource contention or noisy neighbor.

## Mitigation
- Temporarily increase HPA maxReplicas or lower target CPU.
- Roll back to last known good deployment if a recent release correlates.
- If upstream dependency issue, engage owning team and update status.

## Post-Incident
- Capture timeline and key graphs.
- Update SLOs or thresholds if they don't match reality.
- Add regression tests or new alerts to cover the discovered failure mode.
