# Monitoring Setup Guide for Amazon Linux

## Prerequisites
- Amazon Linux instance
- Open ports: 8000 (Backend), 80 (Frontend), 9090 (Prometheus), 3000 (Grafana), 9100 (Node Exporter), 8080 (cAdvisor)

## Installation Steps

1. Clone the repository and navigate to monitoring directory:
```bash
git clone https://github.com/sanketgandhi12/fusionpact-devops-challenge.git
cd fusionpact-devops-challenge/monitoring
```

2. Make the setup script executable and run it:
```bash
chmod +x setup.sh
./setup.sh
```

3. Start the application containers:
```bash
cd ..
docker-compose up -d
```

4. Start the monitoring stack:
```bash
cd monitoring
docker-compose up -d
```

## Accessing Monitoring Tools

1. Prometheus:
   - URL: http://your-instance-ip:9090
   - Use the Prometheus UI to verify targets are being scraped
   - Check Status > Targets to ensure all endpoints are up

2. Grafana:
   - URL: http://your-instance-ip:3000
   - Default credentials:
     - Username: admin
     - Password: admin123
   - Dashboards are automatically provisioned

## Monitoring Components

1. Prometheus:
   - Scrapes metrics from:
     - Backend application (/metrics endpoint)
     - Node Exporter (system metrics)
     - cAdvisor (container metrics)
     - Prometheus itself

2. Grafana Dashboards:
   - Infrastructure Dashboard:
     - CPU Usage
     - Memory Usage
     - Disk I/O
     - Network Traffic
   - Application Dashboard:
     - Request Rate
     - Response Time
     - Error Rate
     - Endpoint Usage

3. Node Exporter:
   - Collects system metrics:
     - CPU
     - Memory
     - Disk
     - Network

4. cAdvisor:
   - Collects container metrics:
     - Container CPU usage
     - Container memory usage
     - Network stats
     - Filesystem usage

## Metrics Available

1. Application Metrics (from FastAPI):
   - http_requests_total
   - http_request_duration_seconds
   - http_requests_in_progress

2. System Metrics (from Node Exporter):
   - node_cpu_seconds_total
   - node_memory_MemTotal_bytes
   - node_disk_io_time_seconds_total

3. Container Metrics (from cAdvisor):
   - container_cpu_usage_seconds_total
   - container_memory_usage_bytes
   - container_network_receive_bytes_total

## Troubleshooting

1. Check container status:
```bash
docker-compose ps
```

2. View container logs:
```bash
docker-compose logs prometheus
docker-compose logs grafana
```

3. Verify Prometheus targets:
```bash
curl http://localhost:9090/api/v1/targets
```

4. Check Node Exporter metrics:
```bash
curl http://localhost:9100/metrics
```

## Maintenance

1. Update monitoring stack:
```bash
docker-compose pull
docker-compose up -d
```

2. Backup Grafana:
```bash
docker run --rm --volumes-from grafana -v $(pwd):/backup alpine tar cvf /backup/grafana-backup.tar /var/lib/grafana
```

3. Backup Prometheus data:
```bash
docker run --rm --volumes-from prometheus -v $(pwd):/backup alpine tar cvf /backup/prometheus-backup.tar /prometheus
```