# 🧭 Runbook: Traffic Spike / HPA Runaway — Space SRE Lab

## Purpose
Respond to sudden traffic increases that trigger aggressive scaling (HPA runaway),
causing instability (thrashing), saturation, and elevated latency/errors.

---

## Symptoms / Alerts
- Rapidly increasing replicas (HPA scales up repeatedly)
- CPU throttling / high CPU usage on nodes
- Latency p95 climbs; 5xx errors increase
- Cluster capacity warnings; pending pods
- Cost spike (in real environments)

---

## Severity
- **SEV-2** Degraded performance
- **SEV-1** Outage / sustained errors

---

## Initial Triage (First 5–10 Minutes)

### Confirm HPA behavior
```bash
kubectl get hpa -n groundstation
kubectl describe hpa groundstation-api -n groundstation

---

## Follow-Up (PIR Required)

- Was this expected traffic? If not: add limits, rate limiting, or WAF rules
- Tune HPA targets and scale-up/down policies
- Add burn-rate alerts and improve dashboards
- Add load test and capacity planning notes

> Note: `kubectl` commands assume an active Kubernetes context.
> This lab is intentionally cluster-agnostic; commands are included
> as runbook guidance for interview discussion.
