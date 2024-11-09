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





# Row A

a1, a2 = st.columns((3,7))


with a1:
    st.markdown('### Bar chart')
    
    
    histogram_selection1 = st.selectbox('Select Data', {'Sex', 'State', 'GeneralHealth', 'PhysicalHealthDays',
               'MentalHealthDays', 'LastCheckupTime', 'PhysicalActivities',
               'SleepHours', 'RemovedTeeth', 'HadHeartAttack', 'HadAngina',
               'HadStroke', 'HadAsthma', 'HadSkinCancer', 'HadCOPD',
               'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis',
               'HadDiabetes', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty',
               'DifficultyConcentrating', 'DifficultyWalking',
               'DifficultyDressingBathing', 'DifficultyErrands', 'SmokerStatus',
               'ECigaretteUsage', 'ChestScan', 'RaceEthnicityCategory', 'AgeCategory',
               'HeightInMeters', 'WeightInKilograms', 'BMI', 'AlcoholDrinkers',
               'HIVTesting', 'FluVaxLast12', 'PneumoVaxEver', 'TetanusLast10Tdap',
               'HighRiskLastYear', 'CovidPos', 'State_ABR'})
    
    histogram_selection2 = st.selectbox('Color by', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
           'MentalHealthDays', 'LastCheckupTime', 'PhysicalActivities',
           'SleepHours', 'RemovedTeeth', 'HadHeartAttack', 'HadAngina',
           'HadStroke', 'HadAsthma', 'HadSkinCancer', 'HadCOPD',
           'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis',
           'HadDiabetes', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty',
           'DifficultyConcentrating', 'DifficultyWalking',
           'DifficultyDressingBathing', 'DifficultyErrands', 'SmokerStatus',
           'ECigaretteUsage', 'ChestScan', 'RaceEthnicityCategory', 'AgeCategory',
           'HeightInMeters', 'WeightInKilograms', 'BMI', 'AlcoholDrinkers',
           'HIVTesting', 'FluVaxLast12', 'PneumoVaxEver', 'TetanusLast10Tdap',
           'HighRiskLastYear', 'CovidPos', 'State_ABR'}, index = None)
    
    
    histogram_selection3 = st.selectbox('Facet by', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
           'MentalHealthDays', 'LastCheckupTime', 'PhysicalActivities',
           'SleepHours', 'RemovedTeeth', 'HadHeartAttack', 'HadAngina',
           'HadStroke', 'HadAsthma', 'HadSkinCancer', 'HadCOPD',
           'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis',
           'HadDiabetes', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty',
           'DifficultyConcentrating', 'DifficultyWalking',
           'DifficultyDressingBathing', 'DifficultyErrands', 'SmokerStatus',
           'ECigaretteUsage', 'ChestScan', 'RaceEthnicityCategory', 'AgeCategory',
           'HeightInMeters', 'WeightInKilograms', 'BMI', 'AlcoholDrinkers',
           'HIVTesting', 'FluVaxLast12', 'PneumoVaxEver', 'TetanusLast10Tdap',
           'HighRiskLastYear', 'CovidPos', 'State_ABR'}, index = None)
    

with a2:    
    # Histogram
    hist1 = px.histogram(dat1 , x = histogram_selection1, color = histogram_selection2, barmode='group', text_auto=True,
                         title= f"{histogram_selection1} Data broken down by {histogram_selection2}",
                         facet_col = histogram_selection3)

    
    st.plotly_chart(hist1, use_container_width=True)




st.markdown('### Boxplot chart')

boxplot_columns = st.selectbox('Select Column', {'PhysicalHealthDays',
       'MentalHealthDays', 'SleepHours', 'HeightInMeters', 'WeightInKilograms', 'BMI'})

# Boxplot
boxplot1 = px.box(dat1, y=boxplot_columns)

st.plotly_chart(boxplot1, use_container_width=True)






# Row B
st.markdown('### Map')

b1, b2 = st.columns((2,8))

# Heat Map


with b1: 
    df = dat1.value_counts(subset = ["State_ABR", "State"], sort = False).to_frame('Count').reset_index()
    st.dataframe(df, 
                 hide_index = True,
                 use_container_width=True, 
                 column_config={
                "State_ABR": None
                })
    
    
with b2:
    
    ## Bubble Map
    states = dat1.value_counts(subset = ["State_ABR"], sort = False).to_frame('Count').reset_index().State_ABR
    sizes = dat1.value_counts(subset = ["State_ABR"], sort = False).to_frame('Count').reset_index().Count
    map1 = px.scatter_geo(dat1, locations= states, locationmode="USA-states", size = sizes , scope="usa")
    
    st.plotly_chart(map1, use_container_width=True)




st.dataframe(dat1, use_container_width=True)






