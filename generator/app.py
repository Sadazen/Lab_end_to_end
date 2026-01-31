import time
import random
from prometheus_client import start_http_server, Counter, Histogram


requests_total = Counter("requests_total", "Total requests")
errors_total = Counter("errors_total", "Total errors")
request_latency = Histogram("request_latency_seconds", "Request latency")
start_http_server(8000)
print("generator start")

#нагрузка
while True:
    latency = random.uniform(0.05, 1.5)
    is_error = random.random() < 0.1           # 10% ошибок

    requests_total.inc()
    request_latency.observe(latency)
    if is_error:
        errors_total.inc()

    #раз в минутуимитация пиковых нагрузок ()
    if random.random() < 0.05:
        print("peak load simulated")
        time.sleep(random.uniform(2, 4))

    time.sleep(random.uniform(0.1, 0.5))
