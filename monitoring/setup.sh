#!/bin/bash

# Update system packages
sudo yum update -y

# Install Docker
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chkconfig docker on

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Create monitoring directories
sudo mkdir -p /opt/monitoring/{prometheus,grafana}
sudo mkdir -p /opt/monitoring/prometheus/{data,config}
sudo mkdir -p /opt/monitoring/grafana/data

# Set permissions
sudo chown -R 65534:65534 /opt/monitoring/prometheus/data
sudo chown -R 472:472 /opt/monitoring/grafana/data

echo "Installation completed. Docker and directories are ready for monitoring setup."