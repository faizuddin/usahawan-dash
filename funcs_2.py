import streamlit as st
import pandas as pd
import malaya

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

def process_data(dataframe):
    df = dataframe
    return df

def load_model(model_name):
   sent_model = malaya.sentiment.transformer(model=model_name)
   return sent_model
