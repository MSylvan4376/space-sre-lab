#!/usr/bin/env python3
"""
Example script that queries Prometheus for a simple success-rate SLO.

In a real setup this could run as a CronJob, Lambda, or be integrated into
an internal reliability dashboard.
"""

import requests
import sys

PROMETHEUS_URL = "http://prometheus.groundstation.svc.cluster.local:9090"
QUERY = 'sum(rate(http_requests_total{status!~"5.."}[5m])) / sum(rate(http_requests_total[5m]))'

def main():
  try:
    r = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": QUERY}, timeout=5)
    r.raise_for_status()
  except Exception as e:
    print(f"Error talking to Prometheus: {e}")
    sys.exit(1)

  body = r.json()
  result = body.get("data", {}).get("result", [])
  if not result:
    print("No SLO data returned")
    sys.exit(1)

  value = float(result[0]["value"][1])
  print(f"SLO success rate (5m): {value:.4f}")

  if value < 0.99:
    print("SLO BREACH – this would trigger alerting/incident flow.")
    sys.exit(2)

  print("SLO OK")
  sys.exit(0)

if __name__ == "__main__":
  main()
