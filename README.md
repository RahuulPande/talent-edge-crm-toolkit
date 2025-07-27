# 🚀 Cognizant Talent Edge CRM Toolkit

## Swiss Banking IT Consulting Edition v2.0

![Talent Edge Banner](docs/images/banner.png)

A comprehensive CRM toolkit designed specifically for Cognizant's Swiss banking practice, enabling CRMs to showcase associate skills, availability, and team configurations for UBS and other Swiss financial institutions.

## 🎯 Overview

The Talent Edge CRM Toolkit is an enterprise-grade Streamlit application that provides:

- **Real-time talent visualization** across 6 global delivery centers
- **Swiss banking-specific intelligence** with FINMA compliance tracking
- **Pre-configured team templates** for major banking projects
- **Advanced cost optimization models** with hybrid delivery options
- **AI-powered natural language queries** for instant talent insights
- **Executive dashboard** with comprehensive analytics

## ✨ Key Features

### 🏠 Executive Dashboard
- Real-time metrics for 2,150+ associates across Zurich, Geneva, Basel, Pune, Bangalore, Chennai
- Pre-configured team templates with cost projections
- Cost optimization models comparing delivery approaches
- Swiss banking readiness indicators

### 🔍 Advanced Talent Search
- Multi-dimensional filtering (Project Type, Skills, Role, Location)
- Smart team builder with proven templates
- Advanced cost calculator with delivery model optimization
- Instant PDF report generation

### 📊 Executive Analytics
- Geographic talent distribution analysis
- Project readiness scoring across banking initiatives
- Skill availability heatmaps
- 6-month growth trend analysis

### 📅 Availability Management
- Real-time availability tracking with visa status
- Deployment timeline simulation
- Resource calendar integration
- Utilization optimization

### 🤖 AI-Powered Insights
- Natural language query processing
- Swiss banking context awareness
- FINMA compliance intelligence
- Cost and budget optimization suggestions

## 🛠️ Technical Architecture

### Core Components
- **Frontend**: Streamlit with custom CSS/JavaScript
- **Data Layer**: Pandas with comprehensive Swiss banking data model
- **Analytics**: Plotly for interactive visualizations
- **Reports**: ReportLab for PDF generation
- **AI**: Enhanced NLP for natural language queries

### Data Structure
- **2,150+ Associate profiles** with Swiss banking expertise
- **50+ Banking platforms** (Avaloq, Temenos, Murex, etc.)
- **Comprehensive role hierarchy** from Junior Engineers to Enterprise Architects
- **Multi-language capabilities** (German, French, Italian, English)
- **Visa status tracking** for Swiss compliance

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- macOS/Windows/Linux
- Modern web browser (Chrome, Safari, Firefox, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CRM_APP
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python3 -m streamlit run app.py
   ```

5. **Access the application**
   - Local URL: http://localhost:8501
   - Network URL: Available in terminal output

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.9 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB free space
- **Network**: Internet connection for initial setup

### Recommended Environment
- **OS**: macOS 12+, Windows 10+, Ubuntu 20.04+
- **Browser**: Latest version of Chrome, Safari, or Firefox
- **Display**: 1920x1080 or higher resolution

## 🎨 User Interface

### Navigation Structure
```
├── 🏠 Dashboard (Executive Overview)
├── 🔍 Project Query (Talent Search & Team Builder)
├── 📊 Visualizations (Analytics & Insights)
├── 📅 Availability (Resource Management)
└── ❓ Help (Documentation & Support)
```

### Key UI Components
- **Responsive design** optimized for desktop and tablet
- **Professional Swiss banking theme** with Cognizant branding
- **Interactive visualizations** with hover effects and drill-down capabilities
- **Advanced dropdown fixes** ensuring perfect visibility across all browsers

## 🏦 Swiss Banking Focus

### UBS-Specific Features
- **Credit Suisse Integration** templates and resource allocation
- **FINMA compliance** tracking and reporting
- **German/French language** capabilities for client-facing roles
- **Swiss visa status** monitoring for regulatory compliance

### Banking Platform Expertise
- **Core Banking**: Avaloq, Temenos T24, Finnova, Oracle FLEXCUBE
- **Trading**: Murex, Calypso, Front Arena, Summit
- **Risk Management**: Axiom, Moody's RiskCalc, MSCI RiskMetrics
- **Payments**: SWIFT, ISO20022, SEPA, TARGET2, SIX Payment

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Customize application settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
```

### Data Configuration
The application uses a sophisticated data generation system in `enhanced_data_structure.py`:
- Configurable associate count (default: 2,150)
- Customizable skill taxonomies
- Adjustable cost models and rate cards

## 📊 Analytics & Reporting

### Dashboard Metrics
- **Total Associates**: Real-time count across all locations
- **Swiss-based Resources**: Zurich, Geneva, Basel availability
- **Immediate Availability**: Associates ready for deployment
- **UBS Readiness**: Specialists prepared for UBS projects

### Report Generation
- **PDF Reports**: Executive summaries with detailed breakdowns
- **Excel Exports**: Data extracts for further analysis
- **Cost Projections**: Multi-scenario financial modeling

## 🤖 AI-Powered Features

### Natural Language Queries
Examples of supported queries:
- "CS Integration specialists in Zurich"
- "FINMA compliance experts with German language"
- "Avaloq developers for UBS project"
- "Cost optimization for 25-person hybrid team"

### Intelligent Responses
The AI system provides contextual responses including:
- **Skill availability** with immediate deployment options
- **Cost comparisons** across delivery models
- **Compliance information** for regulatory requirements
- **Language capabilities** for client-facing roles

## 🔒 Security & Compliance

### Data Protection
- **Swiss DPA compliance** for data residency requirements
- **GDPR alignment** for EU citizen data handling
- **Encryption standards** using AES-256 minimum
- **Access controls** with role-based permissions

### Banking Compliance
- **FINMA regulations** embedded in talent profiles
- **Basel III requirements** tracked for risk management roles
- **Audit trails** for all talent allocation decisions

## 🚀 Deployment Options

### Local Development
```bash
# Standard local deployment
python3 -m streamlit run app.py
```

### Production Deployment
```bash
# Production-ready deployment with optimizations
python3 -m streamlit run app.py --server.port 8501 --server.headless true
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"]
```

## 🛠️ Troubleshooting

### Common Issues

1. **Dropdown text not visible**
   - **Solution**: The app includes comprehensive dropdown visibility fixes
   - **Verification**: Check that CSS and JavaScript fixes are loading properly

2. **Module import errors**
   - **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`
   - **Note**: Use `python3 -m pip` if `pip` command not found

3. **Data loading issues**
   - **Solution**: Verify `enhanced_data_structure.py` is in the same directory
   - **Check**: Confirm pandas and numpy are properly installed

4. **Performance issues**
   - **Solution**: Install Watchdog for better file monitoring: `pip install watchdog`
   - **Optimization**: Use caching for large datasets

### Getting Help
- **Documentation**: Check `/docs` folder for detailed guides
- **Issues**: Create GitHub issues for bug reports
- **Support**: Contact the development team for enterprise support

## 📈 Performance Optimization

### Caching Strategy
- **Data caching** using `@st.cache_data` for expensive operations
- **Component caching** for frequently accessed UI elements
- **Session state management** for user preferences

### Best Practices
- **Lazy loading** for large datasets
- **Pagination** for extensive search results
- **Optimized queries** for database operations

## 🔄 Version History

### v2.0 - Current Release
- ✅ Comprehensive Swiss banking data model
- ✅ Advanced dropdown visibility fixes
- ✅ Pre-configured team templates
- ✅ Cost optimization models
- ✅ Enhanced AI-powered queries

### v1.0 - Initial Release
- ✅ Basic talent search functionality
- ✅ Simple dashboard metrics
- ✅ PDF report generation

## 🤝 Contributing

### Development Workflow
1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/new-feature`
3. **Make changes** with proper testing
4. **Submit pull request** with detailed description

### Code Standards
- **PEP 8** compliance for Python code
- **Comprehensive documentation** for new features
- **Unit tests** for critical functionality
- **Security review** for data handling changes

## 📄 License

This project is proprietary to Cognizant Technology Solutions. All rights reserved.

For licensing inquiries, contact: [legal@cognizant.com](mailto:legal@cognizant.com)

## 📞 Support

### Enterprise Support
- **Email**: talentedge@cognizant.com
- **Phone**: +41 58 123 4567 (Switzerland)
- **Hours**: 24/7 for critical issues

### Documentation
- **User Guides**: [docs/user-guide.md](docs/user-guide.md)
- **Technical Reference**: [docs/technical-reference.md](docs/technical-reference.md)
- **API Documentation**: [docs/api-reference.md](docs/api-reference.md)

---

**Built with ❤️ for UBS Partnership Success**

© 2025 Cognizant Technology Solutions. All rights reserved. 