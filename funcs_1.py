import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

def process_data(dataframe):
    # drop NaNs
    df = dataframe.dropna()

    # drop Bil column
    df = df.drop(["Bil"], axis=1)

    # Calculate age by IC number
    ic = df["No K/P"].str.strip('[]')
    ic = ic.astype(str)

    df["Umur"] = ic.astype(str).str[:2]

    # drop invalid IC numbers
    df = df[pd.to_numeric(df["Umur"], errors='coerce').notnull()]

    age = df["Umur"].astype(int)
    df["Umur"] = abs(2023-age).astype(str).str[-2:].astype(int)

    return df

def calc_freq(dataframe, col):
    freq = dataframe[col].value_counts()
    # convert series to dataframe
    freq = freq.reset_index()
    freq.columns = [col, "Freq"]

    return freq

def process_likert(dataframe, col):
    dataframe.loc[dataframe[col] == 1, col] = "Sangat Tidak Setuju"
    dataframe.loc[dataframe[col] == 2, col] = "Tidak Setuju"
    dataframe.loc[dataframe[col] == 3, col] = "Tidak Setuju atau Setuju"
    dataframe.loc[dataframe[col] == 4, col] = "Setuju"
    dataframe.loc[dataframe[col] == 5, col] = "Sangat Setuju"

    return dataframe
                              