import streamlit as st
import pandas as pd
import numpy as np
import funcs

import plotly.express as px

st.header("KKDW Usahawan Dashboard")
st.sidebar.header("Analisa Data Usahawan")

df = funcs.process_data(funcs.load_dataset("../data/Data Usahawan.xlsx"))

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

tmp = df.groupby(["Agensi", "Kategori Usahawan"]).size()
dff = tmp.reset_index()
dff.columns = ["Agensi", "Kategori Usahawan", "Bilangan"]

fig = px.bar(dff, x="Agensi", y="Bilangan", color="Kategori Usahawan")

st.plotly_chart(fig, theme="streamlit")


col1, col2  = st.columns(2)

with col1:
   tmp = df["Kategori Usahawan"].value_counts()
   fig = px.pie(tmp, values="Kategori Usahawan")

   st.plotly_chart(fig, theme="streamlit", use_container_width=True, names="Kategori Usahawan", title="Pecahan Mengikut Kategori")

with col2:
   tmp = df["Jantina"].value_counts()
   fig = px.pie(tmp, values="Jantina")

   st.plotly_chart(fig, theme="streamlit", use_container_width=True, names="Jantina", title="Pecahan Mengikut Jantina")
