from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = FastAPI(title="Groundstation API")

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/livez")
def live():
    return {"status": "alive"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/telemetry")
def telemetry():
    start = time.time()

    # Simulated variable latency (for SLO demo)
    simulated_latency = random.uniform(0.05, 0.6)
    time.sleep(simulated_latency)

    latency = time.time() - start
    REQUEST_LATENCY.labels(endpoint="/telemetry").observe(latency)
    REQUEST_COUNT.labels(method="GET", endpoint="/telemetry", status="200").inc()

    return {"latency": latency, "message": "Telemetry packet received"}


@app.get("/load/cpu")
def cpu_load(seconds: float = 1.0):
    """Generate bounded CPU pressure for local reliability testing."""
    seconds = max(0.1, min(seconds, 10.0))
    start = time.perf_counter()
    iterations = 0

    while time.perf_counter() - start < seconds:
        # Intentional CPU work for HPA/failure-injection testing.
        _ = sum(i * i for i in range(10_000))
        iterations += 1

    duration = time.perf_counter() - start
    REQUEST_LATENCY.labels(endpoint="/load/cpu").observe(duration)
    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/load/cpu",
        status="200",
    ).inc()

    return {
        "status": "completed",
        "duration_seconds": duration,
        "iterations": iterations,
    }
