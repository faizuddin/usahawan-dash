import streamlit as st
import pandas as pd
import numpy as np
import funcs_2
import plotly.express as px

st.header("KKDW Usahawan Dashboard")
st.sidebar.header("Persepsi Masyarakat")

df = funcs_2.process_data(funcs_2.load_dataset("../data/Pelangai KUD 2023.xlsx"))

st.write(df)
