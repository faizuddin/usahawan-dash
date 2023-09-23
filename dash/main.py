import streamlit as st
import pandas as pd
import numpy as np
import funcs

st.header("Usahawan Dashboard")

df = funcs.process_data(funcs.load_dataset("data/Data Usahawan.xlsx"))

# st.write(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
   val = len(df.index) 
   st.metric("Bilangan rekod", value=val)

with col2:
   rows = funcs.calc_freq(df, "Agensi")
   st.metric("Agensi terbesar", value=rows.iloc[0]["Agensi"])

with col3:
   rows = funcs.calc_freq(df, "Agensi")
   st.metric("Agensi terkecil", value=rows.iloc[-1]["Agensi"])

with col4:
   val = sum(df["Umur"])/len(df.index)
   st.metric("Purata umur usahawan", value="%.2f" % round(val,2))

st.subheader("Summary")


