import osmnx as ox
import plotly.offline as pyo
import streamlit as st
from io import BytesIO
import requests

from PIL import Image

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
)

# IMG_URL = 'https://www.istockphoto.com/photo/3d-render-of-key-performance-indicators-business-concept-' \
#           'banner-gm1387135660-445156283?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_top' \
#           '&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fbenchmarking&utm_term=benchmarking%3A%3A%3A' 

# IMG_URL = 'https://www.talkdesk.com/resources/reports/talkdesk-contact-center-kpi-benchmarking-report/'

# IMG_URL = 'https://www.talkdesk.com/resources/reports/talkdesk-contact-center-kpi' \
#           '-benchmarking-report/'

# IMG_URL = 'https://www.istockphoto.com/photo/on-the-table-are-a-notebook-a-pen-and-a-book-the-book-says-sustainability' \
#           '-gm1330264758-413737731?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_bottom&utm_content=https%' \
#           '3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fsustainability-kpi-reports&utm_term=sustainability%20kpi%20reports%3A%3A%3A' 

# response = requests.get(IMG_URL)
# img = Image.open(BytesIO(response.content))

st.markdown("<h1 style='text-align: center; color: #4169e1;margin-top:-50px;'>OMDENA-SUSTAINLABS</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.subheader('BUILDING SUSTAINABILITY BENCHMARKING SYSTEM GLOBALLY')
st.markdown('<h5>PROBELM STATEMENT:</h5>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([4,0.1,0.2,2.5])
with col1:
    
    
    st.markdown("""
    SustainLab is building an ecosystem of software and AI solutions to help companies to become more sustainable. \
    The result of this project, which is related to text mining and text analysis of annual sustainability reports \
    that companies publish globally, will be used to benchmark companies in their industry and globally. The \
    sustainability benchmarking system combined with our software product will be very valuable for companies, \
    and the comparison against competitors is a compelling incentive for companies to set more ambitious goals and \
    take bolder steps towards those goals. As companies are the main contributor to our unsustainable environment, \
    society and finance helping them to become more sustainable has a huge impact for our planet and our society. \
    
    The main problem is that the data of sustainability reports do not follow any standard format and important \
    figures are presented in a very unstructured way. Steps to be followed for a defined workflow : \

    - Identify important sentences, in which important information such as actions or measurements are reported. \

    - Connect all discovered pieces of information throughout the report and summarise them in a structured way.

    - Well modelled ML tasks with their algorithms for classifying sentences and paragraphs to topics, actions, \
    measurements, etc.
    
    A collected dataset of 40,000 sustainability reports that is cleaned and labelled has been provided and \
    further enabling to gather additional data. 
    """,  unsafe_allow_html=True)

    # with col4:
#     st.image(img.resize((400, 500)))
