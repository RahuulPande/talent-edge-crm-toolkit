# 🔧 Technical Reference Guide

## Cognizant Talent Edge CRM Toolkit - Developer Documentation

### Table of Contents
- [Architecture Overview](#architecture-overview)
- [Data Models](#data-models)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Development Setup](#development-setup)
- [Testing](#testing)
- [Deployment](#deployment)
- [Performance Optimization](#performance-optimization)
- [Security](#security)
- [Troubleshooting](#troubleshooting)

---

## Architecture Overview

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Data Layer    │
│   (Streamlit)   │◄──►│   (Python)      │◄──►│   (Pandas)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   UI Components │    │   Business      │    │   Data          │
│   CSS/JavaScript│    │   Logic         │    │   Generation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technology Stack
- **Frontend Framework**: Streamlit 1.28+
- **Data Processing**: Pandas 2.0+, NumPy 1.24+
- **Visualizations**: Plotly 5.17+
- **PDF Generation**: ReportLab 4.0+
- **Development**: Python 3.9+

### Core Components

#### 1. Application Entry Point (`app.py`)
- Main Streamlit application
- UI components and navigation
- Business logic integration
- Session state management

#### 2. Data Structure Module (`enhanced_data_structure.py`)
- Swiss banking data model
- Associate profile generation
- Team templates and cost models
- NLP query processing

#### 3. Static Assets
- CSS styling and animations
- JavaScript fixes for UI components
- Documentation and images

---

## Data Models

### Associate Profile Structure
```python
{
    "Associate_ID": "COG001234",
    "Location": "Zurich",
    "Role": "Solution_Architect",
    "Role_Category": "Leadership",
    "Experience_Years": 12,
    "Primary_Skills": ["Java", "Avaloq", "AWS"],
    "Banking_Domains": ["Investment Banking", "Risk Management"],
    "Language_Skills": {"German": "Fluent", "English": "Native"},
    "Certifications": ["AWS Solutions Architect", "FINMA Certified"],
    "Project_Experience": ["CS_Integration", "Digital_Transformation"],
    "Available_Now": True,
    "Available_1_Week": True,
    "Available_1_Month": True,
    "Visa_Status": "Swiss Citizen",
    "Day_Rate_CHF": 1800,
    "Previous_Clients": ["UBS", "Credit Suisse"],
    "CS_Integration_Experience": True,
    "Utilization_Current": 0,
    "Last_Updated": "2025-01-15T10:30:00Z"
}
```

### Skills Taxonomy
```python
SKILLS_TAXONOMY = {
    "Programming_Languages": {
        "Core_Banking": ["Java", "C#/.NET", "COBOL", "PL/SQL"],
        "Modern_Stack": ["JavaScript", "React", "Angular", "Node.js"],
        "Data_Analytics": ["Python", "R", "SQL", "Scala"],
        "Mobile": ["Swift", "Kotlin", "React Native", "Flutter"]
    },
    "Banking_Platforms": {
        "Core_Banking": ["Avaloq", "Temenos T24", "Finnova"],
        "Trading": ["Murex", "Calypso", "Front Arena"],
        "Risk_Management": ["Axiom", "Moody's RiskCalc"],
        "Payments": ["SWIFT", "ISO20022", "SEPA"]
    }
}
```

### Team Template Structure
```python
{
    "name": "Credit Suisse Integration Team",
    "composition": {
        "Solution_Architect": 1,
        "Technical_Lead": 2,
        "Senior_Software_Engineer": 4,
        "Software_Engineer": 6,
        "DevOps_Engineer": 2,
        "Test_Manager": 1,
        "Senior_Test_Engineer": 3,
        "Business_Analyst": 2,
        "Scrum_Master": 1
    },
    "total_size": 22,
    "estimated_monthly_cost_chf": 440000,
    "key_skills_required": ["Avaloq", "Data Migration", "FINMA Compliance"],
    "duration": "18-24 months"
}
```

---

## API Reference

### Data Generation Functions

#### `create_streamlit_dataset()`
**Purpose**: Generate simplified dataset for Streamlit consumption
**Returns**: `pandas.DataFrame`
**Parameters**: None

```python
def create_streamlit_dataset():
    """
    Creates a simplified dataset optimized for Streamlit display
    Returns DataFrame with columns:
    - Project_Type, Location, Skill, Role
    - Count, Available_Now, Available_1_Month
    - Experience_Years
    """
```

#### `enhanced_nlp_response(query, df)`
**Purpose**: Process natural language queries
**Parameters**:
- `query` (str): Natural language query
- `df` (DataFrame): Associate data
**Returns**: `str` (formatted response)

```python
def enhanced_nlp_response(query, df):
    """
    Process natural language queries with Swiss banking context
    Supports queries about:
    - CS Integration projects
    - UBS-specific requirements
    - FINMA compliance
    - Cost optimization
    - Language capabilities
    """
```

#### `generate_associates_data(num_associates=2150)`
**Purpose**: Generate comprehensive associate profiles
**Parameters**:
- `num_associates` (int): Number of profiles to generate
**Returns**: `pandas.DataFrame`

```python
def generate_associates_data(num_associates=2150):
    """
    Generate realistic associate data including:
    - Skill distributions based on role
    - Location-based language skills
    - Experience correlations
    - Visa status for Swiss locations
    - Rate calculations by geography
    """
```

### Utility Functions

#### `generate_pdf_report(data, query_params)`
**Purpose**: Generate executive PDF reports
**Parameters**:
- `data` (DataFrame): Filtered associate data
- `query_params` (dict): Search parameters used
**Returns**: `BytesIO` buffer

### Session State Variables
```python
# Available in st.session_state
{
    'query_results': None,          # Last search results
    'loading': False,               # Loading state indicator
    'selected_team_template': None, # Current team template
    'cost_calculation': None        # Last cost calculation
}
```

---

## Configuration

### Environment Variables
```bash
# Application settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
STREAMLIT_SERVER_HEADLESS=false

# Performance settings
STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
STREAMLIT_RUNNER_MAGIC_ENABLED=true

# Development settings
STREAMLIT_DEVELOPMENT_WATCH_FOR_CHANGES=true
STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=true
```

### Data Configuration
Modify `enhanced_data_structure.py` for custom configurations:

```python
# Adjust total associate count
TOTAL_ASSOCIATES = 2150

# Customize location distribution
location_distribution = {
    "Zurich": 0.25,
    "Geneva": 0.08,
    "Basel": 0.05,
    "Pune": 0.35,
    "Bangalore": 0.17,
    "Chennai": 0.10
}

# Modify role distribution
role_category_distribution = {
    "Engineering": 0.40,
    "Quality": 0.20,
    "Leadership": 0.08,
    "Specialized": 0.12,
    "Analysis": 0.10,
    "Project": 0.08,
    "Compliance": 0.02
}
```

### UI Customization
Key CSS variables for theming:

```css
:root {
    --primary-color: #0072C6;        /* Cognizant Blue */
    --secondary-color: #D40511;      /* UBS Red */
    --success-color: #4CAF50;        /* Green */
    --warning-color: #FF9800;        /* Orange */
    --background-gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    --card-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    --border-radius: 16px;
    --font-family: 'Inter', sans-serif;
}
```

---

## Development Setup

### Local Development Environment

1. **Python Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Development Dependencies**
   ```bash
   pip install watchdog          # File monitoring
   pip install black            # Code formatting
   pip install flake8           # Linting
   pip install pytest           # Testing
   ```

3. **IDE Configuration**
   - **VSCode**: Install Python and Streamlit extensions
   - **PyCharm**: Configure Python interpreter to virtual environment
   - **Jupyter**: For data analysis and prototyping

### Project Structure
```
CRM_APP/
├── app.py                          # Main application
├── enhanced_data_structure.py      # Data models and generation
├── requirements.txt                # Python dependencies
├── README.md                       # Main documentation
├── docs/                          # Documentation
│   ├── user-guide.md
│   ├── technical-reference.md
│   ├── api-reference.md
│   └── images/
├── tests/                         # Test suite
│   ├── test_data_generation.py
│   ├── test_nlp_processing.py
│   └── test_ui_components.py
└── .venv/                        # Virtual environment
```

### Code Standards

#### Python Code Style
- **PEP 8** compliance for all Python code
- **Black** formatter with 88-character line length
- **Type hints** for function parameters and return values
- **Docstrings** for all public functions

```python
def generate_team_cost(
    team_size: int, 
    delivery_model: str, 
    duration_months: int
) -> Dict[str, Union[int, float]]:
    """
    Calculate team cost based on size, model, and duration.
    
    Args:
        team_size: Number of team members
        delivery_model: Delivery approach (onsite, hybrid, offshore)
        duration_months: Project duration in months
        
    Returns:
        Dictionary with cost breakdown and totals
    """
```

#### CSS/JavaScript Standards
- **Consistent naming** using BEM methodology
- **Mobile-first** responsive design
- **Progressive enhancement** for JavaScript features
- **Performance optimization** for large datasets

---

## Testing

### Test Framework Setup
```bash
# Install testing dependencies
pip install pytest pytest-cov streamlit-testing

# Run tests
pytest tests/ -v --cov=app --cov=enhanced_data_structure
```

### Unit Test Examples

#### Data Generation Tests
```python
def test_create_streamlit_dataset():
    """Test basic dataset generation"""
    df = create_streamlit_dataset()
    
    assert len(df) == 100  # Expected record count
    assert all(col in df.columns for col in [
        'Project_Type', 'Location', 'Skill', 'Role'
    ])
    assert df['Available_Now'].sum() > 0
    assert df['Count'].min() > 0

def test_nlp_response_ubs_query():
    """Test UBS-specific query processing"""
    df = create_streamlit_dataset()
    response = enhanced_nlp_response("UBS specialists in Zurich", df)
    
    assert "UBS" in response
    assert "Zurich" in response
    assert any(word in response for word in ["specialists", "available"])
```

#### UI Component Tests
```python
def test_dashboard_metrics():
    """Test dashboard metric calculations"""
    df = create_streamlit_dataset()
    
    zurich_total = df[df['Location'] == 'Zurich']['Count'].sum()
    zurich_available = df[df['Location'] == 'Zurich']['Available_Now'].sum()
    
    assert zurich_total > 0
    assert zurich_available <= zurich_total
    assert isinstance(zurich_total, (int, np.integer))
```

### Integration Tests
```python
def test_end_to_end_search():
    """Test complete search workflow"""
    # Simulate user search
    filters = {
        'project_type': 'CS Integration',
        'location': 'Zurich',
        'skill': 'Avaloq'
    }
    
    # Apply filters (mock implementation)
    results = apply_search_filters(create_streamlit_dataset(), filters)
    
    assert len(results) > 0
    assert all(results['Project_Type'] == 'CS Integration')
```

### Performance Tests
```python
def test_data_generation_performance():
    """Ensure data generation completes within acceptable time"""
    import time
    
    start_time = time.time()
    df = create_streamlit_dataset()
    generation_time = time.time() - start_time
    
    assert generation_time < 5.0  # Max 5 seconds
    assert len(df) > 0
```

---

## Deployment

### Local Deployment
```bash
# Standard development deployment
streamlit run app.py

# With custom configuration
streamlit run app.py --server.port 8502 --server.address 0.0.0.0
```

### Production Deployment

#### Docker Deployment
```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
```

#### Docker Compose
```yaml
version: '3.8'
services:
  talent-edge-crm:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_PORT=8501
    volumes:
      - ./data:/app/data  # Optional: for persistent data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

#### Cloud Deployment (AWS/Azure/GCP)
```bash
# Example for AWS ECS with Fargate
aws ecs create-service \
  --cluster talent-edge-cluster \
  --service-name talent-edge-crm \
  --task-definition talent-edge-task \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-12345],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
```

### Environment-Specific Configurations

#### Development
```python
# config/development.py
DEBUG = True
DATA_REFRESH_INTERVAL = 60  # seconds
CACHE_TTL = 300  # 5 minutes
LOG_LEVEL = "DEBUG"
```

#### Production
```python
# config/production.py
DEBUG = False
DATA_REFRESH_INTERVAL = 3600  # 1 hour
CACHE_TTL = 7200  # 2 hours
LOG_LEVEL = "INFO"
ENABLE_ANALYTICS = True
```

---

## Performance Optimization

### Caching Strategies

#### Data Caching
```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_associate_data():
    """Load and cache associate data"""
    return create_streamlit_dataset()

@st.cache_data
def calculate_team_metrics(team_template: str):
    """Cache expensive team calculations"""
    template = TEAM_TEMPLATES[team_template]
    return {
        'total_cost': template['estimated_monthly_cost_chf'],
        'team_size': template['total_size'],
        'skills_coverage': len(template['key_skills_required'])
    }
```

#### Session State Optimization
```python
# Efficient session state management
if 'search_results' not in st.session_state:
    st.session_state.search_results = None

# Only recalculate when filters change
if st.session_state.get('last_filters') != current_filters:
    st.session_state.search_results = perform_search(current_filters)
    st.session_state.last_filters = current_filters
```

### Large Dataset Handling
```python
# Pagination for large results
def paginate_results(df: pd.DataFrame, page_size: int = 50, page_number: int = 1):
    """Paginate large datasets for better performance"""
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    return df.iloc[start_idx:end_idx]

# Lazy loading for expensive operations
@st.cache_data
def get_visualization_data(data_type: str):
    """Only load visualization data when needed"""
    if data_type == "geographic":
        return calculate_geographic_distribution()
    elif data_type == "skills":
        return calculate_skill_matrix()
```

### Memory Management
```python
# Clear unused dataframes
def cleanup_memory():
    """Clean up large objects from memory"""
    if 'large_dataset' in st.session_state:
        del st.session_state.large_dataset
    
    # Force garbage collection
    import gc
    gc.collect()

# Use generators for large datasets
def generate_associate_profiles():
    """Generator for memory-efficient processing"""
    for i in range(TOTAL_ASSOCIATES):
        yield create_associate_profile(i)
```

---

## Security

### Data Protection

#### Input Validation
```python
def validate_search_input(query: str) -> bool:
    """Validate user input for security"""
    # Prevent SQL injection attempts
    forbidden_chars = [';', '--', '/*', '*/', 'xp_', 'sp_']
    
    if any(char in query.lower() for char in forbidden_chars):
        return False
    
    # Limit query length
    if len(query) > 500:
        return False
        
    return True

def sanitize_filename(filename: str) -> str:
    """Sanitize filenames for safe file operations"""
    import re
    # Remove any non-alphanumeric characters except dash and underscore
    return re.sub(r'[^a-zA-Z0-9_-]', '', filename)
```

#### Data Encryption
```python
def encrypt_sensitive_data(data: str, key: bytes) -> bytes:
    """Encrypt sensitive data before storage"""
    from cryptography.fernet import Fernet
    
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_sensitive_data(encrypted_data: bytes, key: bytes) -> str:
    """Decrypt sensitive data for processing"""
    from cryptography.fernet import Fernet
    
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()
```

### Access Control
```python
# Role-based access control
USER_ROLES = {
    'crm_user': ['read', 'search', 'export'],
    'manager': ['read', 'search', 'export', 'team_build'],
    'admin': ['read', 'search', 'export', 'team_build', 'config']
}

def check_permission(user_role: str, action: str) -> bool:
    """Check if user has permission for action"""
    return action in USER_ROLES.get(user_role, [])
```

### Audit Logging
```python
import logging
from datetime import datetime

def log_user_action(user_id: str, action: str, details: dict):
    """Log user actions for audit trail"""
    logger = logging.getLogger('audit')
    
    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'user_id': user_id,
        'action': action,
        'details': details,
        'ip_address': st.experimental_get_query_params().get('client_ip', 'unknown')
    }
    
    logger.info(f"AUDIT: {log_entry}")
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors
**Problem**: `ModuleNotFoundError: No module named 'enhanced_data_structure'`
**Solution**:
```bash
# Ensure file is in correct location
ls -la enhanced_data_structure.py

# Reinstall dependencies
pip install -r requirements.txt

# Check Python path
python -c "import sys; print(sys.path)"
```

#### 2. Performance Issues
**Problem**: Slow loading times or high memory usage
**Solutions**:
```python
# Enable profiling
import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your code here
    create_streamlit_dataset()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('tottime')
    stats.print_stats(10)

# Memory monitoring
import psutil
import os

def check_memory_usage():
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 / 1024
    print(f"Memory usage: {memory_mb:.2f} MB")
```

#### 3. Data Generation Issues
**Problem**: Inconsistent or invalid data generation
**Solutions**:
```python
# Add data validation
def validate_associate_data(df: pd.DataFrame) -> bool:
    """Validate generated associate data"""
    required_columns = ['Associate_ID', 'Location', 'Role', 'Count']
    
    # Check required columns exist
    if not all(col in df.columns for col in required_columns):
        return False
    
    # Check for null values in critical columns
    if df[required_columns].isnull().any().any():
        return False
    
    # Check for negative counts
    if (df['Count'] < 0).any():
        return False
        
    return True

# Seed random number generator for consistent results
np.random.seed(42)
random.seed(42)
```

#### 4. UI Rendering Issues
**Problem**: Dropdown text not visible or CSS not loading
**Solutions**:
```python
# Force browser cache refresh
st.experimental_memo.clear()
st.experimental_singleton.clear()

# Verify CSS loading
st.markdown("<!-- CSS Debug -->", unsafe_allow_html=True)

# Alternative dropdown implementation
def debug_selectbox(label, options):
    """Debug version of selectbox with enhanced visibility"""
    st.markdown(f"""
    <style>
    .debug-selectbox {{
        background: white !important;
        color: black !important;
        border: 2px solid red !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    return st.selectbox(label, options, key=f"debug_{label}")
```

### Debugging Tools

#### Streamlit Debug Mode
```bash
# Run with debug logging
streamlit run app.py --logger.level=debug

# Enable browser developer tools integration
streamlit run app.py --server.enableCORS=false --server.enableWebsocketCompression=false
```

#### Custom Debug Utilities
```python
def debug_dataframe(df: pd.DataFrame, name: str = "DataFrame"):
    """Debug utility for dataframe inspection"""
    st.write(f"**{name} Info:**")
    st.write(f"Shape: {df.shape}")
    st.write(f"Columns: {list(df.columns)}")
    st.write(f"Memory usage: {df.memory_usage().sum() / 1024:.2f} KB")
    
    if st.checkbox(f"Show {name} head"):
        st.write(df.head())
    
    if st.checkbox(f"Show {name} info"):
        buffer = StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

def debug_session_state():
    """Display current session state for debugging"""
    st.write("**Session State:**")
    for key, value in st.session_state.items():
        st.write(f"{key}: {type(value)} = {str(value)[:100]}...")
```

### Performance Monitoring
```python
import time
from functools import wraps

def monitor_performance(func):
    """Decorator to monitor function performance"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        if execution_time > 1.0:  # Log slow functions
            st.warning(f"Slow function: {func.__name__} took {execution_time:.2f}s")
        
        return result
    return wrapper

# Usage
@monitor_performance
def slow_data_operation():
    """Example of monitored function"""
    return create_streamlit_dataset()
```

---

**Last Updated**: January 2025  
**Version**: 2.0  
**Maintainer**: Cognizant Talent Edge Development Team 