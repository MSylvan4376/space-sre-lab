# Incident 001: CPU Saturation and HPA Response

## Overview

This controlled reliability exercise tested how the Groundstation API and Kubernetes Horizontal Pod Autoscaler (HPA) respond to sustained CPU saturation.

The objective was to verify that CPU pressure above the configured HPA target causes automatic scale-out and that the workload returns to its minimum replica count after the pressure is removed.

No production systems were involved. The exercise ran against the local Space SRE Lab Kubernetes environment.

## Environment

- Application: `groundstation-api`
- Namespace: `groundstation`
- Kubernetes: Docker Desktop
- Metrics source: Kubernetes Metrics Server
- HPA metric: CPU utilization
- HPA target: 60%
- Minimum replicas: 3
- Maximum replicas: 8
- Tested application commit: `37106c5726c38dae01f1288068f2dc62b1a81e1b`
- GitHub Actions run: `35492873496`
- Container image: `ghcr.io/msylvan4376/groundstation-api:37106c5726c38dae01f1288068f2dc62b1a81e1b`

## Pre-Incident Baseline

Before introducing CPU pressure:

| Metric | Observed state |
| --- | --- |
| Ready replicas | 3/3 |
| Pod restarts | 0 |
| CPU per pod | 7-8m |
| HPA CPU utilization | 6% |
| HPA CPU target | 60% |
| Memory per pod | 46-49 MiB |
| HPA replicas | 3 |

The application health endpoints were responding successfully and the `/load/cpu` endpoint was verified from inside the Kubernetes service path.

## Failure Injection

A bounded `/load/cpu` endpoint was added to the Groundstation API specifically for controlled reliability testing.

Local validation showed the container increasing from approximately 0.3-0.4% CPU at idle to approximately 100% CPU under concurrent requests, then returning to approximately 0.3-0.4% after the requests completed.

For the Kubernetes exercise, sustained concurrent requests were sent to:

```text
/load/cpu?seconds=10
```

Now paste this:

````markdown
```

The load was maintained for approximately three minutes.

## Detection and HPA Response

The HPA detected CPU resource utilization above its configured 60% target.

Kubernetes HPA events recorded the following scale-out sequence:

```text
3 replicas
    |
    | CPU utilization above target
    v
5 replicas
    |
    | CPU utilization remained above target
    v
8 replicas
```

Eight replicas was the configured maximum.

The HPA controller recorded `SuccessfulRescale` events with CPU resource utilization above target as the reason for increasing the replica count.

## Recovery

After the CPU load stopped, application CPU utilization returned below the HPA target.

The HPA automatically reduced the workload:

```text
8 replicas
    |
    | metrics below target
    v
3 replicas
```

No manual scaling, pod deletion, or deployment restart was used during recovery.

Final observed state:

| Metric | Recovered state |
| --- | --- |
| Ready replicas | 3/3 |
| Pod restarts | 0 |
| CPU per pod | 6-7m |
| HPA CPU utilization | 6% |
| HPA CPU target | 60% |
| Memory per pod | 46-49 MiB |
| HPA replicas | 3 |

The HPA condition returned to `ScalingLimited=True` with `TooFewReplicas`, indicating that the calculated replica requirement had fallen below the configured minimum of three replicas.

## Timeline

1. Established healthy baseline at 3 replicas and approximately 6% HPA CPU utilization.
2. Verified the SHA-tagged application image in Kubernetes.
3. Started sustained concurrent requests against `/load/cpu`.
4. HPA detected CPU utilization above the 60% target.
5. HPA scaled the deployment from 3 to 5 replicas.
6. Continued CPU pressure caused the HPA to scale from 5 to the maximum of 8 replicas.
7. CPU load ended.
8. Metrics fell below the HPA target.
9. HPA automatically returned the deployment from 8 to the minimum of 3 replicas.
10. All remaining pods were healthy with zero restarts.

## Troubleshooting During Validation

During initial validation, the HPA reported CPU utilization as `<unknown>` because the local Kubernetes cluster did not have a functioning Resource Metrics API.

The issue was isolated by checking the Metrics API and HPA events. Metrics Server was installed, but its initial pod could not scrape the Docker Desktop Kubernetes node because kubelet certificate verification failed for the node IP.

For this local lab environment, Metrics Server was configured with `--kubelet-insecure-tls`. After the deployment rolled out successfully:

- `v1beta1.metrics.k8s.io` reported `Available=True`
- `kubectl top pods -n groundstation` returned CPU and memory metrics
- The HPA reported valid CPU utilization
- `ScalingActive=True` with reason `ValidMetricFound`

This restored the telemetry path required by the HPA before the CPU saturation exercise continued.

> The `--kubelet-insecure-tls` setting was used only to accommodate the certificate behavior of this local Docker Desktop lab. It is not presented here as a production Kubernetes configuration.

## Findings

### What worked

- Metrics Server supplied CPU utilization to the HPA.
- CPU pressure was sufficient to cross the configured scaling threshold.
- HPA scale-out occurred without manual intervention.
- The workload reached the configured maximum of eight replicas under sustained pressure.
- HPA scale-down occurred automatically after pressure was removed.
- The application returned to its original three-replica baseline.
- No pod restarts were observed during the exercise.

### Operational observations

CPU measurements captured after the load ended were approximately 6-7%. Those values represent the recovery state and should not be interpreted as CPU utilization during peak saturation.

The HPA event history provides the authoritative evidence that CPU resource utilization exceeded the configured target during scale-out.

## Evidence

Relevant commands used during the exercise included:

```bash
kubectl get hpa -n groundstation
kubectl get pods -n groundstation
kubectl top pods -n groundstation
kubectl describe hpa groundstation-api-hpa -n groundstation
```

The HPA event history recorded:

```text
SuccessfulRescale  New size: 5; reason: cpu resource utilization (percentage of request) above target
SuccessfulRescale  New size: 8; reason: cpu resource utilization (percentage of request) above target
SuccessfulRescale  New size: 3; reason: All metrics below target
```

## Outcome

The experiment validated the intended autoscaling behavior of the Groundstation API under CPU saturation.

The service moved from its healthy three-replica baseline to the configured eight-replica maximum under sustained CPU pressure and returned automatically to three replicas after the load was removed.

This exercise demonstrated detection, automated mitigation, and recovery without manual scaling intervention.
