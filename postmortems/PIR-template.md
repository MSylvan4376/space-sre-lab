# 🧾 Post-Incident Review (PIR) Template — Space SRE Lab

> **Goal:** A blameless, systems-focused review that captures impact, root cause,
> and concrete reliability improvements.

---

## 1) Incident Summary
- **Incident ID:** (e.g., PIR-2025-12-11-01)
- **Date/Time (Start–End):**
- **Duration:**
- **Severity (SEV):** SEV-1 / SEV-2 / SEV-3
- **Services Affected:** groundstation-api, observability, etc.
- **Primary Symptom:** (5xx spike, high latency, outage, HPA runaway)
- **Detection Source:** (Alert / User report / Dashboard / On-call)

---

## 2) Customer / Mission Impact
- **Who was impacted:** (users, internal systems, downstream dependencies)
- **What they experienced:** (timeouts, errors, degraded performance)
- **Estimated scope:** (%, regions, time window, key endpoints)
- **SLO Impact:** (error budget burn, SLO miss Y/N)

---

## 3) Timeline (UTC)
| Time | Event |
|------|------|
|      | Detection (alert fired / report received) |
|      | Initial triage started |
|      | Mitigation action(s) taken |
|      | Service stabilized |
|      | Full recovery confirmed |
|      | Incident closed |

---

## 4) Root Cause
### Direct Cause
What directly caused the failure? (e.g., misconfigured resource limits, bad deploy, dependency outage)

### Contributing Factors
- Missing/insufficient alerts
- Capacity constraints
- Risky release process
- Documentation gaps
- Configuration drift

### Why It Wasn’t Prevented
Which safeguard should have caught this (tests, canary, SLO alerting, policy) and why it didn’t.

---

## 5) Detection & Diagnosis
- **Which alerts fired:** (name, threshold, signal quality)
- **Time to detect (TTD):**
- **Time to diagnose (TTDiag):**
- **Key signals used:** (Grafana panels, PromQL queries, logs)
- **What made diagnosis harder:** (noise, missing labels, lack of tracing)

---

## 6) Mitigation & Resolution
- **Mitigation steps taken:** (restart, rollback, scale, disable HPA, etc.)
- **Why those steps worked:**
- **Time to mitigate (TTM):**
- **Time to recover (TTR):**
- **Runbooks used:** (link to runbook file)

---

## 7) What Went Well
- Clear ownership / fast response
- Useful dashboards
- Rollback worked as designed
- Communication was timely

---

## 8) What Didn’t Go Well
- Alert fatigue / false positives
- Missing SLO coverage
- Manual steps required
- Unclear rollback criteria

---

## 9) Action Items (Most Important Section)
> Keep action items **specific, measurable, and owned**.

| Action Item | Owner | Priority | Due Date | Status |
|------------|-------|----------|----------|--------|
|            |       | P0/P1/P2 |          | Open/In Progress/Done |

---

## 10) Prevent Recurrence
- **Guardrails to add:** (policy, canary, limit ranges, better defaults)
- **Observability improvements:** (labels, dashboards, alerts, logs)
- **Reliability improvements:** (autoscaling tuning, retries, timeouts)

---

## 11) Links / Evidence
- Incident runbook:
- Grafana dashboard:
- Prometheus queries:
- Loki logs:
- Related PR/commit:
- Slack/notes:

---

## 12) Executive Summary (3–5 sentences)
Write a short, plain-English summary suitable for non-technical stakeholders.
