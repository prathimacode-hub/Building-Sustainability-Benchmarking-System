import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.sidebar.header("Timeline")

st.subheader("About the project")


st.markdown(f'Timeline from Start of the Week: ')

st.markdown('<h1 style=color:#ff8080;">Week 1-2</h1>', unsafe_allow_html=True)

st.markdown(""" 
* 
* 
* 
""", unsafe_allow_html=True)

st.markdown('<h1 style=color:#ff8080;">Week 3-4</h1>', unsafe_allow_html=True)

st.markdown(""" 
* 
* 
* 
* 
""", unsafe_allow_html=True)

