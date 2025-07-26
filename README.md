## 1. Objective
Set up system and Docker monitoring using:
```
  - Docker Compose
  - Prometheus
  - Grafana
  - Node Exporter
  - cAdvisor
```
## 2. Docker Compose Setup
We created a docker-compose.yaml file to run all services together.
Services added:
```
  - Grafana → Visual dashboard at port 3000
  - Prometheus → Metrics database at port 9090
  - Node Exporter → Collects system metrics
  - cAdvisor → Collects container metrics (uses port 8080, later changed)
```
## 3. Prometheus Configuration
We created a prometheus.yml file with targets

## 4. Grafana Dashboard Setup
```
  - Opened http://localhost:3000
    - Logged in with default admin / admin
    - Added Prometheus as the data source
    - Imported prebuilt dashboards from Grafana dashboards site
    - Example ID for Docker Monitoring: 193
```
## 5. Metrics Being Monitored
```
  - System metrics via Node Exporter:
      - CPU
      - memory
      - disk usage
```
```
  - Docker container metrics via cAdvisor:
      - Container
      - CPU/memory
      - usage
      - I/O
      - restarts
```
## 6. Key Learnings
```
- How to link multiple monitoring tools using Docker Compose
- Common container port conflicts and how to resolve
- Prometheus target configuration
- Grafana dashboard creation and troubleshooting
```
```
Thank You
```
