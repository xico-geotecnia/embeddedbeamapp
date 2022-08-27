import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_tags import st_tags
from streamlit_tags import st_tags_sidebar
from References.pages2 import main_page,page2

st.set_page_config(layout="wide")
    
page_names_to_funcs = {
"Instructions": main_page,
"App": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()