# 🔭 Observability Layer (Space SRE Lab)

This folder contains **documentation-first** observability assets for the Space SRE Lab.

## Goals
- Measure the **Golden Signals**: traffic, latency, errors, saturation
- Provide interview-ready examples of:
  - Prometheus recording/alert rules
  - Grafana dashboard structure
  - Centralized logging (Loki) + log shipping (Vector)
- Keep it **safe**: configs are designed to be deployable later, but are valuable for review today.

## What’s Included
- `prometheus/` – sample rules (fast/slow burn patterns)
- `grafana/` – dashboard JSON stub showing what panels would exist
- `loki/` – example Loki config skeleton
- `vector/` – example Vector pipeline skeleton

> Note: This repo is a learning-focused lab. These configs are designed to support interview discussion and gradual adoption (local → k8s).
