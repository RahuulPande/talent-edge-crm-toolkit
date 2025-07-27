# 📋 API Reference

## Cognizant Talent Edge CRM Toolkit - API Documentation

### Table of Contents
- [Core Functions](#core-functions)
- [Data Structures](#data-structures)
- [Constants and Enums](#constants-and-enums)
- [Utility Functions](#utility-functions)
- [Configuration Parameters](#configuration-parameters)
- [Error Handling](#error-handling)

---

## Core Functions

### Data Generation

#### `create_streamlit_dataset()`
Creates a simplified dataset optimized for Streamlit display.

**Signature:**
```python
def create_streamlit_dataset() -> pd.DataFrame
```

**Returns:**
- `pd.DataFrame`: Dataset with 100 records containing project, location, skill, and role information

**Example:**
```python
df = create_streamlit_dataset()
print(df.head())
#   Project_Type Location        Skill            Role  Count  Available_Now  Available_1_Month  Experience_Years
# 0   CS Integration   Zurich  Data Analytics  Solution Architect     42             25                 35                 8
```

**Columns:**
- `Project_Type`: Banking project category
- `Location`: Delivery center location
- `Skill`: Primary technical skill
- `Role`: Job role/position
- `Count`: Total associates matching criteria
- `Available_Now`: Associates available immediately
- `Available_1_Month`: Associates available within 1 month
- `Experience_Years`: Average years of experience

---

#### `generate_associates_data(num_associates=2150)`
Generates comprehensive associate profiles with full Swiss banking context.

**Signature:**
```python
def generate_associates_data(num_associates: int = 2150) -> pd.DataFrame
```

**Parameters:**
- `num_associates` (int, optional): Number of associate profiles to generate. Default: 2150

**Returns:**
- `pd.DataFrame`: Comprehensive associate profiles with all attributes

**Example:**
```python
associates = generate_associates_data(100)
print(associates.columns.tolist())
# ['Associate_ID', 'Location', 'Role', 'Role_Category', 'Experience_Years', 
#  'Primary_Skills', 'Banking_Domains', 'Language_Skills', 'Certifications', ...]
```

---

### Natural Language Processing

#### `enhanced_nlp_response(query, df)`
Process natural language queries with Swiss banking intelligence.

**Signature:**
```python
def enhanced_nlp_response(query: str, df: pd.DataFrame) -> str
```

**Parameters:**
- `query` (str): Natural language query from user
- `df` (pd.DataFrame): Associate dataset to query against

**Returns:**
- `str`: Formatted response with banking context and insights

**Supported Query Types:**

1. **CS Integration Queries**
   ```python
   response = enhanced_nlp_response("CS Integration specialists in Zurich", df)
   # Returns: "🏦 CS Integration Readiness: 234 specialists across all locations..."
   ```

2. **UBS-Specific Queries**
   ```python
   response = enhanced_nlp_response("UBS project team", df)
   # Returns: "🎯 UBS Project Readiness: 1,385 specialists in our talent pool..."
   ```

3. **FINMA/Compliance Queries**
   ```python
   response = enhanced_nlp_response("FINMA compliance experts", df)
   # Returns: "⚖️ Regulatory Compliance Experts: 89 specialists with FINMA certification..."
   ```

4. **Language-Specific Queries**
   ```python
   response = enhanced_nlp_response("German speaking architects", df)
   # Returns: "🇩🇪 German-Speaking Talent in Zurich: 156 associates (98 available now)..."
   ```

5. **Technology Queries**
   ```python
   response = enhanced_nlp_response("Avaloq developers", df)
   # Returns: "🏛️ Avaloq Specialists: 67 certified professionals across Switzerland..."
   ```

6. **Cost Optimization Queries**
   ```python
   response = enhanced_nlp_response("cost optimization hybrid model", df)
   # Returns: "💰 Cost Optimization: Our hybrid delivery model offers 28% cost savings..."
   ```

---

### Report Generation

#### `generate_pdf_report(data, query_params)`
Generate executive PDF reports with professional formatting.

**Signature:**
```python
def generate_pdf_report(data: pd.DataFrame, query_params: Dict[str, Any]) -> BytesIO
```

**Parameters:**
- `data` (pd.DataFrame): Filtered associate data
- `query_params` (dict): Search parameters used for filtering

**Query Parameters Structure:**
```python
query_params = {
    'project_type': 'CS Integration',
    'skill': 'Avaloq',
    'role': 'Solution Architect',
    'location': 'Zurich'
}
```

**Returns:**
- `BytesIO`: PDF report buffer ready for download

**Example:**
```python
filtered_data = df[df['Project_Type'] == 'CS Integration']
params = {'project_type': 'CS Integration', 'skill': 'All', 'role': 'All', 'location': 'All'}
pdf_buffer = generate_pdf_report(filtered_data, params)

# Save to file
with open('talent_report.pdf', 'wb') as f:
    f.write(pdf_buffer.getvalue())
```

**Report Sections:**
1. **Executive Summary**: Key metrics and readiness scores
2. **Search Criteria**: Parameters used for filtering
3. **Detailed Breakdown**: Associate profiles and skills
4. **Cost Projections**: Financial estimates and models

---

## Data Structures

### Associate Profile
Complete profile structure for individual associates:

```python
{
    "Associate_ID": str,           # Unique identifier (e.g., "COG001234")
    "Location": str,               # Delivery center location
    "Role": str,                   # Specific job role
    "Role_Category": str,          # High-level role category
    "Experience_Years": int,       # Years of relevant experience
    "Primary_Skills": List[str],   # Technical skills array
    "Banking_Domains": List[str],  # Banking domain expertise
    "Language_Skills": Dict[str, str],  # Language proficiency levels
    "Certifications": List[str],   # Professional certifications
    "Project_Experience": List[str],  # Previous project types
    "Available_Now": bool,         # Immediate availability
    "Available_1_Week": bool,      # 1-week availability
    "Available_1_Month": bool,     # 1-month availability
    "Visa_Status": str,           # Swiss visa/permit status
    "Day_Rate_CHF": int,          # Daily rate in Swiss Francs
    "Previous_Clients": List[str], # Previous banking clients
    "CS_Integration_Experience": bool,  # CS integration expertise
    "Utilization_Current": int,    # Current utilization percentage
    "Last_Updated": datetime      # Profile last update timestamp
}
```

### Team Template
Pre-configured team structure for banking projects:

```python
{
    "name": str,                    # Template display name
    "composition": Dict[str, int],  # Role → count mapping
    "total_size": int,             # Total team members
    "estimated_monthly_cost_chf": int,  # Monthly cost in CHF
    "key_skills_required": List[str],   # Essential skills
    "duration": str                # Typical project duration
}
```

### Cost Model
Delivery model with cost implications:

```python
{
    "description": str,            # Model description
    "cost_index": float,           # Cost multiplier (0.0-1.0)
    "advantages": List[str],       # Model benefits
    "disadvantages": List[str]     # Model limitations
}
```

---

## Constants and Enums

### Skill Categories
Comprehensive taxonomy of technical skills:

```python
SKILLS_TAXONOMY = {
    "Programming_Languages": {
        "Core_Banking": ["Java", "C#/.NET", "COBOL", "PL/SQL", "Python", "C++"],
        "Modern_Stack": ["JavaScript", "TypeScript", "React", "Angular", "Node.js"],
        "Data_Analytics": ["Python", "R", "SQL", "Scala", "SAS", "MATLAB"],
        "Mobile": ["Swift", "Kotlin", "React Native", "Flutter"]
    },
    "Banking_Platforms": {
        "Core_Banking": ["Avaloq", "Temenos T24", "Finnova", "Oracle FLEXCUBE"],
        "Trading": ["Murex", "Calypso", "Front Arena", "Summit"],
        "Risk_Management": ["Axiom", "Moody's RiskCalc", "MSCI RiskMetrics"],
        "Payments": ["SWIFT", "ISO20022", "SEPA", "TARGET2", "SIX Payment"]
    }
}
```

### Role Hierarchy
Comprehensive role structure with experience and rates:

```python
ROLES_HIERARCHY = {
    "Leadership": {
        "Enterprise_Architect": {"min_exp": 15, "day_rate_chf": 2200, "seniority": 10},
        "Solution_Architect": {"min_exp": 12, "day_rate_chf": 1800, "seniority": 9},
        # ... additional roles
    },
    "Engineering": {
        "Senior_Software_Engineer": {"min_exp": 5, "day_rate_chf": 1400, "seniority": 6},
        "Software_Engineer": {"min_exp": 3, "day_rate_chf": 1100, "seniority": 4},
        # ... additional roles
    }
}
```

### Project Types
Banking project categories with metadata:

```python
PROJECT_TYPES = {
    "CS_Integration": {
        "name": "Credit Suisse Integration",
        "priority": "Critical",
        "duration": "24 months",
        "key_skills": ["Avaloq", "Data Migration", "FINMA Compliance"]
    },
    "Digital_Transformation": {
        "name": "Digital Banking Initiative",
        "priority": "High",
        "duration": "18 months",
        "key_skills": ["React", "Node.js", "AWS", "Mobile Development"]
    }
}
```

### Locations
Delivery center information:

```python
LOCATIONS = {
    "Zurich": {
        "total_capacity": 950,
        "office": "Thurgauerstrasse 36, 8050 Zürich",
        "attributes": ["Primary Hub", "Client Facing", "Swiss Resident Priority"]
    },
    "Pune": {
        "total_capacity": 1500,
        "office": "Hinjewadi IT Park",
        "attributes": ["24/7 Support", "Cost Effective", "Scale Center"]
    }
}
```

### Certifications
Professional certifications by category:

```python
CERTIFICATIONS = {
    "Cloud": ["AWS Solutions Architect", "AWS DevOps Engineer", "Azure Solutions Architect"],
    "Banking": ["FINMA Certified", "Basel III Expert", "Swift Certified"],
    "Security": ["CISSP", "CISA", "CEH", "Security+"],
    "Project": ["PMP", "Prince2", "SAFe Agilist", "CSM"],
    "Testing": ["ISTQB Advanced", "ISTQB Expert", "Performance Testing Certified"]
}
```

---

## Utility Functions

### Data Validation

#### `validate_search_filters(filters)`
Validate search filter parameters.

**Signature:**
```python
def validate_search_filters(filters: Dict[str, str]) -> Tuple[bool, str]
```

**Parameters:**
- `filters` (dict): Search filter parameters

**Returns:**
- `Tuple[bool, str]`: (is_valid, error_message)

**Example:**
```python
filters = {'project_type': 'CS Integration', 'location': 'InvalidLocation'}
is_valid, error = validate_search_filters(filters)
if not is_valid:
    print(f"Validation error: {error}")
```

#### `sanitize_input(user_input)`
Sanitize user input for security.

**Signature:**
```python
def sanitize_input(user_input: str) -> str
```

**Parameters:**
- `user_input` (str): Raw user input

**Returns:**
- `str`: Sanitized and validated input

---

### Data Processing

#### `calculate_availability_metrics(df)`
Calculate comprehensive availability metrics.

**Signature:**
```python
def calculate_availability_metrics(df: pd.DataFrame) -> Dict[str, Union[int, float]]
```

**Parameters:**
- `df` (pd.DataFrame): Associate dataset

**Returns:**
```python
{
    'total_associates': int,
    'available_now': int,
    'available_1_week': int,
    'available_1_month': int,
    'average_experience': float,
    'swiss_based_count': int,
    'offshore_count': int,
    'utilization_rate': float
}
```

#### `filter_by_criteria(df, **criteria)`
Apply multiple filter criteria to dataset.

**Signature:**
```python
def filter_by_criteria(df: pd.DataFrame, **criteria) -> pd.DataFrame
```

**Parameters:**
- `df` (pd.DataFrame): Source dataset
- `**criteria`: Arbitrary filter criteria

**Example:**
```python
filtered = filter_by_criteria(
    df, 
    location='Zurich', 
    skill='Avaloq', 
    available_now=True
)
```

---

### Cost Calculations

#### `calculate_team_cost(composition, delivery_model, duration_months)`
Calculate comprehensive team costs.

**Signature:**
```python
def calculate_team_cost(
    composition: Dict[str, int], 
    delivery_model: str, 
    duration_months: int
) -> Dict[str, Union[int, float]]
```

**Parameters:**
- `composition` (dict): Role → count mapping
- `delivery_model` (str): Delivery model key
- `duration_months` (int): Project duration

**Returns:**
```python
{
    'monthly_cost_chf': int,
    'total_cost_chf': int,
    'savings_vs_onsite': float,
    'cost_breakdown': Dict[str, int],
    'delivery_model_benefits': List[str]
}
```

---

## Configuration Parameters

### Application Settings
Environment variables for application behavior:

```python
# Server configuration
STREAMLIT_SERVER_PORT: int = 8501
STREAMLIT_SERVER_ADDRESS: str = "localhost"
STREAMLIT_SERVER_HEADLESS: bool = False

# Performance settings
CACHE_TTL_SECONDS: int = 3600  # 1 hour
MAX_UPLOAD_SIZE_MB: int = 200
ENABLE_PERFORMANCE_MONITORING: bool = True

# Data generation settings
DEFAULT_ASSOCIATE_COUNT: int = 2150
SIMPLIFIED_DATASET_SIZE: int = 100
DATA_REFRESH_INTERVAL_SECONDS: int = 3600

# Security settings
MAX_QUERY_LENGTH: int = 500
ENABLE_INPUT_VALIDATION: bool = True
LOG_USER_ACTIONS: bool = True
```

### UI Customization
CSS and styling parameters:

```python
# Color scheme
PRIMARY_COLOR: str = "#0072C6"    # Cognizant Blue
SECONDARY_COLOR: str = "#D40511"  # UBS Red
SUCCESS_COLOR: str = "#4CAF50"    # Green
WARNING_COLOR: str = "#FF9800"    # Orange

# Layout settings
SIDEBAR_WIDTH: int = 300
MAIN_CONTENT_WIDTH: str = "wide"
CHART_HEIGHT: int = 400
CARD_BORDER_RADIUS: int = 16

# Animation settings
TRANSITION_DURATION: str = "0.3s"
HOVER_SCALE: float = 1.05
PROGRESS_ANIMATION_DURATION: str = "1.5s"
```

---

## Error Handling

### Exception Classes

#### `DataGenerationError`
Raised when data generation fails.

```python
class DataGenerationError(Exception):
    """Raised when associate data generation encounters errors"""
    pass

# Usage
try:
    df = generate_associates_data(2150)
except DataGenerationError as e:
    print(f"Data generation failed: {e}")
```

#### `ValidationError`
Raised when input validation fails.

```python
class ValidationError(Exception):
    """Raised when input validation fails"""
    pass

# Usage
try:
    validate_search_filters(user_filters)
except ValidationError as e:
    st.error(f"Invalid filters: {e}")
```

#### `CostCalculationError`
Raised when cost calculations fail.

```python
class CostCalculationError(Exception):
    """Raised when cost calculation encounters errors"""
    pass
```

### Error Response Format
Standardized error response structure:

```python
{
    "error": True,
    "error_code": str,        # Machine-readable error code
    "error_message": str,     # Human-readable error message
    "error_details": dict,    # Additional error context
    "timestamp": str,         # ISO format timestamp
    "request_id": str        # Unique request identifier
}
```

### Common Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| `DATA_001` | Dataset generation failed | Check memory and dependencies |
| `DATA_002` | Invalid data format | Verify data structure |
| `FILTER_001` | Invalid filter criteria | Check filter parameters |
| `FILTER_002` | No results found | Adjust search criteria |
| `COST_001` | Cost calculation failed | Verify team composition |
| `COST_002` | Invalid delivery model | Use valid delivery model |
| `NLP_001` | Query processing failed | Simplify query or check format |
| `PDF_001` | Report generation failed | Check data availability |
| `CONFIG_001` | Configuration error | Verify environment settings |

---

**API Version**: 2.0  
**Last Updated**: January 2025  
**Compatibility**: Python 3.9+, Streamlit 1.28+ 