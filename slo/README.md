# 🎯 SLIs & SLOs (Space SRE Lab)

This folder documents **reliability goals** for the groundstation-api service.

## Example SLOs
### Availability / Success Rate (API)
- **SLI:** 1 - (5xx responses / total responses)
- **SLO:** 99.5% success rate over 30 days

### Latency
- **SLI:** p95 request latency for /telemetry
- **SLO:** p95 < 750ms over 30 days

## Alerting Philosophy
- Prefer **burn-rate alerts** (fast/slow) over raw threshold spam.
- Alerts should map to **user impact**, not internal noise.
- Runbooks must exist for paging alerts.
