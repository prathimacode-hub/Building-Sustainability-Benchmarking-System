import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Tasks Progress")

#st.markdown(f'Task 1:')

st.markdown('<h2 style=color:#4169e1;">Task 1 - Data Collection</h2>', unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* We have collected 3125 odd reports from saasb.org. 
* Used CSR hub from AWS market place to extract the input. Research was done but Reports are not in PDF format in CSR hub.
Business Intelligence Systems which interests the data from various sources and offer the rating of the reports and its paid. We don't have directly resources available there.
We also checked csrhub.com from where we have extracted the company and industrial details, here we could get the company metadata (more than 18K companies are listed). We're 
trying to webscrape but it's time consuming. It's not a free service and include signup process but as a open source, companies are listed out there which gives the metadata. 
We get company mame, website details, industry sector and so on. The session gets expired periodically so we should see if we can extract specific industries or sectors. 
* We also extracted the company metadata from responsibility-reports.com, it listed around 2000+ companies. We have also compared the companies list with the ones in saasb.org and we could 
recognize to find 500+ odd companies. Using this we could identify the document type in saasb.org and extract the report using it. But for the remaining 1500+ which aren't available 
from saasb, we can pick up data from responsibility-reports.com directly.
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
   * https://www.responsibilityreports.com/
   * https://www.sustainability-reports.com/
   * https://www.online-report.com/
   * https://www.thecsrfoundation.org/   
   * https://www.corporateregister.com/
   * https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
""", unsafe_allow_html=True)


#st.markdown(f'Task 2:')

st.markdown('<h2 style=color:#4169e1;">Task 2 - Data Pre=Processing</h2>', unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Data analysis of sustainability reports.
* Tabular data successfully extracted using Camelot.
* Pytesseract was able to extract the text correctly from pages where we have multiple columns in one page, but it did not extract tables/figures.
* OCR technique worked extremely well and gave a confidence level of 99% in the np array. Extraction was great.
* ESG bert model has being used to filter sentences with keyword topics and ESG-bert topics.
* Achieved accuracy for text extraction using EasyOCR is 75% -99%.
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* Ongoing work on text extraction and improvement on the meaningfulness of extracted text.
* Ongoing work and more focus required on the efficient extraction of chemical formula and symbols. 
* Improvement in the meaningfulness of extracted text.
* Multiprocessing of PDF text extraction.
""", unsafe_allow_html=True)


#st.markdown(f'Task 3:')

st.markdown('<h2 style=color:#4169e1;">Task 3 - Modelling</h2>', unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Significant progress has been made in the KPI matching part i.e. connecting sentences with the closest KPIs present in the list provided by Sustain Lab. 
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:

* The preprocessed datasets and the final KPI list will be passed into the pipeline.
* Match sentences in the dataset with the KPI using multiple approaches. These may produce different KPI matches. In that case take mode.

- Fuzzy Name Matching

- Sentence Embeddings

- N-gram Embeddings

* Apply NER based methods to extract values – measurements, date, time, orgs, indicators, etc. Using dependency parsers to match these extracted values to the KPI.
* We will iteratively improve results by focusing on the problem areas. Some of these we already know :

- Resolving ambiguous KPIs.

- Multi-KPIs present in a single sentence.

- Connecting correct KPIs with their values.

""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
   * https://aaai-kdf2020.github.io/assets/pdfs/kdf2020_paper_24.pdf
   * https://huggingface.co/nbroad/ESG-BERT
   * https://towardsdatascience.com/keybert-keyword-extraction-using-bert-a6dc3dd38caf
   * https://towardsdatascience.com/easy-fine-tuning-of-transformers-for-named-entity-recognition-d72f2b5340e3
   * https://www.pinecone.io/learn/sentence-embeddings/
""", unsafe_allow_html=True)


#st.markdown(f'Task 4:')

st.markdown('<h2 style=color:#4169e1;">Task 4 - Data Visualizations</h2>', unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Taken key takeaways from the data extracted to bring out the points
* Created a streamlit app to bring all the works into a single space
* Showcased all the factors based on the progress done in data collection and data preprocessing
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

st.markdown(""" 

Following are the activities that we need focus on:
* Add additional factors along with interactiveness for the upcoming customized data
* Grab some insights from modelling process to bring clear understanding of the approach that measures the impact
""", unsafe_allow_html=True)



