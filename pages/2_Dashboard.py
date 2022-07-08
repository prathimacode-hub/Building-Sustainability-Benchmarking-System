from pathlib import Path
#import folium
#import geopandas as gpd
import pandas as pd
import numpy as np
import plotly_express as px
import streamlit as st
#from streamlit_folium import folium_static
import chart_studio.plotly as py

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGE_TITLE = "Dashboard"
SUSTAINABILITY_REPORT_WORD_CLOUD = "Sustainability Report Word Cloud"
TAB_LABELS = [SUSTAINABILITY_REPORT_WORD_CLOUD]

st.markdown("<h2 style='text-align: center; color: #4169e1;margin-top:-50px;font-weight:bold'>OMDENA-SUSTAINLABS</h2>", unsafe_allow_html=True)


if active_tab == SUSTAINABILITY_REPORT_WORD_CLOUD:
 
    #st.subheader('VISUALIZATIONS')
    st.markdown('<h4>Word Cloud of a Modified Sustainability Report</h4>', unsafe_allow_html=True)
    st.image("word_cloud.png", width=400)
    st.markdown('<h4>Top Words in Headlines versus Count</h4>', unsafe_allow_html=True)
    st.image("top_words_in_headlines_versus_count.png", width=400)
    
    st.subheader('INFERENCES')
 
    st.markdown("""
    <p style="font-size:15px">
    - By observing the word cloud(1st graph) keyword extracted are properties, tenants which give information that the company is a Property Management company.
    - This company has emphasized more on energy consumption which is one of most frequently used word.
    - They have got "green leases" which is a significant keyword. 
    - Most frequently used word is "Waste"
    - These results are for 1 page extraction. 
    """, unsafe_allow_html=True)
    
    st.subheader('SUMMARY')
    
    st.markdown("""
    <p style="font-size:15px">
    - Super small font size extraction is giving poor results. Metrics fell <50%.
    - EasyOcr works best for text documents
    """, unsafe_allow_html=True)
    
#     st.subheader('Raw data')
#     data = st.checkbox('Show Raw Data')

#     if data:
#         st.dataframe(df_preprocessed_2015)
#         csv = convert_df(df_preprocessed_2015)
#         st.download_button(
#             label="Download data as CSV",
#             data=csv,
#             file_name='large_df.csv',
#             mime='text/csv',
#         )
    
