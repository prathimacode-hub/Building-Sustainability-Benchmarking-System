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

st.markdown("<h2 style='text-align: center; color: #4169e1;margin-top:-50px;font-weight:bold'>OMDENA-SUSTAINLABS</h1>", unsafe_allow_html=True)
