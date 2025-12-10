# Runbook: Groundstation API Pod in CrashLoopBackOff

## Symptoms
- `kubectl -n groundstation get pods` shows status `CrashLoopBackOff`
- Application never reaches Ready state

## First Checks
1. Describe one of the pods:
   `kubectl -n groundstation describe pod <pod-name>`
2. Check logs:
   `kubectl -n groundstation logs <pod-name> --previous`

## Common Causes
- Invalid configuration or missing secret.
- Application crash on startup due to bug or env mismatch.
- Image tag points to a broken build.

## Mitigation
- Fix config/secret and redeploy.
- Roll back to previous known-good image.
- If needed, scale replicas down to reduce noisy alerts while investigating.

## Post-Incident
- Add config validation or startup checks.
- Harden CI so broken builds don't get promoted.
- Update this runbook with the specific root cause and fix.
