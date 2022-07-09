import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Tasks Progress")

st.markdown(f'Task 1:')

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* We have collected 3125 odd reports from saasb.org. 
* Used CSR hub from AWS market place to extract the input. Research was done but Reports are not in PDF format in CSR hub.
Business Intelligence Systems which interests the data from various sources and offer the rating of the reports and its paid. We don't have directly resources available there.
We also checked csrhub.com from where we have extracted the company and industrial details, here we could get the company metadata (more than 18K companies are listed). We're 
trying to webscrape but it's time consuming. It's not a free service and include signup process but as a open source, companies are listed out there which gives the metadata. 
We get company mame, website details, industry sector and so on. The session gets expired periodically so we should see if we can extract specific industries or sectors. 
* We also extracted the company metadata from responsibilityreports.com, it listed around 2000+ companies. We have also compared the companies list with the ones in saasb.org and we could 
recognize to find 500+ odd companies. Using this we could identify the document type in saasb.org and extract the report using it. But for the remaining 1500+ which aren't available 
from saasb, we can pick up data from responsibilityreports.com directly.
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* Spend some time in identifying other sustainability databases from where we could get in form of pdf reports only.
* We could check onto databases like cdp (carbon disclosure project), esg, gri etc
* Explore on how we can programmatically extract the reports from company website. Since it's large in data, we need to find a way to automate this process using web scraping as every company will have its own web design and we have to manually look into their html source to web scrape.
* Finally, merge all these to ensure there is no overlap of reports
""", unsafe_allow_html=True)


st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
   * http://SASB.org
   * http://Responsibilityreports.com
   * http://sustainabilityreports.com
   * https://www.online-report.com/
   * https://www.thecsrfoundation.org/
   * https://www.corporateregister.com/   
""", unsafe_allow_html=True)
   
  
  
st.markdown(f'Task 2:')

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* 
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* 
""", unsafe_allow_html=True)


st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
   * 
""", unsafe_allow_html=True)



st.markdown(f'Task 3:')

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* 
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* 
""", unsafe_allow_html=True)


st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
   *   
""", unsafe_allow_html=True)



st.markdown(f'Task 4:')

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* 
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* 
""", unsafe_allow_html=True)


st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
   *  
""", unsafe_allow_html=True)




