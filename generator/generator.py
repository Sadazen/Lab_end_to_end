import time
import json
import random
from datetime import datetime
import redis
from prometheus_client import start_http_server, Counter, Gauge

r = redis.Redis(host="redis", port=6379, decode_responses=True)

events_counter = Counter("generated_events_total", "Total events generated")
latency_gauge = Gauge("latency_ms", "Latency of last event in ms")
anomaly_counter = Counter("anomalies_total", "Total anomalies detected")

start_http_server(8000)

MODES = ["normal", "peak", "anomaly"]

while True:
    mode = random.choices(MODES, weights=[0.7, 0.2, 0.1])[0]
    if mode == "normal":
        latency = random.uniform(50, 150)
    elif mode == "peak":
        latency = random.uniform(200, 400)
    else:
        latency = random.uniform(600, 1000)

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "service": "payments",
        "latency": latency,
        "mode": mode
    }
    r.rpush("events", json.dumps(event))

    events_counter.inc()
    latency_gauge.set(latency)
    if latency > 500:
        anomaly_counter.inc()


        
    time.sleep(1)
