# 🚀 Deployment Guide

## Overview
This guide covers deploying the Cognizant Talent Edge CRM Toolkit to various cloud platforms.

## 📋 Pre-Deployment Checklist

### ✅ Prerequisites
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Application runs locally without errors
- [ ] Git repository initialized and code committed
- [ ] Environment variables configured (if needed)
- [ ] Database connections tested (if applicable)

### 🔧 Configuration Files
- [ ] `requirements.txt` - Python dependencies
- [ ] `runtime.txt` - Python version specification
- [ ] `.streamlit/config.toml` - Streamlit configuration
- [ ] `Procfile` - Process specification (for supported platforms)
- [ ] `setup.sh` - Setup script (for supported platforms)

## 🌐 Platform-Specific Deployment

### 1. Vercel Deployment (Recommended)

#### Quick Deploy
1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from your project directory**:
   ```bash
   vercel --prod
   ```

#### Manual Deployment Steps
1. **Connect your GitHub repository**:
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"
   - Import your `talent-edge-crm-toolkit` repository

2. **Configure build settings**:
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: `.`
   - **Install Command**: `pip install -r requirements.txt`

3. **Environment Variables** (if needed):
   ```
   STREAMLIT_SERVER_PORT=8501
   STREAMLIT_SERVER_ADDRESS=0.0.0.0
   STREAMLIT_SERVER_HEADLESS=true
   ```

4. **Deploy**:
   - Click "Deploy"
   - Wait for build completion
   - Access your live URL

#### Vercel Configuration Files

**vercel.json**:
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/app.py"
    }
  ],
  "functions": {
    "app.py": {
      "maxDuration": 30
    }
  },
  "env": {
    "STREAMLIT_SERVER_PORT": "8501",
    "STREAMLIT_SERVER_ADDRESS": "0.0.0.0",
    "STREAMLIT_SERVER_HEADLESS": "true",
    "STREAMLIT_SERVER_ENABLE_CORS": "false",
    "STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION": "false"
  }
}
```

**runtime.txt**:
```
python-3.9
```

### 2. Streamlit Cloud Deployment

#### Automatic Deployment
1. **Push to GitHub** (already done)
2. **Visit [share.streamlit.io](https://share.streamlit.io)**
3. **Sign in with GitHub**
4. **Select your repository**: `talent-edge-crm-toolkit`
5. **Configure deployment**:
   - **Main file path**: `app.py`
   - **Python version**: 3.9
6. **Deploy**

#### Streamlit Cloud Configuration
Create `.streamlit/config.toml`:
```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true
enableCORS = false
enableXsrfProtection = false
maxUploadSize = 200

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

### 3. Heroku Deployment

#### Prerequisites
1. **Install Heroku CLI**:
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

#### Deployment Steps
1. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

2. **Set buildpacks**:
   ```bash
   heroku buildpacks:set heroku/python
   ```

3. **Configure environment**:
   ```bash
   heroku config:set STREAMLIT_SERVER_PORT=8501
   heroku config:set STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

5. **Open the app**:
   ```bash
   heroku open
   ```

### 4. Docker Deployment

#### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Docker Compose
```yaml
version: '3.8'
services:
  streamlit-app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    volumes:
      - .:/app
```

#### Build and Run
```bash
# Build the image
docker build -t talent-edge-crm .

# Run the container
docker run -p 8501:8501 talent-edge-crm
```

### 5. AWS ECS Fargate Deployment

#### Prerequisites
- AWS CLI configured
- Docker image built and pushed to ECR
- ECS cluster created

#### Deployment Steps
1. **Create ECR repository**:
   ```bash
   aws ecr create-repository --repository-name talent-edge-crm
   ```

2. **Build and push Docker image**:
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
   docker build -t talent-edge-crm .
   docker tag talent-edge-crm:latest $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/talent-edge-crm:latest
   docker push $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/talent-edge-crm:latest
   ```

3. **Create ECS task definition**:
   ```json
   {
     "family": "talent-edge-crm",
     "networkMode": "awsvpc",
     "requiresCompatibilities": ["FARGATE"],
     "cpu": "256",
     "memory": "512",
     "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
     "containerDefinitions": [
       {
         "name": "talent-edge-crm",
         "image": "ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/talent-edge-crm:latest",
         "portMappings": [
           {
             "containerPort": 8501,
             "protocol": "tcp"
           }
         ],
         "environment": [
           {
             "name": "STREAMLIT_SERVER_PORT",
             "value": "8501"
           },
           {
             "name": "STREAMLIT_SERVER_ADDRESS",
             "value": "0.0.0.0"
           }
         ]
       }
     ]
   }
   ```

4. **Deploy to ECS**:
   ```bash
   aws ecs create-service \
     --cluster your-cluster \
     --service-name talent-edge-crm \
     --task-definition talent-edge-crm:1 \
     --desired-count 1 \
     --launch-type FARGATE \
     --network-configuration "awsvpcConfiguration={subnets=[subnet-12345],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
   ```

### 6. Azure Container Instances

#### Prerequisites
- Azure CLI installed and configured
- Docker image pushed to Azure Container Registry

#### Deployment Steps
1. **Create Azure Container Registry**:
   ```bash
   az acr create --resource-group your-rg --name yourregistry --sku Basic
   ```

2. **Build and push image**:
   ```bash
   az acr build --registry yourregistry --image talent-edge-crm .
   ```

3. **Deploy to Container Instances**:
   ```bash
   az container create \
     --resource-group your-rg \
     --name talent-edge-crm \
     --image yourregistry.azurecr.io/talent-edge-crm:latest \
     --dns-name-label talent-edge-crm \
     --ports 8501 \
     --environment-variables STREAMLIT_SERVER_PORT=8501 STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

### 7. Google Cloud Run

#### Prerequisites
- Google Cloud SDK installed
- Docker image built

#### Deployment Steps
1. **Enable Cloud Run API**:
   ```bash
   gcloud services enable run.googleapis.com
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy talent-edge-crm \
     --image gcr.io/PROJECT_ID/talent-edge-crm \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8501 \
     --set-env-vars STREAMLIT_SERVER_PORT=8501,STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

## 🔧 Environment Configuration

### Environment Variables
```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Application Configuration
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
```

### Configuration Files
- **`.streamlit/config.toml`**: Streamlit server configuration
- **`requirements.txt`**: Python dependencies
- **`runtime.txt`**: Python version specification
- **`Procfile`**: Process specification (Heroku)
- **`vercel.json`**: Vercel deployment configuration

## 🔒 Security Considerations

### Production Security
1. **Environment Variables**: Store sensitive data in environment variables
2. **HTTPS**: Always use HTTPS in production
3. **Authentication**: Implement user authentication if needed
4. **Rate Limiting**: Consider implementing rate limiting
5. **CORS**: Configure CORS appropriately for your domain
6. **Input Validation**: Validate all user inputs
7. **Error Handling**: Don't expose sensitive information in error messages

### Security Headers
```python
# Add to your Streamlit app
st.set_page_config(
    page_title="Cognizant Talent Edge CRM",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Security headers (if using custom server)
import streamlit.web.server as server
server.add_security_headers = lambda headers: headers.update({
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
})
```

## 📊 Monitoring and Logging

### Application Monitoring
1. **Health Checks**: Implement health check endpoints
2. **Error Tracking**: Use services like Sentry for error tracking
3. **Performance Monitoring**: Monitor response times and resource usage
4. **User Analytics**: Track user interactions (with privacy compliance)

### Logging Configuration
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Check what's using the port
lsof -i :8501

# Kill the process
kill -9 <PID>
```

#### 2. Memory Issues
- Increase memory allocation in deployment configuration
- Optimize data loading and processing
- Use streaming for large datasets

#### 3. Timeout Issues
- Increase timeout settings in deployment configuration
- Optimize slow operations
- Use caching for expensive computations

#### 4. Import Errors
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Check Python version compatibility
python --version
```

#### 5. CORS Issues
```python
# In your Streamlit app
import streamlit as st

# Configure CORS
st.set_page_config(
    page_title="Cognizant Talent Edge CRM",
    page_icon="🏦",
    layout="wide"
)

# Add CORS headers if needed
if st.experimental_get_query_params().get("cors"):
    st.markdown("""
    <script>
        // CORS configuration
        fetch('/api/data', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
    </script>
    """, unsafe_allow_html=True)
```

### Debug Mode
```python
# Enable debug mode for development
import streamlit as st

if st.secrets.get("DEBUG", False):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_option('deprecation.showfileUploaderEncoding', False)
```

## 📈 Performance Optimization

### Optimization Strategies
1. **Caching**: Use `@st.cache_data` for expensive computations
2. **Lazy Loading**: Load data only when needed
3. **Pagination**: Implement pagination for large datasets
4. **Compression**: Enable gzip compression
5. **CDN**: Use CDN for static assets

### Caching Example
```python
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    """Load and cache the dataset"""
    return pd.read_csv('data/associates.csv')

@st.cache_data
def process_data(df):
    """Process and cache the data"""
    return df.groupby('location').count()

# Use cached data
data = load_data()
processed_data = process_data(data)
```

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow
```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        run: |
          python -m pytest tests/
      
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
          vercel-args: '--prod'
```

## 📞 Support and Resources

### Documentation
- [Streamlit Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)
- [Vercel Python Documentation](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Heroku Python Documentation](https://devcenter.heroku.com/articles/python-support)

### Community Support
- [Streamlit Community Forum](https://discuss.streamlit.io/)
- [Vercel Community](https://github.com/vercel/vercel/discussions)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/streamlit)

### Monitoring Tools
- [Sentry](https://sentry.io/) - Error tracking
- [DataDog](https://www.datadoghq.com/) - Application monitoring
- [New Relic](https://newrelic.com/) - Performance monitoring

---

## 🎯 Quick Deploy Commands

### Vercel (Recommended)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

### Streamlit Cloud
1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Connect GitHub repository
3. Deploy with one click

### Heroku
```bash
# Create and deploy
heroku create your-app-name
git push heroku main
heroku open
```

### Docker
```bash
# Build and run
docker build -t talent-edge-crm .
docker run -p 8501:8501 talent-edge-crm
```

---

**🎉 Your Cognizant Talent Edge CRM Toolkit is now ready for production deployment!** 