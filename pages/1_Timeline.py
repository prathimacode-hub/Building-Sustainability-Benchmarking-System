import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Timeline")

st.subheader("Overview")

st.markdown(f'Timeline from the Start of the Week: ')

st.markdown('<h3 style=color:#4169e1;">Week 1-2</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Exploring the provided 500 sustainability reports
* Extracting the data from saasb.org and analyzing it
* Figuring out the approach to preprocess the data
* Extracting the data from sustainabilityreports.com and responsibilityreports.com
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Week 3-4</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Comparing the websites and working on gathering information out of the reports extracted
* Generated WordCloud using modified PDF
* Analyzing the data of sustainability reports.
* Tabular data was successfully extracted using Camelot and Pytesseract.
* OCR and ESG bert model gave good efficiency
* Worked on the KPI matching part with SustainLab list
* Created Streamlit application to visualize the data and modelling process
* Reflecting the insights into the dashboard for better understandings
""", unsafe_allow_html=True)

