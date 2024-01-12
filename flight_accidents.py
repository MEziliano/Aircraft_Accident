# 0 import the libraries and packages necessary

# Manipulating Dataframe objects
import pandas as pd
# in case necessary
import numpy as np 
# creating the application 
import streamlit as st 

# 1. load the data 
""" 
    In the future version there will be a file to load extract and transform 
    For the future fiel >> pipeline.py

    Treat the labels of each column using a "lambda" function. Avoid user error typing.
    lowercase = lambda x: str(x).lower()

"""
@st.cache # mantain the data loaded
def load_data(nrows):
    df = pd.read_csv(r"ocorrencia.csv", encoding = "ISO-8859-1", sep=';', nrows=nrows)
    return df
df = load_data()

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


