from pathlib import Path
import pandas as pd
import numpy as np
import plotly_express as px
import streamlit as st
import chart_studio.plotly as py

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGE_TITLE = "Viz Data Preprocessing"
DATA_PREPROCESSING_INSIGHTS = "Data Preprocessing Insights"
TAB_LABELS = [DATA_PREPROCESSING_INSIGHTS]


st.markdown("<h2 style='text-align: center; color: #4169e1;margin-top:-50px;font-weight:bold'>OMDENA-SUSTAINLABS</h2>", unsafe_allow_html=True)

@st.cache
def get_active_tab():
    query_params = st.experimental_get_query_params()

    tab = "tab" in query_params and query_params["tab"][0]
    
    if tab not in TAB_LABELS:
        tab = TAB_LABELS[0]
        st.experimental_set_query_params(tab=tab)

    return tab


def render_tabs_nav(active_tab=None):
    st.markdown(
        '<link rel="stylesheet" '
        'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" '
        'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" '
        'crossorigin="anonymous">',
        unsafe_allow_html=True,
    )
    li_items = "".join(
        f"""
        <li class="nav-item">
            <a style={'width':100} class="nav-link{' active' if t == active_tab else ''}" aria-current="page"
            target="_self" href="/{PAGE_TITLE}?tab={t}">{t}</a>
        </li>
        """
        for t in TAB_LABELS
    )
    tabs_html = f"""
        <ul class="nav nav-tabs" "nav-justified">
        {li_items}
        </ul>
        <br>
    """
    st.markdown(tabs_html, unsafe_allow_html=True)

active_tab = get_active_tab()
render_tabs_nav(active_tab)


if active_tab == DATA_PREPROCESSING_INSIGHTS:

    st.markdown('<h4>Word Cloud of a Modified Sustainability Report</h4>', unsafe_allow_html=True)
    st.image("word_cloud.png", width=500)
    st.markdown('<h4>Top Words in Headlines versus Count</h4>', unsafe_allow_html=True)
    st.image("top_words_in_headlines_versus_count.png", width=700)
    
    st.subheader('Inferences')
 
    st.markdown("""
    <p style="font-size:15px">
    
    - By observing the word cloud(1st graph) keyword extracted are properties, tenants which give information that the company is a Property Management company.
    
    - This company has emphasized more on energy consumption which is one of most frequently used word.
    
    - They have got "green leases" which is a significant keyword. 
    
    - Most frequently used word is "Waste".
    
    - These results are for 1 page extraction. 
    
    """, unsafe_allow_html=True)
    
    st.subheader('Summary')
    
    st.markdown("""
    <p style="font-size:15px">
    
    - Super small font size extraction is giving poor results. Metrics fell <50%.
    
    - EasyOcr works best for text documents
    
    """, unsafe_allow_html=True)
    
    with open("modified_sustainability_report.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        
        st.download_button(label="Download Report",
                           data=PDFbyte,
                           file_name="modified_sustainability_report.pdf",
                           mime='application/octet-stream')
        
             

    


        
