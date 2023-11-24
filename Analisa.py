import streamlit as st
import pandas as pd
import numpy as np
import funcs_1
from PIL import Image

import plotly.express as px

st.set_page_config(
    page_title="KKDW Dashboard",
    page_icon="📊",
    layout="wide",
)

unikl_logo = Image.open("images/unikl-logo.png")
kkdw_logo = Image.open("images/logo-KKDW.png")

with st.sidebar:
   col1, col2 = st.columns(2)

   with col1:
      st.image(kkdw_logo, width=200)
      st.image(unikl_logo, width=180)

st.title("Dashboard Ekosistem Usahawan@KKDW")
st.sidebar.header("Analisa Data Usahawan")

# load dataset
path = "data/kud-putrajaya-231123-1537.csv"
df = funcs_1.load_dataset(path)

col1, col2, col3, col4 = st.columns(4)

with col1:
   val = len(df.index) 
   st.metric("Jumlah responden", value=val)

with col2:
   rows = funcs_1.calc_freq(df, "Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
   words = rows.iloc[0]["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"].split()
   first_word = words[0]
   st.metric("Agensi terbesar", value=first_word)

with col3:
   rows = funcs_1.calc_freq(df, "Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
   st.metric("Agensi terkecil", value=rows.iloc[-1]["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"])

with col4:
   rows = funcs_1.calc_freq(df, "Umur")
   st.metric("Majoriti kumpulan umur", value=rows.iloc[0]["Umur"])

st.divider()

st.header("Demografi Usahawan")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Jantina")

   rows = funcs_1.calc_freq(df, "Jantina")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Jantina")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   
   with tab2:
      fig = px.bar(rows, x='Jantina', y="Freq")
      fig.update_layout(yaxis_title="Bilangan", bargap=0.2) 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
   st.subheader("Umur")

   rows = funcs_1.calc_freq(df, "Umur")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Umur")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   
   with tab2:
      fig = px.bar(rows, x='Umur', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
   st.subheader("Bangsa")

   rows = funcs_1.calc_freq(df, "Bangsa")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Bangsa")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x='Bangsa', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Negeri")

   rows = funcs_1.calc_freq(df, "Negeri")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Negeri")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x='Negeri', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
   st.subheader("Tahap Pendidikan")

   rows = funcs_1.calc_freq(df, "Tahap Pendidikan")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Tahap Pendidikan")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x="Tahap Pendidikan", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
   st.subheader("Status Usahawan")

   st.markdown("Usahawan yang sedang/masih menjalankan perniagaan.")

   rows = funcs_1.calc_freq(df, "Adakah anda sedang menjalankan perniagaan?")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Adakah anda sedang menjalankan perniagaan?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x="Adakah anda sedang menjalankan perniagaan?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.divider()
st.header("Maklumat Perniagaan")

tab1, tab2, tab3, tab4 = st.tabs(["Jenis", "Bidang", "Jumlah Jualan", "Manfaat"])

with tab1:
   st.subheader("Jenis Perniagaan")

   rows = funcs_1.calc_freq(df, "Jenis Pendaftaran Perniagaan")
   tab11, tab12 = st.tabs(["Peratusan", "Bilangan"])

   with tab11:
      fig = px.pie(rows, values='Freq', names="Jenis Pendaftaran Perniagaan")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab12:
      fig = px.bar(rows, x="Jenis Pendaftaran Perniagaan", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
   st.subheader("Bidang Perniagaan")

   rows = funcs_1.calc_freq(df, "Bidang Perniagaan")
   tab21, tab22 = st.tabs(["Peratusan", "Bilangan"])

   with tab21:
      fig = px.pie(rows, values='Freq', names="Bidang Perniagaan")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab22:
      fig = px.bar(rows, x="Bidang Perniagaan", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
   st.subheader("Jumlah Jualan Tahunan")

   rows = funcs_1.calc_freq(df, "Anggaran Jualan Bulanan (Tahunan) Syarikat Semasa")
   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   with tab31:
      fig = px.pie(rows, values='Freq', names="Anggaran Jualan Bulanan (Tahunan) Syarikat Semasa")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab32:
      fig = px.bar(rows, x="Anggaran Jualan Bulanan (Tahunan) Syarikat Semasa", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab4:
   st.subheader("Manfaat")

   rows = funcs_1.calc_freq(df, "Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
   rows["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"] = rows["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"].str.split("-", n=1).str[0]
   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   # st.markdown("Bilangan penerima manfaat berdasarkan agensi.")

   with tab31:
      fig = px.pie(rows, values='Freq', names="Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab32:
      fig = px.bar(rows, y="Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)", x="Freq", orientation="h")
      fig.update_layout(xaxis_title="Bilangan", yaxis_title="Agensi") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
