# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor Bryson
"""


# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_and_components as sac



# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)



# Caching data
@st.cache_data
def get_data(filename):
    dat = pd.read_csv(filename, index_col = False)
    return dat


dat = get_data("https://github.com/connorbryson5/Health-Dashboard-Streamlit/blob/main/data/heart_2022_no_nans.csv?raw=True")









# Main Page 
    
    
    
st.markdown('# NBA Score Prediction App)')





