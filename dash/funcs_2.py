import streamlit as st
import pandas as pd

@st.cache_data
def load_dataset(filepath):
    df = pd.read_excel(filepath)
    return df

def process_data(dataframe):
    df = dataframe
    return df