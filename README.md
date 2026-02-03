# End-to-End Data Monitoring System 

## Description
The project is a minimal data generation and analysis system that simulates the operation of a production system.  

## Architecture
- **Generator** — generates events with different intensity and modes:
  - `normal' — normal load
  - `peak' — peak load
  - `anomaly` — abnormal latency values
- **Redis** — event queuing and buffering between generator and consumer
- **Consumer** — reads events from Redis, performs:
- Data validation
- Saving to SQLite
  - Anomaly detection (`latency > 500`)
- **SQLite** — analytical storage, stores events and anomalies
- **Prometheus** — collects real-time generator metrics:
— `generated_events_total` - number of events
  - `latency_ms` — the latency value of the last event
  - `anomalies_total' — number of anomalies
- **Grafana** — visualization and analysis of metrics in interactive dashboards
