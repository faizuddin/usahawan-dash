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
    page_icon="	📊",
    layout="wide",
)

st.title("KKDW Usahawan Dashboard")
st.sidebar.header("Persepsi Masyarakat")


# path = Path("data") / "clean-with-sentiment.csv"

path = "./data/clean-with-sentiment.csv"
df = funcs_2.process_data(funcs_2.load_dataset(path))

# st.write(df)
st.header("Demografik")
col1, col2, col3 = st.columns(3)


col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("📁 Bilangan rekod", value=len(df), delta="-312 (tidak sah)")
col2.metric("🛒 Pempamer", len(df[df["Bentuk Penyertaan di KUD"]=="Pempamer"]))
col3.metric("🛍️ Pengunjung", len(df[df["Bentuk Penyertaan di KUD"]=="Pengunjung"]))
col4.metric("🎂 Purata Umur", value="%.2f" % round(sum(df["Umur"])/len(df),2))

gender_ratio = df["Jantina"].value_counts(normalize=True).mul(100).round(2).astype(str)+"%"
col5.metric("♂️ Lelaki", value="%s " % (gender_ratio[0]))
col6.metric("♀️ Wanita", value="%s " % (gender_ratio[1]))

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Jantina")

    col11, col12 = st.columns(2)
    with col11:
        y_data = st.selectbox("Pilih input: ", ["Umur", "Negeri", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])

    fig = px.histogram(df, x="Jantina", color=y_data)
    fig.update_layout(yaxis_title="Bilangan") 
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
    st.subheader("Umur")

    col21, col22 = st.columns(2)
    with col21:
        y_data = st.selectbox("Pilih input: ", ["Jantina", "Negeri", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])
    fig = px.histogram(df, x="Umur", color=y_data)
    fig.update_layout(yaxis_title="Bilangan") 

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
    st.subheader("Negeri")

    col31, col32 = st.columns(2)
    with col31:
        y_data = st.selectbox("Pilih input: ", ["Jantina", "Umur", "Bentuk Penyertaan di KUD", "Bidang Perniagaan", "Adakah anda Penerima Manfaat?"])
    fig = px.histogram(df, x="Negeri", color=y_data)
    fig.update_layout(yaxis_title="Bilangan") 
    
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.divider()
# ------------------------------
st.header("Manfaat")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Penerima Manfaat")
    col11, col12 = st.columns(2)
    with col11:
        y_data = st.selectbox("Pilih input: ", ["Umur", "Negeri", "Bentuk Penyertaan di KUD"])
    
    fig = px.histogram(df, x="Adakah anda Penerima Manfaat?", color=y_data)
    fig.update_layout(yaxis_title="Bilangan") 
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
    st.subheader("Jenis Bantuan")
    col21, col22 = st.columns(2)
    with col21:
        y_data = st.selectbox("Pilih input: ", ["Umur", "Negeri", "Bidang Perniagaan", "Modal Sebelum Mendapat Geran", "Keuntungan Bulanan"])
    
    dff = df[df["Adakah anda Penerima Manfaat?"]=="Ya"]
    fig = px.histogram(dff, x="Jenis Bantuan", color=y_data)
    fig.update_layout(yaxis_title="Bilangan") 
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
    st.subheader("Hubungkait antara modal sebelum dan nilai geran")
    st.write(""" Andaian *(H0)*: Nilai bantuan geran tidak bergantung kepada modal sebelum menerima bantuan.""")

    col31, col32 = st.columns(2)
    with col31:
        var = st.selectbox("Pilih input: ", ["Modal Sebelum Mendapat Geran", "Keuntungan Bulanan"])



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
    fig.update_layout(yaxis_title="Bilangan") 
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:

    tmp1 = df[df["Sentiment"]=="positive"]
    Positif = ''.join(tmp1["Adakah anda mempunyai cadangan/ penambahbaikan?"])
    tmp2 = df[df["Sentiment"]=="neutral"]
    Neutral = ''.join(tmp2["Adakah anda mempunyai cadangan/ penambahbaikan?"])
    tmp3 = df[df["Sentiment"]=="negative"]
    Negatif = ''.join(tmp3["Adakah anda mempunyai cadangan/ penambahbaikan?"])

    st.subheader("Ramalan Sentimen")
    # load prediction model
    sent_model = funcs_2.load_model("tiny-bert")
    with st.form("sentiment_example"):
        st.write("""Ramal kebarangkalian sentimen komen-komen dari survey pempamer dan pengunjung di Mini KUD Pelangai 2023.
        """)
        text = st.selectbox("Pilih komen: ", df["Adakah anda mempunyai cadangan/ penambahbaikan?"])
        
        # Every form must have a submit button.
        submitted = st.form_submit_button("Ramal sentimen")

        if submitted:
            # do prediction
            preds = sent_model.predict_proba([text])
            prob_pos = [p["positive"] for p in preds]
            prob_neu = [p["neutral"] for p in preds]
            prob_neg = [p["negative"] for p in preds]

            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Positif", value="%.4f" % prob_pos[0])
            
            with col2:
                st.metric(label="Neutral", value="%.4f" % prob_neu[0])
            
            with col3:
                st.metric(label="Negatif", value="%.4f" % prob_neg[0])


    st.subheader("Awan Perkataan")
    st.write(
    """*Wordcloud* di bawah menunjukkan perkataan-perkataan yang digunakan oleh pempamer dan pengunjung di dalam survey mengikut.
    Size huruf mewakili frekuensi penggunaan perkataan tersebut di dalam survey."""
    )
    
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

        wordcloud = WordCloud(width=800, height=500).generate(topic)
        return wordcloud

    wordcloud = create_wordcloud(topic)

    # Display the generated wordcloud image:
    fig, ax = plt.subplots(figsize = (20, 20))
    ax.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)

