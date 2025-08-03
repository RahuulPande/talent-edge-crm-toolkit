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
    
    /* Mobile responsive design */
    @media (max-width: 768px) {
        /* Adjust main container */
        .main .block-container {
            padding: 1rem 0.5rem;
        }
        
        /* Responsive columns */
        .stColumns > div {
            margin-bottom: 1rem;
        }
        
        /* Adjust metric cards */
        .metric-container {
            padding: 0.5rem;
            margin: 0.25rem 0;
        }
        
        /* Responsive text */
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2 {
            font-size: 1.4rem !important;
        }
        
        h3 {
            font-size: 1.2rem !important;
        }
        
        /* Mobile-friendly buttons */
        .stButton > button {
            width: 100%;
            margin: 0.25rem 0;
            padding: 0.75rem;
            font-size: 1rem;
        }
        
        /* Responsive tables */
        .stDataFrame {
            font-size: 0.8rem;
        }
        
        /* Mobile sidebar */
        .css-1d391kg {
            width: 100% !important;
        }
        
        /* Touch-friendly inputs */
        .stSelectbox, .stTextInput, .stNumberInput {
            margin: 0.5rem 0;
        }
        
        /* Mobile charts */
        .js-plotly-plot {
            height: 300px !important;
        }
        
        /* Responsive cards */
        .stat-card {
            padding: 0.75rem;
            margin: 0.5rem 0;
        }
        
        /* Mobile navigation */
        .stRadio > label {
            padding: 0.5rem;
            margin: 0.25rem 0;
        }
        
        /* Touch targets */
        .stButton, .stSelectbox, .stTextInput {
            min-height: 44px;
        }
        
        /* Mobile tabs */
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: wrap;
        }
        
        .stTabs [data-baseweb="tab"] {
            min-width: 120px;
            padding: 0.5rem;
        }
    }
    
    /* Tablet optimization */
    @media (min-width: 769px) and (max-width: 1024px) {
        .main .block-container {
            padding: 1.5rem;
        }
        
        h1 {
            font-size: 2.2rem !important;
        }
        
        .stColumns > div {
            margin-bottom: 1rem;
        }
    }
    
    /* High DPI displays */
    @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
        .stButton > button {
            border-radius: 8px;
        }
        
        .stat-card {
            border-radius: 12px;
        }
    }
    
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .stat-card {
            background: #2d3748;
            color: white;
        }
        
        .info-box {
            background: #2d3748;
            color: white;
        }
    }
    
    /* Accessibility improvements */
    .stButton > button:focus,
    .stSelectbox > div:focus,
    .stTextInput > div:focus {
        outline: 2px solid #0072C6;
        outline-offset: 2px;
    }
    
    /* Loading states */
    .stSpinner {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }
    
    /* Success/error messages */
    .stAlert {
        border-radius: 8px;
        margin: 0.5rem 0;
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
        ["🏠 Introduction", "📊 Dashboard", "🔍 Talent Search", "👥 Team Builder", "📈 Project Query", "📊 Advanced Analytics", "💼 CRM Tools", "❓ Help"],
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

def show_introduction_page():
    """Display the introduction/landing page"""
    
    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: #1f77b4; font-size: 3rem; margin-bottom: 1rem;">🎯 Cognizant Talent Edge CRM Toolkit</h1>
        <p style="font-size: 1.2rem; color: #666; margin-bottom: 1rem;">
            Your comprehensive solution for Swiss banking talent management and client relationship excellence
        </p>
        <p style="font-size: 1rem; color: #888; margin-bottom: 2rem; font-style: italic;">
            Developed by <strong>Rahuul Pande (152044)</strong>, Cognizant
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Purpose Section
    st.markdown("## 🎯 Purpose & Mission")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### **For UBS Partnership Success**
        - **Talent Acquisition**: Find the perfect Swiss banking experts
        - **Team Optimization**: Build high-performing delivery teams
        - **Cost Management**: Optimize project budgets and rates
        - **Compliance**: Ensure regulatory adherence for Swiss banking
        """)
    
    with col2:
        st.markdown("""
        ### **For CRM Excellence**
        - **Client Management**: Track relationships and opportunities
        - **Pipeline Visibility**: Monitor deal progress and forecasts
        - **Performance Analytics**: Measure team and project success
        - **Strategic Insights**: Data-driven decision making
        """)
    
    # Features Overview
    st.markdown("## 🚀 Key Features")
    
    features = [
        {
            "icon": "📊",
            "title": "Executive Dashboard",
            "description": "Real-time KPIs, team metrics, and Swiss banking insights"
        },
        {
            "icon": "🔍",
            "title": "Advanced Talent Search",
            "description": "Multi-dimensional filtering with AI-powered recommendations"
        },
        {
            "icon": "👥",
            "title": "Smart Team Builder",
            "description": "Optimal team composition with cost and skill optimization"
        },
        {
            "icon": "📈",
            "title": "Project Analytics",
            "description": "Deep insights into project performance and profitability"
        },
        {
            "icon": "🏦",
            "title": "Swiss Banking Focus",
            "description": "Specialized expertise for UBS, Credit Suisse, and regulatory compliance"
        },
        {
            "icon": "📊",
            "title": "Advanced Analytics",
            "description": "Predictive insights, cost optimization, and compliance metrics"
        }
    ]
    
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 1.5rem; border-radius: 10px; margin: 0.5rem 0; color: white;">
                <h3 style="margin: 0 0 0.5rem 0;">{feature['icon']} {feature['title']}</h3>
                <p style="margin: 0; opacity: 0.9;">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # How to Use Guide
    st.markdown("## 📖 How to Use This Toolkit")
    
    steps = [
        {
            "step": "1",
            "title": "Start with Dashboard",
            "description": "Review key metrics and team performance overview"
        },
        {
            "step": "2", 
            "title": "Search for Talent",
            "description": "Use advanced filters to find specific skills and expertise"
        },
        {
            "step": "3",
            "title": "Build Your Team",
            "description": "Create optimal team compositions for your projects"
        },
        {
            "step": "4",
            "title": "Analyze Projects",
            "description": "Get insights into project performance and costs"
        },
        {
            "step": "5",
            "title": "Generate Reports",
            "description": "Create professional reports for stakeholders"
        }
    ]
    
    for step in steps:
        st.markdown(f"""
        <div style="display: flex; align-items: center; margin: 1rem 0; padding: 1rem; 
                    background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1f77b4;">
            <div style="background: #1f77b4; color: white; width: 30px; height: 30px; 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                        margin-right: 1rem; font-weight: bold;">{step['step']}</div>
            <div>
                <h4 style="margin: 0 0 0.25rem 0;">{step['title']}</h4>
                <p style="margin: 0; color: #666;">{step['description']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Swiss Banking Context
    st.markdown("## 🏦 Swiss Banking Expertise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### **UBS Integration**
        - **Regulatory Compliance**: FINMA, SNB requirements
        - **Risk Management**: Basel III, IV frameworks
        - **Digital Transformation**: Core banking modernization
        - **Wealth Management**: Private banking expertise
        """)
    
    with col2:
        st.markdown("""
        ### **Credit Suisse Expertise**
        - **Investment Banking**: M&A, capital markets
        - **Asset Management**: Portfolio optimization
        - **Private Banking**: High-net-worth services
        - **Technology Platforms**: Trading systems, risk engines
        """)
    
    # Call to Action
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; margin: 2rem 0; color: white;">
        <h2 style="margin-bottom: 1rem;">Ready to Transform Your CRM Operations?</h2>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
            Navigate to any section above to start exploring the toolkit's powerful features
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem;">
            <button style="background: white; color: #1f77b4; border: none; padding: 0.75rem 1.5rem; 
                          border-radius: 25px; font-weight: bold; cursor: pointer;">📊 View Dashboard</button>
            <button style="background: rgba(255,255,255,0.2); color: white; border: 2px solid white; 
                          padding: 0.75rem 1.5rem; border-radius: 25px; font-weight: bold; cursor: pointer;">
                🔍 Search Talent
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_talent_search():
    """Display advanced talent search functionality"""
    
    st.markdown("## 🔍 Advanced Talent Search")
    
    # Search filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        skill_filter = st.multiselect("Skills", ["Data Analytics", "Cloud Computing", "Cybersecurity", "AI/ML", "Blockchain", "DevOps"])
        location_filter = st.multiselect("Location", ["Zurich", "Pune", "Bangalore", "Mumbai"])
    
    with col2:
        experience_filter = st.slider("Experience (Years)", 0, 20, (3, 10))
        availability_filter = st.checkbox("Available Now")
    
    with col3:
        project_type_filter = st.multiselect("Project Type", ["CS Integration", "Core Banking", "Wealth Management", "Risk Management"])
        certification_filter = st.multiselect("Certifications", ["AWS", "Azure", "GCP", "CISSP", "PMP", "Scrum Master"])
    
    # Search button
    if st.button("🔍 Search Talent", type="primary"):
        st.success("✅ Found 247 matching candidates!")
        
        # Display results
        st.markdown("### 📊 Search Results")
        
        # Mock search results
        results_data = {
            "Name": ["Sarah Müller", "Raj Patel", "Elena Rodriguez", "Michael Chen"],
            "Skills": ["Data Analytics, AI/ML", "Cloud Computing, DevOps", "Cybersecurity, Blockchain", "AI/ML, Data Analytics"],
            "Experience": ["8 years", "5 years", "12 years", "6 years"],
            "Location": ["Zurich", "Pune", "Zurich", "Bangalore"],
            "Availability": ["Immediate", "2 weeks", "Immediate", "1 week"],
            "Rate": ["CHF 180/hr", "₹8,500/hr", "CHF 200/hr", "₹9,200/hr"]
        }
        
        results_df = pd.DataFrame(results_data)
        st.dataframe(results_df, use_container_width=True)

def show_team_builder():
    """Display team builder functionality"""
    
    st.markdown("## 👥 Smart Team Builder")
    
    # Team requirements
    col1, col2 = st.columns(2)
    
    with col1:
        project_type = st.selectbox("Project Type", ["Core Banking", "Wealth Management", "Risk Management", "Digital Banking"])
        team_size = st.slider("Team Size", 5, 50, 15)
        budget = st.number_input("Budget (CHF)", min_value=100000, max_value=5000000, value=500000, step=50000)
    
    with col2:
        timeline = st.selectbox("Timeline", ["3 months", "6 months", "12 months", "18 months"])
        expertise_level = st.selectbox("Expertise Level", ["Junior", "Mid-level", "Senior", "Mixed"])
        location_preference = st.multiselect("Location Preference", ["Zurich", "Pune", "Bangalore", "Mumbai"])
    
    # Build team button
    if st.button("👥 Build Optimal Team", type="primary"):
        st.success("✅ Team composition optimized!")
        
        # Display team composition
        st.markdown("### 🎯 Recommended Team Composition")
        
        team_data = {
            "Role": ["Project Manager", "Tech Lead", "Senior Developer", "Developer", "QA Engineer", "DevOps Engineer"],
            "Count": [1, 2, 3, 5, 2, 2],
            "Experience": ["10+ years", "8+ years", "6+ years", "3+ years", "4+ years", "5+ years"],
            "Location": ["Zurich", "Zurich", "Pune", "Pune", "Bangalore", "Pune"],
            "Cost/Month": ["CHF 25,000", "CHF 18,000", "CHF 12,000", "CHF 8,000", "CHF 7,000", "CHF 9,000"]
        }
        
        team_df = pd.DataFrame(team_data)
        st.dataframe(team_df, use_container_width=True)
        
        # Cost breakdown
        st.markdown("### 💰 Cost Breakdown")
        total_cost = 25 + 36 + 36 + 40 + 14 + 18  # in thousands
        st.metric("Total Monthly Cost", f"CHF {total_cost},000", f"Budget: CHF {budget//1000},000")
        
        # Progress bar
        progress = (total_cost * 1000) / budget * 100
        st.progress(min(progress, 100) / 100)

def show_project_query():
    """Display project query functionality"""
    
    st.markdown("## 📈 Project Query & Analytics")
    
    # Query interface
    col1, col2 = st.columns(2)
    
    with col1:
        query_type = st.selectbox("Query Type", ["Team Availability", "Cost Analysis", "Skill Gap", "Performance Metrics"])
        project_name = st.text_input("Project Name", "UBS Digital Banking")
    
    with col2:
        date_range = st.date_input("Date Range", value=(datetime.now(), datetime.now()))
        priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
    
    # Natural language query
    st.markdown("### 🤖 AI-Powered Query")
    nl_query = st.text_area("Ask in natural language:", 
                           placeholder="e.g., 'Show me all available data scientists in Zurich with 5+ years experience for a 6-month project'")
    
    if st.button("🔍 Execute Query", type="primary"):
        if nl_query:
            # Simulate AI processing
            with st.spinner("🤖 AI analyzing your query..."):
                time.sleep(2)
            
            st.success("✅ Query executed successfully!")
            
            # Display results
            st.markdown("### 📊 Query Results")
            
            # Mock results based on query
            results = [
                {"Name": "Dr. Anna Schmidt", "Skills": "Data Science, ML", "Experience": "8 years", "Location": "Zurich", "Availability": "Immediate"},
                {"Name": "Prof. Raj Kumar", "Skills": "AI/ML, Analytics", "Experience": "12 years", "Location": "Pune", "Availability": "2 weeks"},
                {"Name": "Elena Petrova", "Skills": "Data Engineering", "Experience": "6 years", "Location": "Zurich", "Availability": "Immediate"}
            ]
            
            for result in results:
                st.markdown(f"""
                <div style="padding: 1rem; margin: 0.5rem 0; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #28a745;">
                    <strong>{result['Name']}</strong> - {result['Skills']}<br>
                    Experience: {result['Experience']} | Location: {result['Location']} | Available: {result['Availability']}
                </div>
                """, unsafe_allow_html=True)

def show_crm_tools():
    """Display CRM-specific tools and features"""
    
    st.markdown("## 💼 CRM Tools & Client Management")
    
    # CRM Overview
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;">
        <h2 style="margin-bottom: 1rem;">🎯 Client Relationship Excellence</h2>
        <p style="font-size: 1.1rem; opacity: 0.9;">
            Comprehensive tools for managing UBS partnerships, tracking opportunities, and driving revenue growth
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CRM Tools Tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["👥 Client Management", "💰 Deal Pipeline", "📅 Meeting Scheduler", "📧 Email Templates", "📄 Proposal Templates", "📋 Contract Management", "📊 Performance Analytics"])
    
    with tab1:
        st.markdown("### 👥 Client Management")
        
        # Client Overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🏦 UBS Switzerland**
            - **Relationship Status**: Strategic Partner
            - **Engagement Value**: $45M annually
            - **Key Contacts**: 12 decision makers
            - **Last Interaction**: 2 days ago
            """)
            
            st.markdown("""
            **🏦 Credit Suisse**
            - **Relationship Status**: Growth Partner
            - **Engagement Value**: $28M annually
            - **Key Contacts**: 8 decision makers
            - **Last Interaction**: 1 week ago
            """)
        
        with col2:
            # Client Activity Timeline
            st.markdown("**📈 Recent Activity**")
            activities = [
                {"date": "2024-01-15", "activity": "UBS Core Banking Phase 2 Kickoff", "status": "✅ Completed"},
                {"date": "2024-01-12", "activity": "CS Risk Engine Upgrade Proposal", "status": "🔄 In Progress"},
                {"date": "2024-01-10", "activity": "UBS Wealth Management Demo", "status": "✅ Completed"},
                {"date": "2024-01-08", "activity": "CS Compliance Review Meeting", "status": "📅 Scheduled"}
            ]
            
            for activity in activities:
                st.markdown(f"""
                <div style="padding: 0.5rem; margin: 0.25rem 0; background: #f8f9fa; border-radius: 5px;">
                    <strong>{activity['date']}</strong> - {activity['activity']} <span style="color: #28a745;">{activity['status']}</span>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 💰 Deal Pipeline")
        
        # Pipeline Overview
        pipeline_data = {
            "Opportunity": ["UBS Digital Banking", "CS Risk Platform", "UBS Wealth Tech", "CS Compliance"],
            "Value": ["$12M", "$8M", "$15M", "$6M"],
            "Probability": ["75%", "60%", "85%", "40%"],
            "Stage": ["Proposal", "Discovery", "Contract", "Qualification"],
            "Expected Close": ["Q1 2024", "Q2 2024", "Q1 2024", "Q3 2024"]
        }
        
        pipeline_df = pd.DataFrame(pipeline_data)
        st.dataframe(pipeline_df, use_container_width=True)
        
        # Pipeline Chart
        fig = go.Figure(data=[
            go.Bar(x=pipeline_data["Stage"], y=[12, 8, 15, 6], 
                   text=[f"${v}M" for v in [12, 8, 15, 6]], 
                   textposition='auto', name="Deal Value")
        ])
        fig.update_layout(title="Pipeline Value by Stage", xaxis_title="Stage", yaxis_title="Value ($M)")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### 📅 Meeting Scheduler")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📅 Schedule New Meeting**")
            
            meeting_type = st.selectbox("Meeting Type", ["Client Review", "Proposal Presentation", "Technical Demo", "Stakeholder Update"])
            client = st.selectbox("Client", ["UBS Switzerland", "Credit Suisse", "UBS Global", "CS Investment Banking"])
            date = st.date_input("Meeting Date")
            time = st.time_input("Meeting Time")
            
            if st.button("📅 Schedule Meeting"):
                st.success(f"✅ Meeting scheduled with {client} on {date} at {time}")
        
        with col2:
            st.markdown("**📋 Upcoming Meetings**")
            
            meetings = [
                {"client": "UBS Switzerland", "type": "Proposal Presentation", "date": "2024-01-20", "time": "10:00 AM"},
                {"client": "Credit Suisse", "type": "Technical Demo", "date": "2024-01-22", "time": "2:00 PM"},
                {"client": "UBS Global", "type": "Client Review", "date": "2024-01-25", "time": "11:00 AM"}
            ]
            
            for meeting in meetings:
                st.markdown(f"""
                <div style="padding: 1rem; margin: 0.5rem 0; background: #e3f2fd; border-radius: 8px; border-left: 4px solid #2196f3;">
                    <strong>{meeting['client']}</strong><br>
                    {meeting['type']} - {meeting['date']} at {meeting['time']}
                </div>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 📧 Email Templates")
        
        template_type = st.selectbox("Select Template Type", ["Proposal Follow-up", "Meeting Confirmation", "Project Update", "Stakeholder Report"])
        
        templates = {
            "Proposal Follow-up": """
            Subject: UBS Digital Banking Proposal - Next Steps
            
            Dear [Client Name],
            
            Thank you for the opportunity to present our Digital Banking solution for UBS. 
            We're excited about the potential partnership and ready to move forward with the implementation.
            
            Key highlights from our proposal:
            • 12-month implementation timeline
            • 45% cost optimization
            • Enhanced regulatory compliance
            • 24/7 support coverage
            
            Next steps:
            1. Technical deep-dive session
            2. Contract finalization
            3. Project kickoff planning
            
            Best regards,
            [Your Name]
            Cognizant Switzerland
            """,
            
            "Meeting Confirmation": """
            Subject: Meeting Confirmation - [Meeting Type]
            
            Dear [Client Name],
            
            This confirms our meeting scheduled for [Date] at [Time].
            
            Agenda:
            • Project status review
            • Next phase planning
            • Risk assessment
            • Q&A session
            
            Location: [Meeting Location/Teams Link]
            
            Please let us know if you need any adjustments.
            
            Best regards,
            [Your Name]
            """,
            
            "Project Update": """
            Subject: Project Update - [Project Name]
            
            Dear [Client Name],
            
            Here's our weekly project update:
            
            ✅ Completed This Week:
            • [Task 1]
            • [Task 2]
            
            🔄 In Progress:
            • [Task 3]
            • [Task 4]
            
            📅 Next Week:
            • [Task 5]
            • [Task 6]
            
            Risks/Issues: [If any]
            
            Best regards,
            [Your Name]
            """,
            
            "Stakeholder Report": """
            Subject: Monthly Stakeholder Report - [Project Name]
            
            Dear [Stakeholder Name],
            
            Please find attached our monthly stakeholder report for [Project Name].
            
            Executive Summary:
            • Project is 75% complete
            • On track for March 2024 delivery
            • Budget utilization: 68%
            • Risk level: Low
            
            Key Achievements:
            • [Achievement 1]
            • [Achievement 2]
            
            Next Month Focus:
            • [Focus Area 1]
            • [Focus Area 2]
            
            Best regards,
            [Your Name]
            """
        }
        
        st.text_area("Email Template", templates.get(template_type, ""), height=300)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 Copy Template"):
                st.success("✅ Template copied to clipboard!")
        with col2:
            if st.button("📧 Send Email"):
                st.success("✅ Email sent successfully!")
    
    with tab5:
        st.markdown("### 📄 Proposal Templates")
        
        proposal_type = st.selectbox("Select Proposal Type", ["Digital Banking", "Core Banking", "Wealth Management", "Risk Management", "Compliance", "AI/ML Solutions"])
        
        proposals = {
            "Digital Banking": """
            # UBS Digital Banking Transformation Proposal
            
            ## Executive Summary
            Comprehensive digital banking solution for UBS Switzerland, delivering 45% cost optimization and enhanced customer experience.
            
            ## Solution Overview
            ### Phase 1: Core Platform (6 months)
            - Modern core banking system implementation
            - API-first architecture design
            - Real-time transaction processing
            - Enhanced security protocols
            
            ### Phase 2: Customer Experience (4 months)
            - Mobile banking application
            - Omnichannel integration
            - Personalized dashboards
            - AI-powered recommendations
            
            ### Phase 3: Advanced Features (2 months)
            - Blockchain integration
            - Advanced analytics
            - Regulatory compliance
            - Performance optimization
            
            ## Team Composition
            - **Project Manager**: 1 (Zurich)
            - **Tech Lead**: 2 (Zurich)
            - **Senior Developers**: 3 (Pune)
            - **Developers**: 5 (Pune)
            - **QA Engineers**: 2 (Bangalore)
            - **DevOps Engineers**: 2 (Pune)
            
            ## Investment & Timeline
            - **Total Investment**: CHF 2.4M
            - **Timeline**: 12 months
            - **ROI**: 300% over 3 years
            - **Risk Level**: Low
            
            ## Success Metrics
            - 60% reduction in transaction processing time
            - 45% improvement in customer satisfaction
            - 30% increase in digital adoption
            - 100% regulatory compliance
            """,
            
            "Core Banking": """
            # Credit Suisse Core Banking Modernization
            
            ## Executive Summary
            End-to-end core banking system modernization for Credit Suisse, ensuring scalability and regulatory compliance.
            
            ## Technical Architecture
            ### Infrastructure Layer
            - Cloud-native architecture (AWS/Azure)
            - Microservices design pattern
            - Container orchestration (Kubernetes)
            - Auto-scaling capabilities
            
            ### Application Layer
            - Java Spring Boot applications
            - React.js frontend
            - GraphQL API design
            - Event-driven architecture
            
            ### Data Layer
            - PostgreSQL for transactional data
            - Redis for caching
            - Elasticsearch for search
            - Apache Kafka for messaging
            
            ## Implementation Phases
            ### Phase 1: Foundation (8 months)
            - Core system architecture
            - Basic transaction processing
            - Security framework
            - Compliance modules
            
            ### Phase 2: Enhancement (6 months)
            - Advanced features
            - Performance optimization
            - Integration testing
            - User acceptance testing
            
            ## Team Structure
            - **Program Director**: 1 (Zurich)
            - **Architecture Lead**: 1 (Zurich)
            - **Tech Leads**: 3 (Zurich/Pune)
            - **Senior Developers**: 8 (Pune)
            - **Developers**: 12 (Pune)
            - **QA Engineers**: 6 (Bangalore)
            - **DevOps Engineers**: 4 (Pune)
            
            ## Investment Details
            - **Total Budget**: CHF 4.8M
            - **Duration**: 14 months
            - **Expected Savings**: CHF 12M annually
            """,
            
            "Wealth Management": """
            # UBS Wealth Management Platform
            
            ## Executive Summary
            Next-generation wealth management platform for UBS private banking clients, featuring AI-driven portfolio optimization.
            
            ## Key Features
            ### Portfolio Management
            - Real-time portfolio tracking
            - AI-powered asset allocation
            - Risk assessment algorithms
            - Performance analytics
            
            ### Client Experience
            - Personalized dashboards
            - Mobile-first design
            - Secure messaging
            - Document management
            
            ### Compliance & Security
            - FINMA compliance
            - GDPR adherence
            - Multi-factor authentication
            - Audit trail logging
            
            ## Technology Stack
            - **Frontend**: React.js, TypeScript
            - **Backend**: Node.js, Python
            - **Database**: PostgreSQL, Redis
            - **AI/ML**: TensorFlow, Scikit-learn
            - **Cloud**: AWS, Azure
            
            ## Team Composition
            - **Product Manager**: 1 (Zurich)
            - **UX/UI Designer**: 2 (Zurich)
            - **Frontend Developers**: 4 (Pune)
            - **Backend Developers**: 6 (Pune)
            - **Data Scientists**: 3 (Bangalore)
            - **QA Engineers**: 3 (Bangalore)
            
            ## Timeline & Investment
            - **Duration**: 10 months
            - **Investment**: CHF 3.2M
            - **Expected Revenue**: CHF 15M annually
            """,
            
            "Risk Management": """
            # Credit Suisse Risk Management System
            
            ## Executive Summary
            Advanced risk management platform for Credit Suisse, implementing Basel III/IV requirements and real-time risk monitoring.
            
            ## Risk Framework
            ### Credit Risk
            - Probability of default models
            - Loss given default calculations
            - Exposure at default analysis
            - Portfolio risk aggregation
            
            ### Market Risk
            - VaR (Value at Risk) calculations
            - Stress testing scenarios
            - Real-time position monitoring
            - Limit management
            
            ### Operational Risk
            - Incident tracking
            - Control monitoring
            - Risk assessment
            - Compliance reporting
            
            ## Technical Implementation
            - **Data Processing**: Apache Spark, Kafka
            - **Analytics**: Python, R, SAS
            - **Visualization**: Tableau, Power BI
            - **Storage**: Hadoop, PostgreSQL
            - **Compute**: AWS EMR, Azure HDInsight
            
            ## Team Structure
            - **Risk Manager**: 1 (Zurich)
            - **Quantitative Analysts**: 4 (Zurich)
            - **Data Engineers**: 6 (Pune)
            - **Software Developers**: 8 (Pune)
            - **QA Engineers**: 4 (Bangalore)
            - **DevOps Engineers**: 3 (Pune)
            
            ## Investment & Benefits
            - **Investment**: CHF 2.8M
            - **Timeline**: 9 months
            - **Risk Reduction**: 40%
            - **Compliance**: 100% Basel III/IV
            """,
            
            "Compliance": """
            # Swiss Banking Compliance Platform
            
            ## Executive Summary
            Comprehensive compliance management system for Swiss banking regulations, covering FINMA, SNB, and international standards.
            
            ## Regulatory Coverage
            ### FINMA Requirements
            - Anti-money laundering (AML)
            - Know your customer (KYC)
            - Market conduct supervision
            - Financial reporting
            
            ### SNB Requirements
            - Capital adequacy reporting
            - Liquidity monitoring
            - Stress testing
            - Systemic risk assessment
            
            ### International Standards
            - FATF recommendations
            - OECD guidelines
            - EU regulations
            - US compliance (if applicable)
            
            ## System Features
            - **Automated Monitoring**: Real-time compliance checking
            - **Reporting Engine**: Automated regulatory reports
            - **Audit Trail**: Complete transaction history
            - **Alert System**: Compliance violation notifications
            - **Dashboard**: Executive compliance overview
            
            ## Technology Stack
            - **Backend**: Java, Spring Boot
            - **Frontend**: Angular, TypeScript
            - **Database**: Oracle, PostgreSQL
            - **Analytics**: Apache Spark, Python
            - **Reporting**: JasperReports, Power BI
            
            ## Team Composition
            - **Compliance Officer**: 1 (Zurich)
            - **Legal Advisor**: 1 (Zurich)
            - **Compliance Analysts**: 3 (Zurich)
            - **Software Developers**: 6 (Pune)
            - **Data Analysts**: 4 (Bangalore)
            - **QA Engineers**: 3 (Bangalore)
            
            ## Investment & Timeline
            - **Investment**: CHF 1.8M
            - **Timeline**: 6 months
            - **Compliance Rate**: 99.9%
            """,
            
            "AI/ML Solutions": """
            # AI/ML Solutions for Swiss Banking
            
            ## Executive Summary
            Cutting-edge AI/ML solutions for Swiss banking operations, including fraud detection, customer insights, and process automation.
            
            ## AI/ML Applications
            ### Fraud Detection
            - Real-time transaction monitoring
            - Anomaly detection algorithms
            - Pattern recognition
            - Risk scoring models
            
            ### Customer Analytics
            - Customer segmentation
            - Churn prediction
            - Product recommendation
            - Lifetime value calculation
            
            ### Process Automation
            - Document processing (OCR)
            - Chatbot implementation
            - Workflow automation
            - Predictive maintenance
            
            ## Technology Stack
            - **Machine Learning**: TensorFlow, PyTorch, Scikit-learn
            - **Data Processing**: Apache Spark, Pandas, NumPy
            - **Big Data**: Hadoop, Kafka, Elasticsearch
            - **Cloud**: AWS SageMaker, Azure ML
            - **Visualization**: Matplotlib, Plotly, Tableau
            
            ## Team Structure
            - **AI/ML Lead**: 1 (Zurich)
            - **Data Scientists**: 6 (Bangalore)
            - **ML Engineers**: 4 (Pune)
            - **Data Engineers**: 5 (Pune)
            - **Software Developers**: 4 (Pune)
            - **QA Engineers**: 3 (Bangalore)
            
            ## Investment & ROI
            - **Investment**: CHF 3.6M
            - **Timeline**: 12 months
            - **Expected ROI**: 400% over 2 years
            - **Cost Savings**: CHF 8M annually
            """
        }
        
        st.text_area("Proposal Template", proposals.get(proposal_type, ""), height=400)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📋 Copy Template"):
                st.success("✅ Proposal template copied!")
        with col2:
            if st.button("📄 Generate PDF"):
                st.success("✅ PDF proposal generated!")
        with col3:
            if st.button("📧 Send to Client"):
                st.success("✅ Proposal sent to client!")
    
    with tab6:
        st.markdown("### 📋 Contract Management")
        
        # Contract Overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📊 Active Contracts**")
            
            contracts = [
                {"client": "UBS Switzerland", "type": "Digital Banking", "value": "CHF 2.4M", "status": "Active", "end_date": "2024-12-31"},
                {"client": "Credit Suisse", "type": "Core Banking", "value": "CHF 4.8M", "status": "Active", "end_date": "2025-06-30"},
                {"client": "UBS Global", "type": "Wealth Management", "value": "CHF 3.2M", "status": "Pending", "end_date": "2024-09-30"},
                {"client": "CS Investment", "type": "Risk Management", "value": "CHF 2.8M", "status": "Active", "end_date": "2025-03-31"}
            ]
            
            for contract in contracts:
                status_color = "#28a745" if contract["status"] == "Active" else "#ffc107"
                st.markdown(f"""
                <div style="padding: 1rem; margin: 0.5rem 0; background: #f8f9fa; border-radius: 8px; border-left: 4px solid {status_color};">
                    <strong>{contract['client']}</strong><br>
                    {contract['type']} - {contract['value']}<br>
                    Status: <span style="color: {status_color};">{contract['status']}</span> | End: {contract['end_date']}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**📈 Contract Metrics**")
            
            # Contract metrics
            total_value = 13.2  # in millions
            active_contracts = 3
            pending_contracts = 1
            avg_contract_value = total_value / (active_contracts + pending_contracts)
            
            st.metric("Total Contract Value", f"CHF {total_value}M", "↑ 15% vs last quarter")
            st.metric("Active Contracts", active_contracts, "↑ 1 vs last quarter")
            st.metric("Avg Contract Value", f"CHF {avg_contract_value:.1f}M", "↑ 8% vs last quarter")
        
        # Contract Management Tools
        st.markdown("### 🔧 Contract Tools")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📝 Create New Contract**")
            
            contract_client = st.selectbox("Client", ["UBS Switzerland", "Credit Suisse", "UBS Global", "CS Investment"])
            contract_type = st.selectbox("Contract Type", ["Time & Materials", "Fixed Price", "Retainer", "SLA"])
            contract_value = st.number_input("Contract Value (CHF)", min_value=100000, max_value=10000000, value=1000000, step=100000)
            contract_duration = st.selectbox("Duration", ["3 months", "6 months", "12 months", "18 months", "24 months"])
            
            if st.button("📋 Create Contract"):
                st.success("✅ Contract created successfully!")
        
        with col2:
            st.markdown("**📊 Contract Analytics**")
            
            # Contract performance chart
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            revenue = [2.1, 2.3, 2.8, 3.2, 3.5, 3.8]
            
            fig = go.Figure(data=go.Bar(x=months, y=revenue, 
                                       text=[f"CHF {v}M" for v in revenue], 
                                       textposition='auto'))
            fig.update_layout(title="Monthly Contract Revenue", xaxis_title="Month", yaxis_title="Revenue (CHF M)")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab7:
        st.markdown("### 📊 Performance Analytics")
        
        # CRM Performance Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Pipeline", "$41M", "↑ 12% vs last quarter")
        
        with col2:
            st.metric("Win Rate", "68%", "↑ 5% vs last quarter")
        
        with col3:
            st.metric("Avg Deal Size", "$10.25M", "↑ 8% vs last quarter")
        
        with col4:
            st.metric("Client Satisfaction", "4.8/5", "↑ 0.2 vs last quarter")
        
        # Performance Charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Revenue Trend
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            revenue = [8.2, 9.1, 10.5, 11.2, 12.8, 13.5]
            
            fig = go.Figure(data=go.Scatter(x=months, y=revenue, mode='lines+markers', 
                                           line=dict(color='#1f77b4', width=3)))
            fig.update_layout(title="Revenue Trend ($M)", xaxis_title="Month", yaxis_title="Revenue")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Client Distribution
            clients = ['UBS Switzerland', 'Credit Suisse', 'UBS Global', 'CS Investment']
            values = [45, 28, 15, 12]
            
            fig = go.Figure(data=[go.Pie(labels=clients, values=values, hole=0.4)])
            fig.update_layout(title="Revenue Distribution by Client")
            st.plotly_chart(fig, use_container_width=True)

# Main content based on selected page
if page == "🏠 Introduction":
    show_introduction_page()
elif page == "📊 Dashboard":
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

elif page == "🔍 Talent Search":
    show_talent_search()
elif page == "👥 Team Builder":
    show_team_builder()
elif page == "📈 Project Query":
    show_project_query()
elif page == "📊 Advanced Analytics":
    # Import and use the advanced analytics module
    from enhanced_data_structure import create_streamlit_dataset
    advanced_df = create_streamlit_dataset()
    show_advanced_analytics(advanced_df)
elif page == "💼 CRM Tools":
    show_crm_tools()
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