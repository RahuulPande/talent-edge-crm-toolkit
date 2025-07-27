# 🚀 Deployment Guide

## Cognizant Talent Edge CRM Toolkit - Production Deployment

### Table of Contents
- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Cloud Deployment](#cloud-deployment)
- [Environment Configuration](#environment-configuration)
- [Security Considerations](#security-considerations)
- [Monitoring & Maintenance](#monitoring--maintenance)
- [Troubleshooting](#troubleshooting)

---

## Pre-Deployment Checklist

### System Requirements
- ✅ **Python 3.9+** installed and configured
- ✅ **8GB RAM minimum** (16GB recommended for production)
- ✅ **2GB free disk space** for application and dependencies
- ✅ **Network access** to package repositories
- ✅ **Modern web browser** for administration
- ✅ **SSL certificate** (for production environments)

### Dependencies Verification
```bash
# Check Python version
python3 --version  # Should be 3.9 or higher

# Verify pip
python3 -m pip --version

# Check available disk space
df -h

# Verify network connectivity
curl -I https://pypi.org/simple/
```

### Security Prerequisites
- [ ] **Firewall configuration** with required ports
- [ ] **SSL/TLS certificates** for HTTPS
- [ ] **User access controls** defined
- [ ] **Backup strategy** established
- [ ] **Monitoring tools** configured

---

## Local Development

### Quick Start Development Setup
```bash
# Clone repository
git clone <repository-url>
cd CRM_APP

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
python3 -m pip install -r requirements.txt

# Verify installation
python3 -c "import streamlit; print(f'Streamlit {streamlit.__version__} ready')"

# Run application
python3 -m streamlit run app.py
```

### Development Configuration
Create `.streamlit/config.toml` for development settings:

```toml
[server]
port = 8501
address = "localhost"
headless = false
enableCORS = false
enableWebsocketCompression = false

[browser]
serverAddress = "localhost"
serverPort = 8501

[logger]
level = "debug"

[client]
showErrorDetails = true
```

### Environment Variables
```bash
# Development environment
export STREAMLIT_ENV="development"
export STREAMLIT_DEBUG="true"
export CACHE_TTL="300"  # 5 minutes for development
```

---

## Docker Deployment

### Production Dockerfile
```dockerfile
# Use official Python runtime as base image
FROM python:3.9-slim

# Set metadata
LABEL maintainer="talentedge@cognizant.com"
LABEL version="2.0"
LABEL description="Cognizant Talent Edge CRM Toolkit"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Create app user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership to app user
RUN chown -R appuser:appuser /app
USER appuser

# Create directories for data and logs
RUN mkdir -p /app/data /app/logs

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Expose port
EXPOSE 8501

# Run application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
```

### Docker Compose for Production
```yaml
version: '3.8'

services:
  talent-edge-crm:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: talent-edge-crm
    restart: unless-stopped
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - CACHE_TTL=3600
      - LOG_LEVEL=INFO
    volumes:
      - ./data:/app/data:rw
      - ./logs:/app/logs:rw
      - ./config:/app/config:ro
    networks:
      - talent-edge-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Optional: Reverse proxy for SSL termination
  nginx:
    image: nginx:alpine
    container_name: talent-edge-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      - talent-edge-crm
    networks:
      - talent-edge-network

networks:
  talent-edge-network:
    driver: bridge
```

### Building and Running
```bash
# Build the image
docker build -t talent-edge-crm:2.0 .

# Run with Docker Compose
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f talent-edge-crm

# Scale if needed
docker-compose up -d --scale talent-edge-crm=3
```

---

## Cloud Deployment

### AWS Deployment (ECS Fargate)

#### Task Definition
```json
{
  "family": "talent-edge-crm",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "1024",
  "memory": "2048",
  "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskRole",
  "containerDefinitions": [
    {
      "name": "talent-edge-crm",
      "image": "YOUR_ECR_URI/talent-edge-crm:2.0",
      "portMappings": [
        {
          "containerPort": 8501,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "STREAMLIT_SERVER_HEADLESS",
          "value": "true"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/talent-edge-crm",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "curl -f http://localhost:8501/_stcore/health || exit 1"
        ],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

#### Application Load Balancer
```bash
# Create target group
aws elbv2 create-target-group \
  --name talent-edge-crm-tg \
  --protocol HTTP \
  --port 8501 \
  --vpc-id vpc-xxxxxxxx \
  --target-type ip \
  --health-check-path "/_stcore/health"

# Create load balancer
aws elbv2 create-load-balancer \
  --name talent-edge-crm-alb \
  --subnets subnet-xxxxxxxx subnet-yyyyyyyy \
  --security-groups sg-xxxxxxxx
```

### Azure Deployment (Container Instances)

#### ARM Template
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "containerGroupName": {
      "type": "string",
      "defaultValue": "talent-edge-crm"
    }
  },
  "resources": [
    {
      "type": "Microsoft.ContainerInstance/containerGroups",
      "apiVersion": "2021-03-01",
      "name": "[parameters('containerGroupName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "containers": [
          {
            "name": "talent-edge-crm",
            "properties": {
              "image": "youracr.azurecr.io/talent-edge-crm:2.0",
              "ports": [
                {
                  "port": 8501,
                  "protocol": "TCP"
                }
              ],
              "environmentVariables": [
                {
                  "name": "STREAMLIT_SERVER_HEADLESS",
                  "value": "true"
                }
              ],
              "resources": {
                "requests": {
                  "cpu": 1,
                  "memoryInGb": 2
                }
              }
            }
          }
        ],
        "ipAddress": {
          "type": "Public",
          "ports": [
            {
              "protocol": "TCP",
              "port": 8501
            }
          ]
        },
        "osType": "Linux"
      }
    }
  ]
}
```

### Google Cloud Platform (Cloud Run)

#### Deployment Configuration
```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: talent-edge-crm
  annotations:
    run.googleapis.com/ingress: all
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/maxScale: "10"
        run.googleapis.com/cpu-throttling: "false"
    spec:
      containerConcurrency: 100
      timeoutSeconds: 300
      containers:
      - image: gcr.io/PROJECT_ID/talent-edge-crm:2.0
        ports:
        - containerPort: 8501
        env:
        - name: STREAMLIT_SERVER_HEADLESS
          value: "true"
        resources:
          limits:
            cpu: 1000m
            memory: 2Gi
```

---

## Environment Configuration

### Production Environment Variables
```bash
# Application settings
export STREAMLIT_ENV="production"
export STREAMLIT_SERVER_HEADLESS="true"
export STREAMLIT_SERVER_PORT="8501"
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"

# Performance settings
export CACHE_TTL="7200"  # 2 hours
export MAX_UPLOAD_SIZE="200"
export ENABLE_PERFORMANCE_MONITORING="true"

# Security settings
export ENABLE_INPUT_VALIDATION="true"
export LOG_USER_ACTIONS="true"
export MAX_QUERY_LENGTH="500"

# Data settings
export DEFAULT_ASSOCIATE_COUNT="2150"
export DATA_REFRESH_INTERVAL="3600"

# Logging
export LOG_LEVEL="INFO"
export LOG_FORMAT="structured"
```

### Streamlit Production Config
Create `.streamlit/config.toml`:

```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true
enableCORS = false
enableWebsocketCompression = true
maxUploadSize = 200

[browser]
gatherUsageStats = false

[logger]
level = "info"

[client]
showErrorDetails = false
toolbarMode = "minimal"

[theme]
primaryColor = "#0072C6"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

---

## Security Considerations

### Network Security
```bash
# Firewall rules for production
# Allow HTTP/HTTPS only
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw deny 8501/tcp  # Don't expose Streamlit port directly

# For Docker environments
docker run -p 127.0.0.1:8501:8501 talent-edge-crm:2.0  # Bind to localhost only
```

### SSL/TLS Configuration
#### Nginx SSL Proxy
```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

### Access Control
```python
# Add to app.py for basic authentication
import os
import hashlib

def check_password():
    """Simple password protection for production"""
    def password_entered():
        if hashlib.sha256(st.session_state["password"].encode()).hexdigest() == os.getenv("APP_PASSWORD_HASH"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Password incorrect")
        return False
    else:
        return True

# Use in production
if os.getenv("STREAMLIT_ENV") == "production":
    if not check_password():
        st.stop()
```

---

## Monitoring & Maintenance

### Health Monitoring
```python
# Add health check endpoint
@st.cache_data
def health_check():
    """Simple health check"""
    try:
        # Check data generation
        df = create_streamlit_dataset()
        if len(df) == 0:
            return False
        
        # Check memory usage
        import psutil
        memory_percent = psutil.virtual_memory().percent
        if memory_percent > 90:
            return False
        
        return True
    except Exception:
        return False
```

### Logging Configuration
```python
import logging
import json
from datetime import datetime

# Production logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/app.log'),
        logging.StreamHandler()
    ]
)

def log_user_action(action, details):
    """Log user actions for monitoring"""
    log_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'action': action,
        'details': details,
        'user_agent': st.experimental_get_query_params().get('user_agent'),
        'ip': st.experimental_get_query_params().get('client_ip')
    }
    logging.info(f"USER_ACTION: {json.dumps(log_data)}")
```

### Performance Monitoring
```bash
# Docker stats monitoring
docker stats talent-edge-crm

# Resource usage monitoring
#!/bin/bash
# monitor.sh
while true; do
    echo "$(date): Memory: $(free -m | awk 'NR==2{printf "%.2f%%\t", $3*100/$2 }')"
    echo "$(date): CPU: $(top -bn1 | grep load | awk '{printf "%.2f%%\t\n", $(NF-2)}')"
    sleep 60
done >> /var/log/app-monitor.log
```

### Backup Strategy
```bash
#!/bin/bash
# backup.sh - Daily backup of application data

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/talent-edge-crm"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup application data
tar -czf $BACKUP_DIR/app-data-$DATE.tar.gz /app/data

# Backup logs
tar -czf $BACKUP_DIR/app-logs-$DATE.tar.gz /app/logs

# Keep only last 7 days of backups
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed: $DATE"
```

---

## Troubleshooting

### Common Production Issues

#### 1. Application Won't Start
```bash
# Check logs
docker logs talent-edge-crm

# Check port availability
netstat -tlnp | grep 8501

# Verify dependencies
python3 -c "import streamlit, pandas, plotly; print('Dependencies OK')"
```

#### 2. High Memory Usage
```bash
# Monitor memory
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Restart container if needed
docker-compose restart talent-edge-crm
```

#### 3. SSL Certificate Issues
```bash
# Test SSL
openssl s_client -connect your-domain.com:443

# Verify certificate
openssl x509 -in /etc/nginx/ssl/cert.pem -text -noout
```

#### 4. Performance Issues
```python
# Enable profiling
import cProfile
import pstats

def profile_page_load():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your page logic
    create_streamlit_dataset()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)
```

### Rollback Procedure
```bash
# Quick rollback to previous version
docker-compose down
docker tag talent-edge-crm:2.0 talent-edge-crm:2.0-backup
docker tag talent-edge-crm:1.9 talent-edge-crm:2.0
docker-compose up -d

# Verify rollback
curl -f http://localhost:8501/_stcore/health
```

### Emergency Contacts
- **Primary Support**: talentedge@cognizant.com
- **Emergency Hotline**: +41 58 123 4567
- **Technical Lead**: Available 24/7 for critical issues
- **Infrastructure Team**: For cloud and network issues

---

**Last Updated**: January 2025  
**Version**: 2.0  
**Next Review**: April 2025 