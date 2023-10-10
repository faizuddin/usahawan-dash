import streamlit as st
import pandas as pd
import numpy as np
import funcs_2
import plotly.express as px
import matplotlib.pyplot as plt

from pathlib import Path

from wordcloud import WordCloud

st.set_page_config(
    page_title="KKDW Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("KKDW Usahawan Dashboard")
st.sidebar.header("Persepsi Masyarakat")

path = Path("./data")/"clean-with-sentiment.csv"
df = funcs_2.process_data(funcs_2.load_dataset(path))

# st.write(df)
st.header("Demografik")
col1, col2, col3 = st.columns(3)


col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Bilangan rekod", value=len(df), delta="-312 (tidak sah)")
col2.metric("Pempamer", len(df[df["Bentuk Penyertaan di KUD"]=="Pempamer"]))
col3.metric("Pengunjung", len(df[df["Bentuk Penyertaan di KUD"]=="Pengunjung"]))
col4.metric("Purata Umur", value="%.2f" % round(sum(df["Umur"])/len(df),2))

gender_ratio = df["Jantina"].value_counts(normalize=True).mul(100).round(2)+"%"
col5.metric("Lelaki", value="%s " % (gender_ratio[0]))
col6.metric("Wanita", value="%s " % (gender_ratio[1]))

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Jantina")

    col11, col12 = st.columns(2)
    with col11:
        y_data = st.selectbox("Pilih input: ", ["Umur", "Negeri", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])

    fig = px.histogram(df, x="Jantina", color=y_data)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
    st.subheader("Umur")

    col21, col22 = st.columns(2)
    with col21:
        y_data = st.selectbox("Pilih input: ", ["Jantina", "Negeri", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])
    fig = px.histogram(df, x="Umur", color=y_data)

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
    st.subheader("Negeri")

    col31, col32 = st.columns(2)
    with col31:
        y_data = st.selectbox("Pilih input: ", ["Jantina", "Umur", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])
    fig = px.histogram(df, x="Negeri", color=y_data)
    
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.divider()
# ------------------------------
st.header("Pengetahuan")
col1, col2, col3 = st.columns(3)




st.divider()
#--------------------------------
st.header("Sentimen Masyarakat")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Analisa Sentimen")
    st.write(
    """Carta turus di bawah menunjukkan sentimen masyarakat berdasarkan bentuk penyertaan di Mini KUD Pelangai 2023. 
    *Pre-trained* model yang dilatih menggunakan [Malaya](https://malaya.readthedocs.io/en/stable/index.html) *Natural Language Processing (NLP) toolkit* 
    telah digunakan untuk menganalisa sentimen dari teks survey pempamer dan pengunjung."""
    )

    col11, col12 = st.columns(2)
    with col11:
        y_data = st.selectbox("Pilih input: ", ["Jantina", "Umur", "Negeri", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])

    fig = px.histogram(df, x="Sentiment", color=y_data)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
    st.subheader("Awan Perkataan")
    st.write(
    """*Wordcloud* di bawah menunjukkan contoh perkataan-perkataan yang digunakan oleh pempamer dan pengunjung di dalam survey mengikut sentimen.
    Kekerapan penggunaan perkataan diwakili oleh saiz."""
    )

    tmp1 = df[df["Sentiment"]=="positive"]
    Positif = ''.join(tmp1["Adakah anda mempunyai cadangan/ penambahbaikan?"])
    tmp2 = df[df["Sentiment"]=="neutral"]
    Neutral = ''.join(tmp2["Adakah anda mempunyai cadangan/ penambahbaikan?"])
    tmp3 = df[df["Sentiment"]=="negative"]
    Negatif = ''.join(tmp3["Adakah anda mempunyai cadangan/ penambahbaikan?"])

    col21, col22 = st.columns(2)

    with col21:
        topic = st.selectbox('Pilih sentimen: ',["Positif","Neutral","Negatif"])

    # Create and generate a word cloud image:
    def create_wordcloud(topic):
        if Positif == "Positif":
            topic = Positif
        elif topic == "Neutral":
            topic = Neutral
        else:
            topic = Negatif

        wordcloud = WordCloud(width=800, height=400).generate(topic)
        return wordcloud

    wordcloud = create_wordcloud(topic)

    # Display the generated image:
    fig, ax = plt.subplots(figsize = (20, 10))
    ax.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)

