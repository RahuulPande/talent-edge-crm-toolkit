import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import random

def show_advanced_analytics(df):
    """Advanced Analytics Dashboard with predictive insights and Swiss banking focus"""
    
    st.markdown("## 📊 Advanced Analytics Dashboard")
    st.markdown("### Swiss Banking Intelligence & Predictive Insights")
    
    # Create tabs for different analytics sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Predictive Analytics", 
        "💰 Cost Optimization", 
        "🏦 Compliance Metrics", 
        "📈 Performance Insights"
    ])
    
    with tab1:
        show_predictive_analytics(df)
    
    with tab2:
        show_cost_optimization(df)
    
    with tab3:
        show_compliance_metrics(df)
    
    with tab4:
        show_performance_insights(df)

def show_predictive_analytics(df):
    """Predictive analytics for talent demand and market trends"""
    
    st.markdown("### 🎯 Predictive Analytics")
    
    # Simulate predictive data
    np.random.seed(42)
    months = pd.date_range(start='2024-01-01', end='2025-12-31', freq='M')
    
    # UBS Integration demand prediction
    ubs_demand = np.random.normal(150, 20, len(months)) + np.sin(np.arange(len(months)) * 0.3) * 30
    ubs_demand = np.maximum(ubs_demand, 100)
    
    # CS Integration demand prediction
    cs_demand = np.random.normal(120, 15, len(months)) + np.cos(np.arange(len(months)) * 0.2) * 25
    cs_demand = np.maximum(cs_demand, 80)
    
    # Create prediction dataframe
    prediction_df = pd.DataFrame({
        'Month': months,
        'UBS_Integration_Demand': ubs_demand,
        'CS_Integration_Demand': cs_demand,
        'Total_Demand': ubs_demand + cs_demand
    })
    
    # Demand prediction chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=prediction_df['Month'], 
        y=prediction_df['UBS_Integration_Demand'],
        name='UBS Integration',
        line=dict(color='#0072C6', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=prediction_df['Month'], 
        y=prediction_df['CS_Integration_Demand'],
        name='CS Integration',
        line=dict(color='#00A651', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=prediction_df['Month'], 
        y=prediction_df['Total_Demand'],
        name='Total Demand',
        line=dict(color='#FF6B35', width=4, dash='dash')
    ))
    
    fig.update_layout(
        title='📈 Swiss Banking Talent Demand Forecast (2024-2025)',
        xaxis_title='Month',
        yaxis_title='Demand (Associates)',
        hovermode='x unified',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Peak UBS Demand", 
            f"{int(prediction_df['UBS_Integration_Demand'].max())}",
            f"+{int(prediction_df['UBS_Integration_Demand'].max() - prediction_df['UBS_Integration_Demand'].min())} from baseline"
        )
    
    with col2:
        st.metric(
            "Peak CS Demand", 
            f"{int(prediction_df['CS_Integration_Demand'].max())}",
            f"+{int(prediction_df['CS_Integration_Demand'].max() - prediction_df['CS_Integration_Demand'].min())} from baseline"
        )
    
    with col3:
        st.metric(
            "Total Peak Demand", 
            f"{int(prediction_df['Total_Demand'].max())}",
            f"Combined Swiss banking expertise"
        )

def show_cost_optimization(df):
    """Cost optimization insights and recommendations"""
    
    st.markdown("### 💰 Cost Optimization Insights")
    
    # Calculate cost optimization metrics
    current_avg_rate = df['rate_per_hour'].mean()
    zurich_avg_rate = df[df['location'] == 'Zurich']['rate_per_hour'].mean()
    pune_avg_rate = df[df['location'] == 'Pune']['rate_per_hour'].mean()
    
    # Cost savings potential
    savings_per_hour = zurich_avg_rate - pune_avg_rate
    annual_savings = savings_per_hour * 8 * 220  # 8 hours/day, 220 working days
    
    # Create cost comparison chart
    locations = ['Zurich', 'Pune', 'Bangalore', 'Mumbai']
    avg_rates = [
        df[df['location'] == loc]['rate_per_hour'].mean() 
        for loc in locations
    ]
    
    fig = px.bar(
        x=locations,
        y=avg_rates,
        title='💵 Average Hourly Rates by Location',
        color=avg_rates,
        color_continuous_scale='RdYlGn_r'
    )
    
    fig.update_layout(
        xaxis_title='Location',
        yaxis_title='Average Rate (CHF/hour)',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Cost optimization recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💡 Cost Optimization Recommendations")
        
        st.info(f"""
        **Immediate Savings Opportunity:**
        - **Rate Differential**: CHF {savings_per_hour:.0f}/hour between Zurich and Pune
        - **Annual Savings**: CHF {annual_savings:,.0f} per associate
        - **Team of 10**: CHF {annual_savings * 10:,.0f} annual savings
        """)
        
        st.success(f"""
        **Recommended Actions:**
        1. **Hybrid Teams**: 70% Pune + 30% Zurich
        2. **Skill Transfer**: Train Pune team on Swiss banking
        3. **Cost Savings**: 28% reduction in project costs
        """)
    
    with col2:
        st.markdown("#### 📊 Cost Breakdown")
        
        # Create pie chart for cost distribution
        cost_data = {
            'Zurich Associates': len(df[df['location'] == 'Zurich']) * zurich_avg_rate * 8 * 220,
            'Pune Associates': len(df[df['location'] == 'Pune']) * pune_avg_rate * 8 * 220,
            'Other Locations': len(df[~df['location'].isin(['Zurich', 'Pune'])]) * current_avg_rate * 8 * 220
        }
        
        fig = px.pie(
            values=list(cost_data.values()),
            names=list(cost_data.keys()),
            title='Annual Cost Distribution'
        )
        
        st.plotly_chart(fig, use_container_width=True)

def show_compliance_metrics(df):
    """Swiss banking compliance metrics and regulatory insights"""
    
    st.markdown("### 🏦 Swiss Banking Compliance Metrics")
    
    # Simulate compliance data
    compliance_data = {
        'FINMA Compliance': 98.5,
        'GDPR Compliance': 99.2,
        'Swiss Banking Act': 97.8,
        'Anti-Money Laundering': 99.7,
        'Data Protection': 98.9,
        'Risk Management': 96.3
    }
    
    # Compliance radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(compliance_data.values()),
        theta=list(compliance_data.keys()),
        fill='toself',
        name='Compliance Score',
        line_color='#0072C6'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[90, 100]
            )),
        showlegend=False,
        title='🏦 Swiss Banking Compliance Metrics'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Compliance insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📋 Compliance Highlights")
        
        st.success(f"""
        **✅ Excellent Compliance:**
        - **FINMA**: {compliance_data['FINMA Compliance']}% compliant
        - **GDPR**: {compliance_data['GDPR Compliance']}% compliant
        - **AML**: {compliance_data['Anti-Money Laundering']}% compliant
        """)
        
        st.warning(f"""
        **⚠️ Areas for Improvement:**
        - **Risk Management**: {compliance_data['Risk Management']}% (target: 99%)
        - **Swiss Banking Act**: {compliance_data['Swiss Banking Act']}% (target: 99%)
        """)
    
    with col2:
        st.markdown("#### 🔍 Regulatory Insights")
        
        # Certification distribution
        cert_data = df['certifications'].value_counts().sort_index()
        
        fig = px.bar(
            x=cert_data.index,
            y=cert_data.values,
            title='Professional Certifications Distribution',
            labels={'x': 'Number of Certifications', 'y': 'Number of Associates'}
        )
        
        st.plotly_chart(fig, use_container_width=True)

def show_performance_insights(df):
    """Performance analytics and team insights"""
    
    st.markdown("### 📈 Performance Insights")
    
    # Performance metrics by location
    performance_metrics = df.groupby('location').agg({
        'experience_years': 'mean',
        'rate_per_hour': 'mean',
        'certifications': 'mean'
    }).round(2)
    
    # Performance heatmap
    fig = px.imshow(
        performance_metrics.T,
        title='🏆 Performance Metrics by Location',
        aspect='auto',
        color_continuous_scale='RdYlGn'
    )
    
    fig.update_layout(
        xaxis_title='Location',
        yaxis_title='Metrics'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Team performance insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Top Performers")
        
        # Top 5 by experience and certifications
        top_performers = df.nlargest(5, ['experience_years', 'certifications'])
        
        fig = px.scatter(
            top_performers,
            x='experience_years',
            y='certifications',
            size='rate_per_hour',
            color='location',
            hover_data=['name'],
            title='Top Performers by Experience & Certifications'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 Skill Distribution")
        
        # Skill distribution
        skill_dist = df['primary_skill'].value_counts()
        
        fig = px.pie(
            values=skill_dist.values,
            names=skill_dist.index,
            title='Primary Skills Distribution'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance recommendations
    st.markdown("#### 💡 Performance Recommendations")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Avg Experience", 
            f"{df['experience_years'].mean():.1f} years",
            f"Target: 8+ years for Swiss banking"
        )
    
    with col2:
        st.metric(
            "Avg Certifications", 
            f"{df['certifications'].mean():.1f}",
            f"Target: 2+ certifications"
        )
    
    with col3:
        st.metric(
            "High Performers", 
            f"{len(df[df['experience_years'] >= 8])}",
            f"Out of {len(df)} total"
        )

# Export the function for use in main app
if __name__ == "__main__":
    st.title("Advanced Analytics Module")
    st.write("This module provides advanced analytics for the CRM toolkit.") 