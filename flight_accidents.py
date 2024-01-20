# 0 import the libraries and packages necessary

# Manipulating Dataframe objects
import pandas as pd
# in case necessary
import numpy as np 
# creating the application 
import streamlit as st 

from pipeline import load_data
# 1. load the data 
""" 
    In the future version there will be a file to load extract and transform 
    For the future fiel >> pipeline.py

    Treat the labels of each column using a "lambda" function. Avoid user error typing.
    lowercase = lambda x: str(x).lower()

"""
@st.cache_data  # mantain the data loaded

def load_data():
   contribute_factor = pd.read_csv(r'C:\Users\U6094291\Desktop\flights\fator_contribuinte.csv', encoding = "ISO-8859-1", sep=';')
   type_occorency    = pd.read_csv(r'C:\Users\U6094291\Desktop\flights\ocorrencia_tipo.csv', encoding = "ISO-8859-1", sep=';') 
   ocorrency         = pd.read_csv(r'ocorrencia.csv', encoding = "ISO-8859-1", sep=';')
   aircraft          = pd.read_csv(r'aeronave.csv', encoding = "ISO-8859-1", sep=';') 

   ocorrency.drop(['codigo_ocorrencia1','codigo_ocorrencia2','codigo_ocorrencia3','codigo_ocorrencia4'], axis=1, inplace=True)
   type_occorency.rename({'codigo_ocorrencia1': 'codigo_ocorrencia'},  inplace=True, axis='columns') 
   aircraft.rename({'codigo_ocorrencia2': 'codigo_ocorrencia'}, inplace=True, axis='columns')
   contribute_factor.rename({'codigo_ocorrencia3': 'codigo_ocorrencia'}, inplace=True, axis='columns')
   
   # [ocorrency, type_occorency, aircraft, contribute_factor]
   df = pd.merge(ocorrency, type_occorency,  on='codigo_ocorrencia')
   df = pd.merge(df, aircraft, on='codigo_ocorrencia')
   df = pd.merge(df, contribute_factor, on = 'codigo_ocorrencia')

   del contribute_factor, type_occorency,  ocorrency,  aircraft

   return df

df = load_data()
st.set_page_config(layout='wide')
# Start the application
# Setting tittle
st.title("Aircraft Accident Report") 
st.markdown(
    """
    This report has the goal to clearify accidents and incidents which happen with aircrafts under the suppervison of **Brazillian Avation Agency**.   
    """
)
if st.sidebar.checkbox("Show table?"):
    st.header("Raw data")
    st.write(df)

st.sidebar.info("{} lines has been loaded".format(df.shape[0]))

st.subheader("Somenthing")


