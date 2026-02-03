# End-to-End Data Monitoring System (Without DATABASE)

## Description
The project is a minimal data generation and analysis system that simulates the operation of a production system.  
The system generates events, collects metrics using Prometheus, and visualizes them in Grafana.  

## Architecture
- Data generator (Python) — creates random events and errors
- Prometheus — collecting metrics from the generator
- Grafana — visualization and analysis of metrics in real time
