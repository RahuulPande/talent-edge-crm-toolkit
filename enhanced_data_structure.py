# Enhanced Mock Data Structure for Talent Edge CRM Toolkit
# Swiss Banking IT Consulting Edition

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration for realistic data generation
TOTAL_ASSOCIATES = 2150  # Cognizant Switzerland + Support from India

# 1. COMPREHENSIVE SKILLS TAXONOMY
SKILLS_TAXONOMY = {
    "Programming_Languages": {
        "Core_Banking": ["Java", "C#/.NET", "COBOL", "PL/SQL", "Python", "C++"],
        "Modern_Stack": ["JavaScript", "TypeScript", "React", "Angular", "Node.js", "Spring Boot"],
        "Data_Analytics": ["Python", "R", "SQL", "Scala", "SAS", "MATLAB"],
        "Mobile": ["Swift", "Kotlin", "React Native", "Flutter"]
    },
    "Banking_Platforms": {
        "Core_Banking": ["Avaloq", "Temenos T24", "Finnova", "Oracle FLEXCUBE", "Finastra Fusion"],
        "Trading": ["Murex", "Calypso", "Front Arena", "Summit"],
        "Risk_Management": ["Axiom", "Moody's RiskCalc", "MSCI RiskMetrics", "Numerix"],
        "Payments": ["SWIFT", "ISO20022", "SEPA", "TARGET2", "SIX Payment"]
    },
    "Cloud_Platforms": {
        "Public_Cloud": ["AWS", "AWS Switzerland", "Azure", "Google Cloud Platform"],
        "Private_Cloud": ["VMware", "OpenStack", "Swiss Private Cloud"]
    },
    "Databases": {
        "Relational": ["Oracle", "SQL Server", "PostgreSQL", "MySQL", "DB2"],
        "NoSQL": ["MongoDB", "Cassandra", "Redis", "Elasticsearch", "Neo4j"]
    },
    "DevOps_Tools": {
        "CI_CD": ["Jenkins", "GitLab CI", "Azure DevOps", "Bamboo", "TeamCity"],
        "Containerization": ["Docker", "Kubernetes", "OpenShift", "Rancher"],
        "IaC": ["Terraform", "Ansible", "CloudFormation", "Helm"]
    },
    "Testing_Tools": {
        "Automation": ["Selenium", "Cypress", "Playwright", "TestComplete"],
        "Performance": ["JMeter", "LoadRunner", "Gatling", "BlazeMeter"],
        "API": ["Postman", "SoapUI", "Rest Assured", "Karate"]
    },
    "Security_Tools": {
        "SAST": ["SonarQube", "Fortify", "Checkmarx", "Veracode"],
        "DAST": ["OWASP ZAP", "Burp Suite", "Acunetix"],
        "IAM": ["Okta", "Ping Identity", "ForgeRock", "SailPoint"]
    },
    "Monitoring": {
        "APM": ["Dynatrace", "AppDynamics", "New Relic", "Splunk"],
        "Logging": ["ELK Stack", "Splunk", "Datadog", "Prometheus/Grafana"]
    },
    "Project_Tools": {
        "Agile": ["JIRA", "Confluence", "Azure Boards", "Rally"],
        "PPM": ["ServiceNow", "Clarity PPM", "MS Project", "Planview"]
    }
}

# 2. COMPREHENSIVE ROLE HIERARCHY
ROLES_HIERARCHY = {
    "Leadership": {
        "Enterprise_Architect": {"min_exp": 15, "day_rate_chf": 2200, "seniority": 10},
        "Solution_Architect": {"min_exp": 12, "day_rate_chf": 1800, "seniority": 9},
        "Technical_Lead": {"min_exp": 10, "day_rate_chf": 1600, "seniority": 8},
        "Delivery_Manager": {"min_exp": 10, "day_rate_chf": 1500, "seniority": 8},
        "Program_Manager": {"min_exp": 12, "day_rate_chf": 1700, "seniority": 9}
    },
    "Specialized": {
        "DevOps_Architect": {"min_exp": 8, "day_rate_chf": 1600, "seniority": 7},
        "Cloud_Architect": {"min_exp": 8, "day_rate_chf": 1700, "seniority": 7},
        "Security_Architect": {"min_exp": 10, "day_rate_chf": 1800, "seniority": 8},
        "Data_Architect": {"min_exp": 10, "day_rate_chf": 1700, "seniority": 8},
        "Integration_Architect": {"min_exp": 10, "day_rate_chf": 1600, "seniority": 7}
    },
    "Engineering": {
        "Senior_Software_Engineer": {"min_exp": 5, "day_rate_chf": 1400, "seniority": 6},
        "Software_Engineer": {"min_exp": 3, "day_rate_chf": 1100, "seniority": 4},
        "Junior_Engineer": {"min_exp": 1, "day_rate_chf": 800, "seniority": 2},
        "DevOps_Engineer": {"min_exp": 4, "day_rate_chf": 1300, "seniority": 5},
        "Cloud_Engineer": {"min_exp": 4, "day_rate_chf": 1350, "seniority": 5},
        "Data_Engineer": {"min_exp": 4, "day_rate_chf": 1400, "seniority": 5},
        "ML_Engineer": {"min_exp": 5, "day_rate_chf": 1500, "seniority": 6}
    },
    "Quality": {
        "Test_Manager": {"min_exp": 8, "day_rate_chf": 1400, "seniority": 7},
        "Test_Architect": {"min_exp": 10, "day_rate_chf": 1500, "seniority": 8},
        "Senior_Test_Engineer": {"min_exp": 5, "day_rate_chf": 1200, "seniority": 5},
        "Test_Engineer": {"min_exp": 2, "day_rate_chf": 900, "seniority": 3},
        "Performance_Test_Engineer": {"min_exp": 4, "day_rate_chf": 1300, "seniority": 5}
    },
    "Analysis": {
        "Business_Analyst": {"min_exp": 5, "day_rate_chf": 1200, "seniority": 5},
        "Systems_Analyst": {"min_exp": 6, "day_rate_chf": 1300, "seniority": 6},
        "Data_Analyst": {"min_exp": 4, "day_rate_chf": 1100, "seniority": 4},
        "Quantitative_Analyst": {"min_exp": 6, "day_rate_chf": 1600, "seniority": 6}
    },
    "Project": {
        "Scrum_Master": {"min_exp": 4, "day_rate_chf": 1200, "seniority": 5},
        "Product_Owner": {"min_exp": 6, "day_rate_chf": 1400, "seniority": 6},
        "Release_Manager": {"min_exp": 5, "day_rate_chf": 1300, "seniority": 5},
        "PMO_Lead": {"min_exp": 8, "day_rate_chf": 1400, "seniority": 7}
    },
    "Compliance": {
        "Compliance_Manager": {"min_exp": 8, "day_rate_chf": 1600, "seniority": 7},
        "Risk_Analyst": {"min_exp": 5, "day_rate_chf": 1300, "seniority": 5},
        "Security_Analyst": {"min_exp": 4, "day_rate_chf": 1200, "seniority": 4},
        "Audit_Specialist": {"min_exp": 6, "day_rate_chf": 1400, "seniority": 6}
    }
}

# 3. BANKING PROJECT TYPES (UBS FOCUSED)
PROJECT_TYPES = {
    "CS_Integration": {
        "name": "Credit Suisse Integration",
        "priority": "Critical",
        "duration": "24 months",
        "key_skills": ["Avaloq", "Data Migration", "FINMA Compliance", "Project Management"]
    },
    "Digital_Transformation": {
        "name": "Digital Banking Initiative",
        "priority": "High",
        "duration": "18 months",
        "key_skills": ["React", "Node.js", "AWS", "Mobile Development"]
    },
    "Core_Banking_Modernization": {
        "name": "Core System Upgrade",
        "priority": "High",
        "duration": "36 months",
        "key_skills": ["Java", "Oracle", "Temenos", "DevOps"]
    },
    "Regulatory_Compliance": {
        "name": "FINMA/Basel III Compliance",
        "priority": "Critical",
        "duration": "12 months",
        "key_skills": ["Risk Management", "Reporting", "SQL", "Compliance"]
    },
    "Cloud_Migration": {
        "name": "AWS Switzerland Migration",
        "priority": "High",
        "duration": "24 months",
        "key_skills": ["AWS", "Terraform", "DevOps", "Security"]
    },
    "Data_Analytics_Platform": {
        "name": "Risk Analytics Enhancement",
        "priority": "Medium",
        "duration": "18 months",
        "key_skills": ["Python", "Spark", "ML", "Tableau"]
    },
    "API_Modernization": {
        "name": "Open Banking APIs",
        "priority": "Medium",
        "duration": "12 months",
        "key_skills": ["API Gateway", "Spring Boot", "Security", "Integration"]
    },
    "Cybersecurity_Enhancement": {
        "name": "Security Transformation",
        "priority": "Critical",
        "duration": "18 months",
        "key_skills": ["Security Tools", "IAM", "Compliance", "DevSecOps"]
    }
}

# 4. CERTIFICATIONS RELEVANT TO BANKING
CERTIFICATIONS = {
    "Cloud": ["AWS Solutions Architect", "AWS DevOps Engineer", "Azure Solutions Architect", 
              "Google Cloud Architect", "Kubernetes CKA", "Kubernetes CKAD"],
    "Banking": ["FINMA Certified", "Basel III Expert", "Swift Certified", "ISO20022 Expert"],
    "Security": ["CISSP", "CISA", "CEH", "Security+", "CCSP"],
    "Project": ["PMP", "Prince2", "SAFe Agilist", "CSM", "PSM"],
    "Testing": ["ISTQB Advanced", "ISTQB Expert", "Performance Testing Certified"],
    "Data": ["Databricks Certified", "Confluent Kafka", "Elastic Certified"],
    "Vendor": ["Oracle DBA", "Microsoft Certified", "Red Hat Certified", "VMware Certified"]
}

# 5. LANGUAGE CAPABILITIES
LANGUAGES = {
    "German": ["Native", "Fluent", "Business", "Basic"],
    "French": ["Native", "Fluent", "Business", "Basic"],
    "Italian": ["Native", "Fluent", "Business", "Basic"],
    "English": ["Native", "Fluent", "Business", "Basic"]
}

# 6. LOCATIONS WITH DETAILED ATTRIBUTES
LOCATIONS = {
    "Zurich": {
        "total_capacity": 950,
        "office": "Thurgauerstrasse 36, 8050 Zürich",
        "attributes": ["Primary Hub", "Client Facing", "Swiss Resident Priority"]
    },
    "Geneva": {
        "total_capacity": 250,
        "office": "Route de l'Aéroport 31, 1215 Genève",
        "attributes": ["French Speaking", "Private Banking Focus"]
    },
    "Basel": {
        "total_capacity": 180,
        "office": "Aeschenvorstadt 55, 4051 Basel",
        "attributes": ["Pharma-Banking Crossover", "German Speaking"]
    },
    "Pune": {
        "total_capacity": 1500,
        "office": "Hinjewadi IT Park",
        "attributes": ["24/7 Support", "Cost Effective", "Scale Center"]
    },
    "Bangalore": {
        "total_capacity": 800,
        "office": "Electronic City",
        "attributes": ["Innovation Hub", "AI/ML Center", "FinTech Focus"]
    },
    "Chennai": {
        "total_capacity": 600,
        "office": "SIPCOT IT Park",
        "attributes": ["Testing Center", "Support Hub"]
    }
}

# 7. TEAM COMPOSITION TEMPLATES
TEAM_TEMPLATES = {
    "CS_Integration_Squad": {
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
        "key_skills_required": ["Avaloq", "Data Migration", "FINMA Compliance", "German"],
        "duration": "18-24 months"
    },
    
    "Digital_Banking_Team": {
        "name": "Digital Transformation Squad",
        "composition": {
            "Solution_Architect": 1,
            "Technical_Lead": 1,
            "Senior_Software_Engineer": 3,
            "Software_Engineer": 5,
            "Cloud_Engineer": 2,
            "DevOps_Engineer": 2,
            "Test_Engineer": 3,
            "Product_Owner": 1
        },
        "total_size": 18,
        "estimated_monthly_cost_chf": 360000,
        "key_skills_required": ["React", "Node.js", "AWS", "Mobile", "API Development"],
        "duration": "12-18 months"
    },
    
    "Core_Banking_Modernization": {
        "name": "Core System Upgrade Team",
        "composition": {
            "Enterprise_Architect": 1,
            "Solution_Architect": 2,
            "Technical_Lead": 3,
            "Senior_Software_Engineer": 8,
            "Software_Engineer": 10,
            "Data_Engineer": 3,
            "DevOps_Engineer": 3,
            "Test_Architect": 1,
            "Senior_Test_Engineer": 5,
            "Business_Analyst": 3,
            "Scrum_Master": 2
        },
        "total_size": 41,
        "estimated_monthly_cost_chf": 820000,
        "key_skills_required": ["Java", "Oracle", "Temenos", "Performance Tuning"],
        "duration": "24-36 months"
    },
    
    "Regulatory_Compliance_Team": {
        "name": "FINMA Compliance Squad",
        "composition": {
            "Compliance_Manager": 1,
            "Business_Analyst": 3,
            "Senior_Software_Engineer": 2,
            "Software_Engineer": 3,
            "Risk_Analyst": 2,
            "Test_Engineer": 2
        },
        "total_size": 13,
        "estimated_monthly_cost_chf": 260000,
        "key_skills_required": ["FINMA Regulations", "Basel III", "Reporting", "SQL"],
        "duration": "9-12 months"
    }
}

# 8. COST OPTIMIZATION MODELS
COST_MODELS = {
    "delivery_models": {
        "Onsite_Only": {
            "description": "100% Zurich based team",
            "cost_index": 1.0,
            "advantages": ["Direct client interaction", "No time zone issues", "Cultural alignment"],
            "disadvantages": ["Highest cost", "Limited talent pool", "Scaling challenges"]
        },
        "Hybrid_70_30": {
            "description": "70% Zurich, 30% Offshore",
            "cost_index": 0.82,
            "advantages": ["Cost optimized", "Follow-the-sun support", "Scalability"],
            "disadvantages": ["Coordination overhead", "Some time zone challenges"]
        },
        "Hybrid_50_50": {
            "description": "50% Zurich, 50% Offshore",
            "cost_index": 0.65,
            "advantages": ["Significant cost savings", "Large talent pool", "24/7 capability"],
            "disadvantages": ["Higher coordination effort", "Cultural differences"]
        },
        "Offshore_Led": {
            "description": "30% Zurich, 70% Offshore",
            "cost_index": 0.48,
            "advantages": ["Lowest cost", "Maximum scalability", "Round-the-clock delivery"],
            "disadvantages": ["Client acceptance", "Communication challenges", "Quality concerns"]
        }
    }
}

# 9. GENERATE REALISTIC ASSOCIATE DATA
def generate_associates_data(num_associates=TOTAL_ASSOCIATES):
    """Generate realistic associate data for Swiss banking context"""
    associates = []
    
    # Distribution logic
    location_distribution = {
        "Zurich": 0.25,
        "Geneva": 0.08,
        "Basel": 0.05,
        "Pune": 0.35,
        "Bangalore": 0.17,
        "Chennai": 0.10
    }
    
    for i in range(num_associates):
        # Basic attributes
        associate_id = f"COG{str(i+1).zfill(6)}"
        
        # Location assignment
        location = np.random.choice(
            list(location_distribution.keys()),
            p=list(location_distribution.values())
        )
        
        # Role assignment based on realistic distribution
        role_category = np.random.choice(
            ["Engineering", "Quality", "Leadership", "Specialized", "Analysis", "Project", "Compliance"],
            p=[0.40, 0.20, 0.08, 0.12, 0.10, 0.08, 0.02]
        )
        role = np.random.choice(list(ROLES_HIERARCHY[role_category].keys()))
        role_info = ROLES_HIERARCHY[role_category][role]
        
        # Experience calculation
        base_exp = role_info["min_exp"]
        experience_years = base_exp + np.random.randint(0, 8)
        
        # Skills assignment (realistic combinations)
        primary_skills = []
        if "Engineer" in role or "Developer" in role:
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["Programming_Languages"]["Core_Banking"], 
                size=np.random.randint(2, 4), 
                replace=False
            ))
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["Programming_Languages"]["Modern_Stack"], 
                size=np.random.randint(1, 3), 
                replace=False
            ))
        
        if "Architect" in role:
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["Banking_Platforms"]["Core_Banking"], 
                size=np.random.randint(1, 3), 
                replace=False
            ))
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["Cloud_Platforms"]["Public_Cloud"], 
                size=np.random.randint(1, 2), 
                replace=False
            ))
        
        if "Test" in role:
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["Testing_Tools"]["Automation"], 
                size=np.random.randint(2, 3), 
                replace=False
            ))
        
        if "DevOps" in role:
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["DevOps_Tools"]["CI_CD"], 
                size=np.random.randint(1, 2), 
                replace=False
            ))
            primary_skills.extend(np.random.choice(
                SKILLS_TAXONOMY["DevOps_Tools"]["Containerization"], 
                size=np.random.randint(1, 2), 
                replace=False
            ))
        
        # Banking domain experience
        banking_domains = np.random.choice(
            ["Retail Banking", "Investment Banking", "Private Banking", "Corporate Banking", 
             "Digital Banking", "Risk Management", "Compliance", "Payments"],
            size=np.random.randint(1, 3),
            replace=False
        )
        
        # Language skills (Swiss locations get German/French priority)
        language_skills = {}
        if location in ["Zurich", "Basel"]:
            language_skills["German"] = np.random.choice(["Fluent", "Business", "Native"], p=[0.5, 0.3, 0.2])
            language_skills["English"] = np.random.choice(["Fluent", "Business"], p=[0.7, 0.3])
        elif location == "Geneva":
            language_skills["French"] = np.random.choice(["Fluent", "Business", "Native"], p=[0.5, 0.3, 0.2])
            language_skills["English"] = np.random.choice(["Fluent", "Business"], p=[0.7, 0.3])
        else:
            language_skills["English"] = np.random.choice(["Fluent", "Business"], p=[0.8, 0.2])
            if np.random.random() > 0.7:
                language_skills["German"] = np.random.choice(["Basic", "Business"], p=[0.7, 0.3])
        
        # Certifications
        certs = []
        if experience_years > 5:
            cert_categories = np.random.choice(
                list(CERTIFICATIONS.keys()), 
                size=np.random.randint(1, 3), 
                replace=False
            )
            for cat in cert_categories:
                certs.extend(np.random.choice(
                    CERTIFICATIONS[cat], 
                    size=1
                ))
        
        # Project experience (UBS specific)
        project_exp = np.random.choice(
            list(PROJECT_TYPES.keys()), 
            size=np.random.randint(1, 3), 
            replace=False
        ).tolist()
        
        # Availability calculation
        if location in ["Zurich", "Geneva", "Basel"]:
            # Swiss locations have higher immediate availability
            available_now = np.random.choice([True, False], p=[0.65, 0.35])
            available_1_week = np.random.choice([True, False], p=[0.80, 0.20])
            available_1_month = True
        else:
            # Offshore locations have different availability patterns
            available_now = np.random.choice([True, False], p=[0.45, 0.55])
            available_1_week = np.random.choice([True, False], p=[0.70, 0.30])
            available_1_month = np.random.choice([True, False], p=[0.90, 0.10])
        
        # Visa status (for Swiss locations)
        if location in ["Zurich", "Geneva", "Basel"]:
            visa_status = np.random.choice(
                ["Swiss Citizen", "EU/EFTA Permit", "Swiss Permit B", "Swiss Permit C", "Requires Sponsorship"],
                p=[0.15, 0.25, 0.30, 0.20, 0.10]
            )
        else:
            visa_status = "Not Applicable"
        
        # Day rate calculation
        base_rate = role_info["day_rate_chf"]
        # Adjust for location
        if location in ["Pune", "Bangalore", "Chennai"]:
            day_rate = int(base_rate * 0.4)  # Offshore rates
        else:
            # Adjust for experience and certifications
            exp_multiplier = 1 + (experience_years - role_info["min_exp"]) * 0.02
            cert_multiplier = 1 + len(certs) * 0.05
            day_rate = int(base_rate * exp_multiplier * cert_multiplier)
        
        # Previous client experience
        prev_clients = []
        if experience_years > 3:
            client_pool = ["UBS", "Credit Suisse", "Julius Baer", "Pictet", "Lombard Odier", 
                          "Swiss Re", "Zurich Insurance", "PostFinance", "Raiffeisen", "ZKB"]
            prev_clients = np.random.choice(
                client_pool, 
                size=np.random.randint(1, min(4, experience_years // 2)), 
                replace=False
            ).tolist()
        
        # CS Integration specific experience
        cs_integration_exp = False
        if "Credit Suisse" in prev_clients or "UBS" in prev_clients:
            cs_integration_exp = np.random.choice([True, False], p=[0.7, 0.3])
        
        # Utilization rate
        if available_now:
            utilization_current = 0
        else:
            utilization_current = np.random.choice([100, 80, 60, 40], p=[0.5, 0.3, 0.15, 0.05])
        
        # Build associate record
        associate = {
            "Associate_ID": associate_id,
            "Location": location,
            "Role": role,
            "Role_Category": role_category,
            "Experience_Years": experience_years,
            "Primary_Skills": primary_skills,
            "Banking_Domains": banking_domains.tolist(),
            "Language_Skills": language_skills,
            "Certifications": certs,
            "Project_Experience": project_exp,
            "Available_Now": available_now,
            "Available_1_Week": available_1_week,
            "Available_1_Month": available_1_month,
            "Visa_Status": visa_status,
            "Day_Rate_CHF": day_rate,
            "Previous_Clients": prev_clients,
            "CS_Integration_Experience": cs_integration_exp,
            "Utilization_Current": utilization_current,
            "Last_Updated": datetime.now() - timedelta(days=np.random.randint(0, 30))
        }
        
        associates.append(associate)
    
    return pd.DataFrame(associates)

# 10. SIMPLIFIED DATASET FOR STREAMLIT
def create_streamlit_dataset():
    """Create a simplified dataset optimized for Streamlit"""
    
    # Generate realistic data but in simplified format for the current app structure
    simple_data = []
    
    locations = ["Zurich", "Geneva", "Basel", "Pune", "Bangalore", "Chennai"]
    project_types = ["CS Integration", "Digital Banking", "Core Banking", "Regulatory Compliance", 
                     "Cloud Migration", "API Modernization", "Cybersecurity", "Data Analytics"]
    skills = ["Java", "Python", "Avaloq", "Temenos", "AWS", "DevOps", "Testing", "Security", 
              "Data Analytics", "Mobile", "FINMA Compliance", "German Language"]
    roles = ["Solution Architect", "Technical Lead", "Senior Engineer", "Engineer", 
             "DevOps Engineer", "Test Engineer", "Business Analyst", "Scrum Master"]
    
    # Generate 100 realistic records
    for i in range(100):
        location = np.random.choice(locations, p=[0.25, 0.08, 0.05, 0.35, 0.17, 0.10])
        project_type = np.random.choice(project_types)
        skill = np.random.choice(skills)
        role = np.random.choice(roles)
        
        # Realistic counts based on role and location
        if "Architect" in role:
            base_count = np.random.randint(8, 15)
        elif "Lead" in role:
            base_count = np.random.randint(12, 25)
        elif "Senior" in role:
            base_count = np.random.randint(25, 45)
        else:
            base_count = np.random.randint(35, 75)
        
        # Adjust for location
        if location in ["Pune", "Bangalore", "Chennai"]:
            count = int(base_count * 1.5)  # More offshore resources
        else:
            count = base_count
        
        # Availability calculations
        available_now = int(count * np.random.uniform(0.4, 0.7))
        available_1_month = int(count * np.random.uniform(0.7, 0.9))
        experience_years = np.random.randint(3, 12)
        
        simple_data.append({
            'Project_Type': project_type,
            'Location': location,
            'Skill': skill,
            'Role': role,
            'Count': count,
            'Available_Now': available_now,
            'Available_1_Month': available_1_month,
            'Experience_Years': experience_years
        })
    
    return pd.DataFrame(simple_data)

# 11. ENHANCED NLP QUERY RESPONSES
def enhanced_nlp_response(query, df):
    """Enhanced NLP response function with Swiss banking context"""
    query_lower = query.lower()
    
    # CS Integration specific queries
    if any(term in query_lower for term in ['cs', 'credit suisse', 'integration', 'merger']):
        cs_data = df[df['Project_Type'] == 'CS Integration']
        total = cs_data['Count'].sum()
        available = cs_data['Available_Now'].sum()
        return f"🏦 CS Integration Readiness: {total} specialists across all locations ({available} available immediately). Cognizant has deployed 450+ associates on similar integration projects with 94% success rate."
    
    # UBS specific queries
    if 'ubs' in query_lower:
        total_ubs_ready = df['Count'].sum()
        zurich_ready = df[df['Location'] == 'Zurich']['Available_Now'].sum()
        return f"🎯 UBS Project Readiness: {total_ubs_ready} specialists in our talent pool. {zurich_ready} immediately available in Zurich with Swiss banking domain expertise and FINMA compliance training."
    
    # FINMA/Compliance queries
    if any(term in query_lower for term in ['finma', 'compliance', 'regulatory', 'basel']):
        compliance_data = df[df['Project_Type'] == 'Regulatory Compliance']
        total = compliance_data['Count'].sum()
        return f"⚖️ Regulatory Compliance Experts: {total} specialists with FINMA certification and Basel III expertise. All team members undergo quarterly Swiss banking law updates."
    
    # German language queries
    if any(term in query_lower for term in ['german', 'deutsch', 'zurich']):
        zurich_data = df[df['Location'] == 'Zurich']
        total = zurich_data['Count'].sum()
        available = zurich_data['Available_Now'].sum()
        return f"🇩🇪 German-Speaking Talent in Zurich: {total} associates ({available} available now). 89% have business-level German proficiency for direct client interaction."
    
    # Technology specific queries
    if 'avaloq' in query_lower:
        avaloq_data = df[df['Skill'] == 'Avaloq']
        total = avaloq_data['Count'].sum()
        return f"🏛️ Avaloq Specialists: {total} certified professionals across Switzerland and India. Average 6.5 years Avaloq experience with UBS-specific configuration expertise."
    
    if any(term in query_lower for term in ['cloud', 'aws', 'migration']):
        cloud_data = df[df['Project_Type'] == 'Cloud Migration']
        total = cloud_data['Count'].sum()
        return f"☁️ Cloud Migration Excellence: {total} AWS certified professionals. 67 specialists with AWS Switzerland region expertise and financial services compliance."
    
    # Cost/budget queries
    if any(term in query_lower for term in ['cost', 'budget', 'rate', 'price']):
        return f"💰 Cost Optimization: Our hybrid delivery model (70% Zurich, 30% Offshore) offers 28% cost savings vs. pure onsite. Average blended rate: CHF 980/day vs. market rate CHF 1,350/day."
    
    # Default intelligent response
    return f"💡 Based on our Swiss banking talent pool: {df['Available_Now'].sum()} associates available immediately across {df['Location'].nunique()} locations. Try queries like 'Avaloq developers in Zurich' or 'FINMA compliance experts'."

# Export functions for the main app
__all__ = [
    'SKILLS_TAXONOMY',
    'ROLES_HIERARCHY', 
    'PROJECT_TYPES',
    'TEAM_TEMPLATES',
    'COST_MODELS',
    'create_streamlit_dataset',
    'enhanced_nlp_response'
] 