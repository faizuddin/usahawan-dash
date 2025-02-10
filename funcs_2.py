import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency, chi2
import malaya

@st.cache_data
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

def process_data(dataframe):
    df = dataframe
    df = df.drop(columns=["Unnamed: 0"])
    return df

def stats_test(dataframe, idx, cols):
    crosstab_res=pd.crosstab(index=dataframe[idx],columns=dataframe[cols])
    stat, p, dof, expected = chi2_contingency(crosstab_res)

    # interpret p-value
    alpha = 0.05
    # print("p value is %.10f" % p)
    if p <= alpha:
        text = "Bergantung (tolak H0). Pembolehubah berhubungkait."
    else:
        text = "Bebas (H0 terbukti benar). Pembolehubah tidak berhubungkait"
    
    return crosstab_res, p, text

@st.cache_resource
def list_avail_model():
    # model_list = malaya.sentiment.available_transformer()
    model_list = malaya.sentiment.available_huggingface
    return model_list

# @st.cache_resource
# def load_model(model_name, quant=True):
#    sent_model = malaya.sentiment.huggingface(model=model_name, quantized=quant)
# #  sent_model = malaya.sentiment.transformer(model=model_name, quantized=quant)
#    return sent_model
    
@st.cache_resource
def load_model(model_name):
   sent_model = malaya.sentiment.huggingface(model=model_name)
#  sent_model = malaya.sentiment.transformer(model=model_name, quantized=quant)
   return sent_model