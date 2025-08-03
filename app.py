import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import time
from advanced_analytics import show_advanced_analytics

# Page configuration
st.set_page_config(
    page_title="Cognizant Talent Edge CRM Toolkit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# DROPDOWN VISIBILITY FIX - Apply immediately after page config
dropdown_style_fix = """
<style>
    /* Force all selectbox text to be visible with maximum specificity */
    
    /* Main container fix */
    .stSelectbox > div > div {
        background-color: white !important;
    }
    
    /* The input field that shows selected value */
    .stSelectbox [data-baseweb="select"] [data-baseweb="input"] {
        color: black !important;
        -webkit-text-fill-color: black !important;
        opacity: 1 !important;
    }
    
    /* Alternative selector for the displayed value */
    .stSelectbox [data-baseweb="select"] > div > div > div:first-child {
        color: black !important;
        -webkit-text-fill-color: black !important;
        opacity: 1 !important;
    }
    
    /* The actual value container */
    div[data-baseweb="select"] [class*="valueContainer"] {
        color: black !important;
    }
    
    /* Single value display */
    div[data-baseweb="select"] [class*="singleValue"] {
        color: black !important;
        opacity: 1 !important;
    }
    
    /* For the placeholder text */
    div[data-baseweb="select"] [class*="placeholder"] {
        color: #666666 !important;
        opacity: 1 !important;
    }
    
    /* Target the specific baseweb classes */
    [class*="css"][class*="singleValue"] {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* Override any inherited styles */
    .stSelectbox * {
        color: inherit !important;
    }
    
    .stSelectbox [data-baseweb="select"] * {
        -webkit-text-fill-color: initial !important;
    }
    
    /* Ensure text is visible in all states */
    .stSelectbox [data-baseweb="select"]:not([data-baseweb="popover"]) {
        color: black !important;
    }
    
    /* Target the input specifically */
    .stSelectbox input[aria-autocomplete="list"] {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* For any div containing the selected text */
    .stSelectbox [data-baseweb="select"] > div:first-child > div:first-child {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* Additional fix for nested divs */
    .stSelectbox [data-baseweb="select"] div[style*="color"] {
        color: black !important;
    }
    
    /* Override inline styles */
    .stSelectbox [style*="color: rgb(255, 255, 255)"] {
        color: black !important;
    }
    
    /* Dropdown menu items (these should remain visible) */
    div[data-baseweb="popover"] li {
        color: black !important;
        background-color: white !important;
    }
    
    div[data-baseweb="popover"] li:hover {
        background-color: #f0f7ff !important;
        color: #0072C6 !important;
    }
    
    /* Enhanced fixes for Safari and Chrome */
    .stSelectbox [data-baseweb="select"] div[role="combobox"] {
        color: black !important;
    }
    
    .stSelectbox [data-baseweb="select"] div[aria-expanded] {
        color: black !important;
    }
    
    /* Fix for radio buttons in sidebar */
    .stSidebar .stRadio > label {
        color: black !important;
    }
    
    .stSidebar .stRadio > div[role="radiogroup"] > label {
        color: black !important;
    }
    
    /* Fix for multiselect */
    .stMultiSelect [data-baseweb="select"] {
        color: black !important;
    }
    
    /* Force all text in selectboxes to be black */
    .stSelectbox * {
        color: black !important;
    }
    
    /* Override any white text */
    .stSelectbox [style*="color: white"],
    .stSelectbox [style*="color: rgb(255, 255, 255)"],
    .stSelectbox [style*="color: #ffffff"] {
        color: black !important;
    }
</style>
"""

# JavaScript backup fix for dynamic elements
js_fix = """
<script>
    // Force dropdown text to be visible
    function fixDropdownVisibility() {
        // Find all selectbox inputs
        const selectInputs = document.querySelectorAll('[data-baseweb="select"] input');
        selectInputs.forEach(input => {
            input.style.color = 'black';
            input.style.webkitTextFillColor = 'black';
        });
        
        // Find all value containers
        const valueContainers = document.querySelectorAll('[data-baseweb="select"] [class*="valueContainer"]');
        valueContainers.forEach(container => {
            container.style.color = 'black';
            container.style.webkitTextFillColor = 'black';
        });
        
        // Find any element that might contain the selected value
        const selectDivs = document.querySelectorAll('.stSelectbox [data-baseweb="select"] > div > div');
        selectDivs.forEach(div => {
            if (div.textContent && !div.querySelector('input')) {
                div.style.color = 'black';
                div.style.webkitTextFillColor = 'black';
            }
        });
        
        // Enhanced fix for all dropdown elements
        const allDropdownElements = document.querySelectorAll('.stSelectbox [data-baseweb="select"] *');
        allDropdownElements.forEach(element => {
            if (element.textContent && element.textContent.trim() !== '') {
                element.style.color = 'black';
                element.style.webkitTextFillColor = 'black';
            }
        });
        
        // Fix for radio buttons in sidebar
        const radioLabels = document.querySelectorAll('.stSidebar .stRadio label');
        radioLabels.forEach(label => {
            label.style.color = 'black';
        });
        
        // Fix for multiselect elements
        const multiSelectElements = document.querySelectorAll('.stMultiSelect [data-baseweb="select"] *');
        multiSelectElements.forEach(element => {
            if (element.textContent && element.textContent.trim() !== '') {
                element.style.color = 'black';
                element.style.webkitTextFillColor = 'black';
            }
        });
    }
    
    // Run the fix initially
    setTimeout(fixDropdownVisibility, 100);
    
    // Run the fix whenever the DOM changes
    const observer = new MutationObserver(fixDropdownVisibility);
    observer.observe(document.body, { 
        childList: true, 
        subtree: true,
        attributes: true,
        attributeFilter: ['style', 'class']
    });
    
    // Also run on click events
    document.addEventListener('click', () => {
        setTimeout(fixDropdownVisibility, 50);
    });
    
    // Run on focus events
    document.addEventListener('focusin', () => {
        setTimeout(fixDropdownVisibility, 25);
    });
    
    // Run periodically to catch any missed elements
    setInterval(fixDropdownVisibility, 2000);
</script>
"""

# Apply both fixes immediately
st.markdown(dropdown_style_fix, unsafe_allow_html=True)
st.markdown(js_fix, unsafe_allow_html=True)

# Enhanced CSS with animations and professional styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated header */
    .main-header {
        background: linear-gradient(90deg, #0072C6 0%, #005a9e 100%);
        color: white;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        padding: 2rem;
        margin: -1rem -5rem 2rem -5rem;
        box-shadow: 0 4px 20px rgba(0, 114, 198, 0.3);
        position: relative;
        overflow: hidden;
        animation: slideDown 0.8s ease-out;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    @keyframes slideDown {
        from { transform: translateY(-100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .sub-header {
        color: white;
        font-size: 1.3rem;
        font-weight: 300;
        text-align: center;
        margin-top: -1rem;
        opacity: 0.9;
    }
    
    /* Card styling with hover effects */
    div[data-testid="metric-container"] {
        background: white;
        border: none;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 114, 198, 0.2);
    }
    
    div[data-testid="metric-container"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #0072C6, #D40511);
        transform: scaleX(0);
        transition: transform 0.3s;
    }
    
    div[data-testid="metric-container"]:hover::before {
        transform: scaleX(1);
    }
    
    /* Enhanced buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0072C6 0%, #005a9e 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 30px;
        box-shadow: 0 4px 15px rgba(0, 114, 198, 0.3);
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 114, 198, 0.4);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:active::before {
        width: 300px;
        height: 300px;
    }
    
    /* UBS accent button */
    .accent-button > button {
        background: linear-gradient(135deg, #D40511 0%, #b00410 100%);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 4px 15px rgba(212, 5, 17, 0.3); }
        50% { box-shadow: 0 4px 25px rgba(212, 5, 17, 0.5); }
        100% { box-shadow: 0 4px 15px rgba(212, 5, 17, 0.3); }
    }
    
    /* Success messages with animation */
    .success-msg {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        display: inline-block;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* Enhanced sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        box-shadow: 4px 0 10px rgba(0, 0, 0, 0.1);
    }
    
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* Fix radio button text visibility in sidebar */
    section[data-testid="stSidebar"] .stRadio > label {
        color: white !important;
        font-weight: 500;
    }
    
    section[data-testid="stSidebar"] [data-baseweb="radio"] > div {
        color: white !important;
    }
    
    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label {
        color: white !important;
        font-size: 1.1rem;
        padding: 0.5rem 0;
        transition: all 0.3s;
    }
    
    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label:hover {
        color: #4CAF50 !important;
        transform: translateX(5px);
    }
    
    /* Input fields */
    .stSelectbox > div > div,
    .stTextInput > div > div > input {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 0.5rem;
        transition: all 0.3s;
    }
    
    .stTextInput > div > div > input {
        color: #1a1a1a !important;
    }
    
    /* Focus states */
    .stSelectbox > div > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: #0072C6;
        box-shadow: 0 0 0 3px rgba(0, 114, 198, 0.1);
    }
    
    /* Data tables */
    .dataframe {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    .dataframe thead th {
        background: linear-gradient(135deg, #0072C6 0%, #005a9e 100%);
        color: white !important;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 1rem !important;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(0, 114, 198, 0.05);
        transition: background 0.3s;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 50px;
        padding: 0.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 30px;
        color: #666;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0072C6 0%, #005a9e 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(0, 114, 198, 0.3);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .info-box::before {
        content: '💡';
        position: absolute;
        top: -20px;
        right: -20px;
        font-size: 100px;
        opacity: 0.1;
    }
    
    /* Loading animation */
    .loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(0, 114, 198, 0.3);
        border-radius: 50%;
        border-top-color: #0072C6;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Floating badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-left: 0.5rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Executive summary box */
    .executive-summary {
        background: white;
        border-left: 5px solid #0072C6;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
        position: relative;
    }
    
    .executive-summary h3 {
        color: #0072C6;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .executive-summary::before {
        content: '📊';
        position: absolute;
        top: 1rem;
        right: 1rem;
        font-size: 2rem;
        opacity: 0.5;
    }
    
    /* Stat cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .stat-card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0, 114, 198, 0.2);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #0072C6 0%, #D40511 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        color: #666;
        font-size: 1rem;
        font-weight: 500;
    }
    
    /* Progress bars */
    .progress-bar {
        width: 100%;
        height: 20px;
        background: #f0f0f0;
        border-radius: 10px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #0072C6 0%, #D40511 100%);
        border-radius: 10px;
        animation: fillProgress 1.5s ease-out;
    }
    
    @keyframes fillProgress {
        from { width: 0; }
    }
</style>

""", unsafe_allow_html=True)

# Initialize session state
if 'query_results' not in st.session_state:
    st.session_state.query_results = None
if 'loading' not in st.session_state:
    st.session_state.loading = False

# Import enhanced data structure
from enhanced_data_structure import (
    create_streamlit_dataset, 
    enhanced_nlp_response,
    TEAM_TEMPLATES,
    COST_MODELS,
    PROJECT_TYPES
)

# Enhanced mock data with comprehensive Swiss banking structure
@st.cache_data
def create_mock_data():
    """Create comprehensive Swiss banking talent data"""
    return create_streamlit_dataset()

# Enhanced NLP response function
def mock_nlp_response(query):
    with st.spinner('🤖 AI analyzing your query...'):
        time.sleep(1)  # Simulate processing
    
    df = create_mock_data()
    return enhanced_nlp_response(query, df)

# PDF Export Function with enhanced styling
def generate_pdf_report(data, query_params):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#0072C6'),
        spaceAfter=30,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#666666'),
        spaceAfter=30,
        alignment=1
    )
    
    # Title
    elements.append(Paragraph("COGNIZANT TALENT REPORT", title_style))
    elements.append(Paragraph("Executive Summary for UBS Engagement", subtitle_style))
    elements.append(Spacer(1, 30))
    
    # Executive Summary Box
    summary_data = [
        ['EXECUTIVE SUMMARY', ''],
        ['Total Associates Found:', f"{data['Count'].sum()}"],
        ['Immediate Availability:', f"{data['Available_Now'].sum()} ({round(data['Available_Now'].sum()/data['Count'].sum()*100)}%)"],
        ['Average Experience:', f"{data['Experience_Years'].mean():.1f} years"],
        ['Deployment Readiness:', 'HIGH - Teams ready within 24-48 hours']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 3*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0072C6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8f9fa')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 30))
    
    # Query Parameters
    elements.append(Paragraph("<b>SEARCH CRITERIA</b>", styles['Heading2']))
    param_data = [
        ['Parameter', 'Value'],
        ['Date:', datetime.now().strftime('%Y-%m-%d %H:%M')],
        ['Project Type:', query_params.get('project_type', 'All')],
        ['Skill:', query_params.get('skill', 'All')],
        ['Location:', query_params.get('location', 'All')],
        ['Role:', query_params.get('role', 'All')]
    ]
    
    param_table = Table(param_data, colWidths=[2*inch, 4*inch])
    param_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#666666')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0'))
    ]))
    elements.append(param_table)
    elements.append(Spacer(1, 30))
    
    # Detailed Results
    elements.append(Paragraph("<b>DETAILED TALENT BREAKDOWN</b>", styles['Heading2']))
    if not data.empty:
        table_data = [['Project', 'Location', 'Skill', 'Role', 'Total', 'Available Now', '1 Month', 'Avg Exp']]
        for _, row in data.iterrows():
            table_data.append([
                row['Project_Type'], row['Location'], row['Skill'], row['Role'],
                str(row['Count']), str(row['Available_Now']), str(row['Available_1_Month']),
                f"{row['Experience_Years']}y"
            ])
        
        detail_table = Table(table_data)
        detail_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0072C6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
        ]))
        elements.append(detail_table)
    
    # Footer
    elements.append(Spacer(1, 50))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        alignment=1
    )
    elements.append(Paragraph("© 2025 Cognizant Technology Solutions. Confidential and Proprietary.", footer_style))
    
    doc.build(elements)
    buffer.seek(0)
    return buffer

# Header with animation
st.markdown("""
<div class="main-header">
    Cognizant Talent Edge CRM Toolkit
    <div class="sub-header">Empower CRMs to showcase associate skills and availability for UBS projects</div>
</div>
""", unsafe_allow_html=True)

# Sidebar with enhanced styling
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h1 style='color: white; font-size: 1.8rem; margin-bottom: 0;'>🚀 Talent Edge</h1>
        <p style='color: #aaa; font-size: 0.9rem;'>CRM Toolkit v2.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation with icons
    page = st.radio(
        "Navigate",
        ["🏠 Dashboard", "🔍 Project Query", "📊 Visualizations", "📅 Availability", "📊 Advanced Analytics", "❓ Help"],
        label_visibility="collapsed"
    )
    
    # Add some stats in sidebar
    st.markdown("---")
    st.markdown("### 📈 Quick Stats")
    df_temp = create_mock_data()
    total_associates = df_temp['Count'].sum()
    total_available = df_temp['Available_Now'].sum()
    
    st.markdown(f"""
    <div class='stat-card' style='margin: 1rem 0;'>
        <div class='stat-number'>{total_associates}</div>
        <div class='stat-label'>Total Associates</div>
    </div>
    <div class='stat-card' style='margin: 1rem 0;'>
        <div class='stat-number'>{round(total_available/total_associates*100)}%</div>
        <div class='stat-label'>Available Now</div>
    </div>
    """, unsafe_allow_html=True)

# Load data
df = create_mock_data()

# Main content based on selected page
if page == "🏠 Dashboard":
    # Executive Summary at the top
    st.markdown("""
    <div class="executive-summary">
        <h3>Executive Summary</h3>
        <p><strong>UBS Talent Readiness:</strong> 1,385 specialists across critical project areas with 61% immediate availability. 
        Our Zurich hub maintains 895 associates optimized for Swiss financial regulations and UBS-specific requirements.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced metrics with progress bars
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        zurich_total = df[df['Location'] == 'Zurich']['Count'].sum()
        zurich_available = df[df['Location'] == 'Zurich']['Available_Now'].sum()
        zurich_percent = round(zurich_available/zurich_total*100) if zurich_total > 0 else 0
        st.metric("🏢 Zurich Hub", f"{zurich_total}", f"↑ {zurich_percent}% Available")
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {zurich_percent}%"></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pune_total = df[df['Location'] == 'Pune']['Count'].sum()
        pune_available = df[df['Location'] == 'Pune']['Available_Now'].sum()
        pune_percent = round(pune_available/pune_total*100) if pune_total > 0 else 0
        st.metric("🌏 Pune Center", f"{pune_total}", f"↑ {pune_percent}% Available")
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {pune_percent}%"></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        ai_total = df[df['Skill'] == 'Data Analytics']['Count'].sum()
        ai_available = df[df['Skill'] == 'Data Analytics']['Available_Now'].sum()
        ai_percent = round(ai_available/ai_total*100) if ai_total > 0 else 0
        st.metric("🤖 AI Specialists", f"{ai_total}", f"↑ {ai_percent}% Available")
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {ai_percent}%"></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        ubs_projects = df[df['Project_Type'].isin(['CS Integration', 'Core Banking'])]['Count'].sum()
        ubs_available = df[df['Project_Type'].isin(['CS Integration', 'Core Banking'])]['Available_Now'].sum()
        ubs_percent = round(ubs_available/ubs_projects*100) if ubs_projects > 0 else 0
        st.metric("🏦 UBS Ready", f"{ubs_projects}", f"↑ {ubs_percent}% Available")
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {ubs_percent}%"></div>
        </div>
        """, unsafe_allow_html=True)
    
    # Two columns for charts and AI query
    col_left, col_right = st.columns([1.5, 1])
    
    with col_left:
        # Enhanced skill distribution chart
        st.markdown("### 🎯 Skill Distribution Analysis")
        skill_dist = df.groupby('Skill')['Count'].sum().reset_index()
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=skill_dist['Skill'],
            values=skill_dist['Count'],
            hole=0.4,
            marker=dict(
                colors=['#0072C6', '#D40511', '#4CAF50', '#FF9800', '#9C27B0'],
                line=dict(color='white', width=2)
            ),
            textposition='inside',
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Associates: %{value}<br>Percentage: %{percent}<extra></extra>'
        )])
        
        fig_pie.update_layout(
            showlegend=True,
            height=400,
            font=dict(size=14, family="Inter"),
            annotations=[dict(text='Skills', x=0.5, y=0.5, font_size=20, showarrow=False)],
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col_right:
        # AI-Powered Query Section with enhanced UI
        st.markdown("### 🤖 AI-Powered Insights")
        st.markdown("""
        <div class="info-box">
            <p style="margin: 0;"><strong>Claude AI Integration</strong><br>
            Ask natural language questions about our talent pool</p>
        </div>
        """, unsafe_allow_html=True)
        
        nlp_query = st.text_input(
            "Ask AI about talent",
            placeholder="Try: 'AI specialists for UBS' or 'Mobile developers in Zurich'",
            key="nlp_input",
            label_visibility="hidden"
        )
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔍 Analyze", type="primary", use_container_width=True):
                if nlp_query:
                    response = mock_nlp_response(nlp_query)
                    st.markdown(f'<div class="success-msg">{response}</div>', unsafe_allow_html=True)
        
        with col_btn2:
            if st.button("💡 Suggest", use_container_width=True):
                suggestions = [
                    "Python developers for trading systems",
                    "Cybersecurity experts available now",
                    "Pega specialists in Zurich"
                ]
                st.info(f"Try: {suggestions[datetime.now().second % 3]}")
    
    # Team Templates Section
    st.markdown("### 🎯 Pre-Configured Team Templates")
    
    template_cols = st.columns(2)
    with template_cols[0]:
        cs_team = TEAM_TEMPLATES["CS_Integration_Squad"]
        st.markdown(f"""
        <div class="stat-card">
            <h4 style="color: #0072C6;">🏦 {cs_team['name']}</h4>
            <div class="stat-number">{cs_team['total_size']}</div>
            <div class="stat-label">Team Members</div>
            <p style="margin: 0.5rem 0; font-size: 0.9rem;">
                Monthly Cost: CHF {cs_team['estimated_monthly_cost_chf']:,}<br>
                Duration: {cs_team['duration']}<br>
                Key Skills: {', '.join(cs_team['key_skills_required'][:2])}...
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with template_cols[1]:
        digital_team = TEAM_TEMPLATES["Digital_Banking_Team"]
        st.markdown(f"""
        <div class="stat-card">
            <h4 style="color: #D40511;">🚀 {digital_team['name']}</h4>
            <div class="stat-number">{digital_team['total_size']}</div>
            <div class="stat-label">Team Members</div>
            <p style="margin: 0.5rem 0; font-size: 0.9rem;">
                Monthly Cost: CHF {digital_team['estimated_monthly_cost_chf']:,}<br>
                Duration: {digital_team['duration']}<br>
                Key Skills: {', '.join(digital_team['key_skills_required'][:2])}...
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cost Optimization Insights
    st.markdown("### 💰 Cost Optimization Models")
    
    cost_cols = st.columns(3)
    hybrid_model = COST_MODELS["delivery_models"]["Hybrid_70_30"]
    onsite_model = COST_MODELS["delivery_models"]["Onsite_Only"]
    offshore_model = COST_MODELS["delivery_models"]["Offshore_Led"]
    
    with cost_cols[0]:
        st.markdown(f"""
        <div class="stat-card">
            <h4 style="color: #4CAF50;">💼 Recommended: {hybrid_model['description']}</h4>
            <div class="stat-number">{int((1-hybrid_model['cost_index'])*100)}%</div>
            <div class="stat-label">Cost Savings vs Onsite</div>
            <p style="margin: 0.5rem 0; font-size: 0.85rem;">
                {hybrid_model['advantages'][0]}<br>
                {hybrid_model['advantages'][1]}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cost_cols[1]:
        st.markdown(f"""
        <div class="stat-card">
            <h4 style="color: #0072C6;">🏢 Premium: {onsite_model['description']}</h4>
            <div class="stat-number">0%</div>
            <div class="stat-label">Baseline Cost Model</div>
            <p style="margin: 0.5rem 0; font-size: 0.85rem;">
                {onsite_model['advantages'][0]}<br>
                {onsite_model['advantages'][1]}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cost_cols[2]:
        st.markdown(f"""
        <div class="stat-card">
            <h4 style="color: #FF9800;">🌏 Economy: {offshore_model['description']}</h4>
            <div class="stat-number">{int((1-offshore_model['cost_index'])*100)}%</div>
            <div class="stat-label">Maximum Savings</div>
            <p style="margin: 0.5rem 0; font-size: 0.85rem;">
                {offshore_model['advantages'][0]}<br>
                {offshore_model['advantages'][1]}
            </p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🔍 Project Query":
    st.markdown("### 🔍 Advanced Talent Search")
    st.markdown("""
    <div class="info-box">
        <p style="margin: 0;">🎯 <strong>Pro Tip:</strong> Combine filters to find the perfect team for your UBS project. 
        Our AI-powered matching ensures optimal resource allocation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter section with enhanced styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        project_type = st.selectbox(
            "🏗️ Project Type",
            ["All"] + sorted(df['Project_Type'].unique().tolist()),
            help="Select the UBS project category"
        )
    
    with col2:
        skill = st.selectbox(
            "💻 Required Skill",
            ["All"] + sorted(df['Skill'].unique().tolist()),
            help="Primary technical skill needed"
        )
    
    with col3:
        role = st.selectbox(
            "👥 Role",
            ["All"] + sorted(df['Role'].unique().tolist()),
            help="Developer or Tester role"
        )
    
    with col4:
        location = st.selectbox(
            "📍 Location",
            ["All"] + sorted(df['Location'].unique().tolist()),
            help="Preferred delivery center"
        )
    
    # Search section
    st.markdown("---")
    col_search, col_space = st.columns([1, 3])
    
    with col_search:
        st.markdown('<div class="accent-button">', unsafe_allow_html=True)
        search_clicked = st.button("🔍 Search Talent", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if search_clicked:
        with st.spinner('🔄 Analyzing talent database...'):
            time.sleep(0.5)  # Simulate search
        
        # Filter data
        filtered_df = df.copy()
        
        if project_type != "All":
            filtered_df = filtered_df[filtered_df['Project_Type'] == project_type]
        if skill != "All":
            filtered_df = filtered_df[filtered_df['Skill'] == skill]
        if role != "All":
            filtered_df = filtered_df[filtered_df['Role'] == role]
        if location != "All":
            filtered_df = filtered_df[filtered_df['Location'] == location]
        
        if not filtered_df.empty:
            st.session_state.query_results = filtered_df
            
            # Results summary with animation
            total_found = filtered_df['Count'].sum()
            available_now = filtered_df['Available_Now'].sum()
            avg_exp = filtered_df['Experience_Years'].mean()
            
            # Executive summary of results
            st.markdown(f"""
            <div class="executive-summary">
                <h3>Search Results Summary</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 1rem;">
                    <div>
                        <div class="stat-number">{total_found}</div>
                        <div class="stat-label">Total Associates</div>
                    </div>
                    <div>
                        <div class="stat-number">{available_now}</div>
                        <div class="stat-label">Available Now</div>
                    </div>
                    <div>
                        <div class="stat-number">{avg_exp:.1f}y</div>
                        <div class="stat-label">Avg Experience</div>
                    </div>
                    <div>
                        <div class="stat-number">{round(available_now/total_found*100) if total_found > 0 else 0}%</div>
                        <div class="stat-label">Availability Rate</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Enhanced data display
            display_df = filtered_df[['Project_Type', 'Location', 'Skill', 'Role', 'Count', 'Available_Now', 'Available_1_Month', 'Experience_Years']]
            display_df = display_df.rename(columns={
                'Project_Type': 'Project',
                'Available_Now': 'Immediate',
                'Available_1_Month': '1 Month',
                'Experience_Years': 'Avg Exp (Years)'
            })
            
            st.markdown("### 📊 Detailed Results")
            st.dataframe(
                display_df.style.background_gradient(subset=['Count', 'Immediate'], cmap='Blues'),
                use_container_width=True,
                height=400
            )
            
            # Action buttons
            col_pdf, col_excel, col_schedule = st.columns(3)
            
            with col_pdf:
                query_params = {
                    'project_type': project_type,
                    'skill': skill,
                    'role': role,
                    'location': location
                }
                
                pdf_buffer = generate_pdf_report(filtered_df, query_params)
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_buffer,
                    file_name=f"talent_report_ubs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            
            with col_excel:
                if st.button("📊 Export to Excel", use_container_width=True):
                    st.info("Excel export ready for download")
            
            with col_schedule:
                if st.button("📅 Schedule Discussion", use_container_width=True):
                    st.success("Meeting request sent to resource managers")
        else:
            st.warning("⚠️ No results found. Try adjusting your filters for better matches.")
    
    # Team Builder Section
    st.markdown("---")
    st.markdown("### 🏗️ Smart Team Builder")
    st.markdown("""
    <div class="info-box">
        <p style="margin: 0;">⚡ <strong>Pre-Configured Teams:</strong> Select from proven team templates optimized for Swiss banking projects.</p>
    </div>
    """, unsafe_allow_html=True)
    
    team_cols = st.columns([2, 1])
    
    with team_cols[0]:
        selected_template = st.selectbox(
            "🎯 Select Team Template",
            list(TEAM_TEMPLATES.keys()),
            format_func=lambda x: TEAM_TEMPLATES[x]["name"],
            help="Choose from pre-configured team templates"
        )
        
        if selected_template:
            template = TEAM_TEMPLATES[selected_template]
            
            st.markdown(f"#### 📋 {template['name']} Composition")
            
            # Team composition table
            composition_data = []
            for role, count in template['composition'].items():
                composition_data.append({
                    'Role': role.replace('_', ' '),
                    'Count': count,
                    'Specialization': 'Swiss Banking Expert' if count <= 2 else 'Banking Professional'
                })
            
            composition_df = pd.DataFrame(composition_data)
            st.dataframe(composition_df, use_container_width=True, height=300)
    
    with team_cols[1]:
        if selected_template:
            template = TEAM_TEMPLATES[selected_template]
            
            st.markdown("""
            <div class="stat-card">
                <h4>📊 Team Summary</h4>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("👥 Total Team Size", template['total_size'])
            st.metric("💰 Monthly Cost (CHF)", f"{template['estimated_monthly_cost_chf']:,}")
            st.metric("⏱️ Duration", template['duration'])
            
            st.markdown("**🎯 Key Skills Required:**")
            for skill in template['key_skills_required']:
                st.markdown(f"- {skill}")
            
            if st.button("🚀 Build This Team", type="primary", use_container_width=True):
                st.markdown("""
                <div class="success-msg">
                    ✅ Team configuration saved! Resource allocation initiated for immediate deployment.
                </div>
                """, unsafe_allow_html=True)
                
                st.info(f"""
                **Next Steps:**
                1. Team matching algorithm activated
                2. Swiss visa status verification in progress
                3. FINMA compliance check scheduled
                4. Client onboarding timeline: 5-7 business days
                """)
    
    # Cost Calculator
    st.markdown("---")
    st.markdown("### 💰 Advanced Cost Calculator")
    
    calc_cols = st.columns(3)
    
    with calc_cols[0]:
        delivery_model = st.selectbox(
            "🌍 Delivery Model",
            list(COST_MODELS["delivery_models"].keys()),
            format_func=lambda x: COST_MODELS["delivery_models"][x]["description"]
        )
    
    with calc_cols[1]:
        project_duration = st.slider("📅 Project Duration (months)", 6, 36, 18)
    
    with calc_cols[2]:
        team_size = st.slider("👥 Team Size", 5, 50, 20)
    
    if st.button("🧮 Calculate Costs", use_container_width=True):
        model = COST_MODELS["delivery_models"][delivery_model]
        
        # Base cost calculation (simplified)
        base_monthly_cost = team_size * 22 * 1200  # Avg daily rate * working days
        adjusted_cost = int(base_monthly_cost * model["cost_index"])
        total_project_cost = adjusted_cost * project_duration
        
        st.markdown(f"""
        <div class="executive-summary">
            <h3>💼 Cost Projection: {model['description']}</h3>
            <div style="display: flex; justify-content: space-around; margin-top: 1rem;">
                <div>
                    <div class="stat-number">CHF {adjusted_cost:,}</div>
                    <div class="stat-label">Monthly Cost</div>
                </div>
                <div>
                    <div class="stat-number">CHF {total_project_cost:,}</div>
                    <div class="stat-label">Total Project Cost</div>
                </div>
                <div>
                    <div class="stat-number">{int((1-model['cost_index'])*100)}%</div>
                    <div class="stat-label">Savings vs Pure Onsite</div>
                </div>
            </div>
            <p style="margin-top: 1rem;"><strong>Model Benefits:</strong> {', '.join(model['advantages'])}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📊 Visualizations":
    st.markdown("### 📊 Executive Analytics Dashboard")
    
    # Tabs for different visualizations
    viz_tabs = st.tabs(["🌍 Geographic Distribution", "💼 Project Analysis", "📈 Trend Analysis", "🎯 Skill Matrix"])
    
    with viz_tabs[0]:
        # Geographic visualization
        st.markdown("#### Associate Distribution by Location")
        
        location_summary = df.groupby('Location').agg({
            'Count': 'sum',
            'Available_Now': 'sum'
        }).reset_index()
        
        fig_geo = go.Figure()
        
        # Add bars for total count
        fig_geo.add_trace(go.Bar(
            name='Total Associates',
            x=location_summary['Location'],
            y=location_summary['Count'],
            marker_color='#0072C6',
            text=location_summary['Count'],
            textposition='outside'
        ))
        
        # Add bars for available now
        fig_geo.add_trace(go.Bar(
            name='Available Now',
            x=location_summary['Location'],
            y=location_summary['Available_Now'],
            marker_color='#4CAF50',
            text=location_summary['Available_Now'],
            textposition='outside'
        ))
        
        fig_geo.update_layout(
            barmode='group',
            height=500,
            title={
                'text': 'Talent Distribution Across Delivery Centers',
                'font': {'size': 20, 'family': 'Inter'}
            },
            xaxis_title="Location",
            yaxis_title="Number of Associates",
            font=dict(family="Inter", size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_geo, use_container_width=True)
        
        # Location insights
        col_insight1, col_insight2 = st.columns(2)
        with col_insight1:
            st.markdown("""
            <div class="info-box">
                <h4>🏢 Zurich Hub Advantages</h4>
                <ul style="margin: 0.5rem 0;">
                    <li>Same timezone as UBS headquarters</li>
                    <li>Swiss regulatory compliance expertise</li>
                    <li>Direct client collaboration capability</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col_insight2:
            st.markdown("""
            <div class="info-box">
                <h4>🌏 Pune Center Benefits</h4>
                <ul style="margin: 0.5rem 0;">
                    <li>24/7 support coverage</li>
                    <li>Cost-effective delivery model</li>
                    <li>Large talent pool for scaling</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with viz_tabs[1]:
        # Project-wise analysis
        st.markdown("#### Project Type Analysis")
        
        # Stacked bar chart for project types
        project_pivot = df.pivot_table(
            values='Count',
            index='Project_Type',
            columns='Skill',
            aggfunc='sum',
            fill_value=0
        )
        
        fig_project = go.Figure()
        
        colors = ['#0072C6', '#D40511', '#4CAF50', '#FF9800', '#9C27B0']
        
        for i, skill in enumerate(project_pivot.columns):
            fig_project.add_trace(go.Bar(
                name=skill,
                x=project_pivot.index,
                y=project_pivot[skill],
                marker_color=colors[i % len(colors)],
                text=project_pivot[skill],
                textposition='inside',
                textfont=dict(color='white', size=12, family='Inter')
            ))
        
        fig_project.update_layout(
            barmode='stack',
            height=500,
            title={
                'text': 'Skill Distribution Across UBS Project Types',
                'font': {'size': 20, 'family': 'Inter'}
            },
            xaxis_title="Project Type",
            yaxis_title="Number of Associates",
            font=dict(family="Inter", size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_project, use_container_width=True)
        
        # Project readiness scores
        st.markdown("#### 🎯 Project Readiness Scores")
        readiness_data = {
            'Project Type': ['Integration/Migration', 'Pega', 'Mobile Apps', 'Cards'],
            'Readiness Score': [92, 88, 95, 85],
            'Risk Level': ['Low', 'Low', 'Very Low', 'Medium']
        }
        readiness_df = pd.DataFrame(readiness_data)
        
        col1, col2, col3, col4 = st.columns(4)
        for i, (idx, row) in enumerate(readiness_df.iterrows()):
            with [col1, col2, col3, col4][i]:
                color = '#4CAF50' if row['Risk Level'] == 'Very Low' else '#0072C6' if row['Risk Level'] == 'Low' else '#FF9800'
                st.markdown(f"""
                <div class="stat-card">
                    <h5>{row['Project Type']}</h5>
                    <div class="stat-number" style="color: {color};">{row['Readiness Score']}%</div>
                    <div class="stat-label">Risk: {row['Risk Level']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    with viz_tabs[2]:
        # Trend Analysis
        st.markdown("#### 📈 Talent Growth Trends")
        
        # Mock trend data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        trends = {
            'AI': [420, 445, 470, 495, 520, 550],
            'Python': [380, 390, 410, 425, 440, 460],
            'Cloud': [340, 355, 370, 385, 400, 420]
        }
        
        fig_trend = go.Figure()
        
        for skill, values in trends.items():
            fig_trend.add_trace(go.Scatter(
                x=months,
                y=values,
                mode='lines+markers',
                name=skill,
                line=dict(width=3),
                marker=dict(size=8)
            ))
        
        fig_trend.update_layout(
            height=400,
            title={
                'text': '6-Month Talent Growth Trajectory',
                'font': {'size': 20, 'family': 'Inter'}
            },
            xaxis_title="Month (2025)",
            yaxis_title="Number of Associates",
            font=dict(family="Inter", size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            showlegend=True
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Growth insights
        st.markdown("""
        <div class="executive-summary">
            <h3>Growth Analysis</h3>
            <p>📈 <strong>31% growth in AI capabilities</strong> over 6 months, directly supporting UBS's AI-first digital transformation strategy. 
            Python and Cloud competencies show steady 21% and 24% growth respectively, ensuring scalable solutions for future projects.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with viz_tabs[3]:
        # Skill Matrix Heatmap
        st.markdown("#### 🎯 Skill Availability Matrix")
        
        # Create availability heatmap
        pivot_avail = df.pivot_table(
            values='Available_Now',
            index='Project_Type',
            columns='Skill',
            aggfunc='sum',
            fill_value=0
        )
        
        fig_heatmap = px.imshow(
            pivot_avail,
            labels=dict(x="Skill", y="Project Type", color="Available Associates"),
            color_continuous_scale='Blues',
            aspect='auto',
            title='Real-Time Availability Heatmap'
        )
        
        fig_heatmap.update_layout(
            height=400,
            font=dict(family="Inter", size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Add text annotations
        for i in range(len(pivot_avail.index)):
            for j in range(len(pivot_avail.columns)):
                fig_heatmap.add_annotation(
                    text=str(pivot_avail.iloc[i, j]),
                    x=j,
                    y=i,
                    showarrow=False,
                    font=dict(color='white' if pivot_avail.iloc[i, j] > 50 else 'black', size=12)
                )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)

elif page == "📅 Availability":
    st.markdown("### 📅 Real-Time Availability & Deployment Planning")
    
    # Deployment readiness dashboard
    st.markdown("""
    <div class="executive-summary">
        <h3>🚀 Deployment Readiness Dashboard</h3>
        <p>Real-time visibility into talent availability for immediate UBS project deployment. 
        Our predictive analytics ensure optimal resource allocation and zero bench time.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        project_filter = st.selectbox(
            "🏗️ Filter by Project Type",
            ["All"] + sorted(df['Project_Type'].unique().tolist())
        )
    
    with col2:
        location_filter = st.selectbox(
            "📍 Filter by Location",
            ["All"] + sorted(df['Location'].unique().tolist())
        )
    
    with col3:
        urgency = st.selectbox(
            "⏱️ Deployment Timeline",
            ["Immediate (24-48h)", "Short-term (1 week)", "Standard (1 month)"]
        )
    
    # Apply filters
    availability_df = df.copy()
    
    if project_filter != "All":
        availability_df = availability_df[availability_df['Project_Type'] == project_filter]
    if location_filter != "All":
        availability_df = availability_df[availability_df['Location'] == location_filter]
    
    # Availability metrics
    st.markdown("---")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    total_available_now = availability_df['Available_Now'].sum()
    total_available_month = availability_df['Available_1_Month'].sum()
    total_count = availability_df['Count'].sum()
    
    with col_m1:
        st.markdown(f"""
        <div class="stat-card">
            <h4>⚡ Immediate</h4>
            <div class="stat-number" style="color: #4CAF50;">{total_available_now}</div>
            <div class="stat-label">Ready in 24-48h</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_m2:
        st.markdown(f"""
        <div class="stat-card">
            <h4>📅 Short-term</h4>
            <div class="stat-number" style="color: #0072C6;">{total_available_month}</div>
            <div class="stat-label">Available in 1 month</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_m3:
        st.markdown(f"""
        <div class="stat-card">
            <h4>🎯 Total Pool</h4>
            <div class="stat-number">{total_count}</div>
            <div class="stat-label">Associates matched</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_m4:
        utilization = round((total_count - total_available_now) / total_count * 100) if total_count > 0 else 0
        st.markdown(f"""
        <div class="stat-card">
            <h4>📊 Utilization</h4>
            <div class="stat-number" style="color: #FF9800;">{utilization}%</div>
            <div class="stat-label">Currently deployed</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Availability table
    st.markdown("### 📋 Detailed Availability Matrix")
    
    display_cols = ['Project_Type', 'Location', 'Skill', 'Role', 'Available_Now', 'Available_1_Month', 'Count']
    availability_display = availability_df[display_cols].rename(columns={
        'Project_Type': 'Project',
        'Available_Now': 'Immediate',
        'Available_1_Month': '1 Month',
        'Count': 'Total'
    })
    
    st.dataframe(
        availability_display.style.background_gradient(subset=['Immediate'], cmap='Greens')
                                 .background_gradient(subset=['1 Month'], cmap='Blues'),
        use_container_width=True,
        height=400
    )
    
    # Deployment timeline visualization
    st.markdown("### 📅 Deployment Timeline Simulator")
    
    col_cal1, col_cal2 = st.columns([2, 1])
    
    with col_cal1:
        if st.button("🚀 Generate Deployment Plan", type="primary", use_container_width=True):
            with st.spinner("🤖 AI optimizing deployment schedule..."):
                time.sleep(1.5)
            
            st.markdown("""
            <div class="success-msg">
                ✅ Deployment Plan Generated for UBS Project
            </div>
            """, unsafe_allow_html=True)
            
            # Mock deployment timeline
            timeline_data = {
                'Phase': ['Team Assembly', 'Onboarding', 'Knowledge Transfer', 'Production Ready'],
                'Duration': ['2 days', '3 days', '5 days', 'Day 10'],
                'Resources': [total_available_now, total_available_now, total_available_now, total_available_now],
                'Status': ['Ready', 'Scheduled', 'Planned', 'Projected']
            }
            timeline_df = pd.DataFrame(timeline_data)
            
            st.dataframe(timeline_df, use_container_width=True)
    
    with col_cal2:
        st.markdown("""
        <div class="info-box">
            <h4>🎯 Deployment Benefits</h4>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li>Zero bench time</li>
                <li>Skill-matched teams</li>
                <li>Domain expertise</li>
                <li>Compliance ready</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Resource calendar
    st.markdown("### 📅 Resource Calendar Integration")
    if st.button("📅 Connect to Resource Calendar", use_container_width=True):
        st.markdown("""
        <div class="success-msg">
            ✅ Connected to Cognizant Resource Management System
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **Calendar Sync Status:**
        - Microsoft Teams: ✅ Connected
        - Outlook Calendar: ✅ Synced
        - Resource Manager Notifications: ✅ Sent
        - UBS Project Dashboard: ✅ Updated
        """)

elif page == "📊 Advanced Analytics":
    # Import and use the advanced analytics module
    from enhanced_data_structure import create_streamlit_dataset
    advanced_df = create_streamlit_dataset()
    show_advanced_analytics(advanced_df)

elif page == "❓ Help":
    st.markdown("### ❓ Help & User Guide")
    
    # Video tutorial placeholder
    st.markdown("""
    <div class="executive-summary">
        <h3>🎥 Quick Start Video Tutorial</h3>
        <p>Watch our 3-minute guide to maximize the Talent Edge CRM Toolkit for winning UBS deals.</p>
        <div style="background: #f0f0f0; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 12px; margin-top: 1rem;">
            <span style="font-size: 3rem;">▶️</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # FAQ Section
    st.markdown("### 🤔 Frequently Asked Questions")
    
    faq_items = [
        {
            "question": "How quickly can we deploy resources for UBS projects?",
            "answer": "Our Zurich hub maintains a 24-48 hour deployment capability for critical projects, with pre-screened associates ready for immediate onboarding.",
            "icon": "⚡"
        },
        {
            "question": "What's the accuracy of the AI-powered insights?",
            "answer": "Our Claude AI integration provides 95%+ accuracy in talent matching, leveraging real-time data from our HR systems and project histories.",
            "icon": "🤖"
        },
        {
            "question": "Can we scale teams dynamically?",
            "answer": "Yes! Our dual-shore model (Zurich + Pune) enables 24/7 coverage and seamless scaling from 5 to 500+ associates within weeks.",
            "icon": "📈"
        },
        {
            "question": "How does this integrate with existing systems?",
            "answer": "The toolkit integrates with Cognizant's HRMS, Microsoft Teams, and project management tools via secure APIs for real-time data synchronization.",
            "icon": "🔗"
        }
    ]
    
    for item in faq_items:
        with st.expander(f"{item['icon']} {item['question']}"):
            st.write(item['answer'])
    
    # Best practices
    st.markdown("### 💡 Best Practices for CRM Success")
    
    col_bp1, col_bp2 = st.columns(2)
    
    with col_bp1:
        st.markdown("""
        <div class="info-box">
            <h4>🎯 Pre-Meeting Preparation</h4>
            <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li>Run queries for client's project type</li>
                <li>Generate PDF reports in advance</li>
                <li>Prepare 3 deployment scenarios</li>
                <li>Test AI insights with client keywords</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col_bp2:
        st.markdown("""
        <div class="info-box">
            <h4>🚀 During Client Meetings</h4>
            <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li>Use live queries to answer questions</li>
                <li>Show real-time availability</li>
                <li>Demonstrate deployment timelines</li>
                <li>Export custom reports on-demand</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Support section
    st.markdown("### 📞 Support & Contact")
    
    support_cols = st.columns(3)
    
    with support_cols[0]:
        st.markdown("""
        <div class="stat-card">
            <h4>💬 Live Chat</h4>
            <p style="margin: 1rem 0;">24/7 technical support</p>
            <div style="color: #0072C6; font-weight: 600;">chat.cognizant.com</div>
        </div>
        """, unsafe_allow_html=True)
    
    with support_cols[1]:
        st.markdown("""
        <div class="stat-card">
            <h4>📧 Email Support</h4>
            <p style="margin: 1rem 0;">Response within 2 hours</p>
            <div style="color: #0072C6; font-weight: 600;">talentedge@cognizant.com</div>
        </div>
        """, unsafe_allow_html=True)
    
    with support_cols[2]:
        st.markdown("""
        <div class="stat-card">
            <h4>📱 Hotline</h4>
            <p style="margin: 1rem 0;">For urgent requests</p>
            <div style="color: #0072C6; font-weight: 600;">+41 58 123 4567</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Version info
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p><strong>Talent Edge CRM Toolkit v2.0</strong></p>
        <p>Last updated: July 2025 | Next release: August 2025</p>
        <p style="font-size: 0.9rem;">© 2025 Cognizant Technology Solutions. Built with ❤️ for UBS Partnership Success.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer with live status
st.markdown("---")
footer_cols = st.columns([2, 1, 1, 1])

with footer_cols[0]:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 1rem;">
        <div class="loading"></div>
        <span style="color: #4CAF50; font-weight: 600;">System Status: All services operational</span>
    </div>
    """, unsafe_allow_html=True)

with footer_cols[1]:
    st.markdown("""
    <div style="text-align: center;">
        <span class="badge">LIVE DATA</span>
    </div>
    """, unsafe_allow_html=True)

with footer_cols[2]:
    st.markdown("""
    <div style="text-align: center;">
        <span style="color: #666;">Zurich: 14:32</span>
    </div>
    """, unsafe_allow_html=True)

with footer_cols[3]:
    st.markdown("""
    <div style="text-align: center;">
        <span style="color: #666;">Pune: 19:02</span>
    </div>
    """, unsafe_allow_html=True) 