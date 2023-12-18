import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo
import funcs_1
from PIL import Image

import plotly.express as px

st.set_page_config(
    page_title="KKDW Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Dashboard Ekosistem Usahawan@KKDW")
st.sidebar.header("Analisa Data Usahawan")

def sidebar_logo():
   add_logo("assets/KKDW-dash-sidebar-logo.png", height=220)

# add logo
sidebar_logo()

# load dataset
path = "data/kud-putrajaya-171223.csv"
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

tab1, tab2, tab3 = st.tabs(["Jenis", "Bidang", "Jumlah Jualan (Semasa)"])

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



st.divider()
st.header("Maklumat Manfaat")
tab1, tab2, tab3 = st.tabs(["Manfaat", "Jenis", "Jualan Tahunan (Sebelum)"])

with tab1:
   st.subheader("Manfaat")

   rows = funcs_1.calc_freq(df, "Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
   rows["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"] = rows["Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)"].str.split("-", n=1).str[0]
   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   with tab31:
      fig = px.pie(rows, values='Freq', names="Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab32:
      fig = px.bar(rows, y="Bahagian, Jabatan, dan Agensi di bawah KKDW pemberi manfaat (boleh lebih daripada 1 jawapan)", x="Freq", orientation="h")
      fig.update_layout(xaxis_title="Bilangan", yaxis_title="Agensi") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
   st.subheader("Jenis Manfaat")

   responses = []
   for r in df["Jenis bantuan / kemudahan yang telah di terima  (boleh lebih daripada 1 jawapan)"]:
      tmp = str(r).split(";")
      responses.extend(tmp)

   # use dataframe
   responses = pd.DataFrame(responses, columns=["Jenis Manfaat"])

   rows = funcs_1.calc_freq(responses, "Jenis Manfaat")
   tab21, tab22 = st.tabs(["Peratusan", "Bilangan"])

   with tab21:
      fig = px.pie(rows, values='Freq', names="Jenis Manfaat")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab22:
      fig = px.bar(rows, y="Jenis Manfaat", x="Freq", orientation="h")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
   st.subheader("Jumlah Jualan Tahunan (Sebelum)")

   rows = funcs_1.calc_freq(df, "Anggaran Jualan Bulanan (Tahunan) Syarikat Sebelum Menyertai Program Keusahawanan KKDW")
   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   with tab31:
      fig = px.pie(rows, values='Freq', names="Anggaran Jualan Bulanan (Tahunan) Syarikat Sebelum Menyertai Program Keusahawanan KKDW")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab32:
      fig = px.bar(rows, x="Anggaran Jualan Bulanan (Tahunan) Syarikat Sebelum Menyertai Program Keusahawanan KKDW", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.divider()
st.header("Persepsi Usahawan")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Kecapaian", "Pendidikan dan Kemahiran", "Sosioekonomi", "Rangkaian", "Keupayaan Bersaing", "Perundangan", "Wira Aspirasi", "Kelestarian"])

with tab1:
   st.subheader("Kecapaian")
   st.markdown("Sejauh manakah usahawan bersetuju bahawa terdapat **akses yang terhad** kepada pembiayaan modal, infrastruktur, teknologi, peluang latihan dan mentorship.")

   df = funcs_1.process_likert(df, "Sejauh manakah anda bersetuju bahawa terdapat akses yang terhad kepada pembiayaan modal, infrastruktur, teknologi, peluang latihan, mentorship dan lain-lain?")

   rows = funcs_1.calc_freq(df, "Sejauh manakah anda bersetuju bahawa terdapat akses yang terhad kepada pembiayaan modal, infrastruktur, teknologi, peluang latihan, mentorship dan lain-lain?")

   tab11, tab12 = st.tabs(["Peratusan", "Bilangan"])

   with tab11:
      fig = px.pie(rows, values='Freq', names="Sejauh manakah anda bersetuju bahawa terdapat akses yang terhad kepada pembiayaan modal, infrastruktur, teknologi, peluang latihan, mentorship dan lain-lain?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab12:
      fig = px.bar(rows, x="Sejauh manakah anda bersetuju bahawa terdapat akses yang terhad kepada pembiayaan modal, infrastruktur, teknologi, peluang latihan, mentorship dan lain-lain?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)


with tab2:
   st.subheader("Pendidikan dan Kemahiran")
   st.markdown("Sejauh mana usahawan percaya bahawa terdapat **jurang dalam pendidikan dan kemahiran** di kalangan masyarakat kita seperti pembangunan kemahiran, dan keperluan pasaran dan industri.")

   df = funcs_1.process_likert(df, "Sejauh mana anda percaya bahawa terdapat jurang dalam pendidikan dan kemahiran di kalangan masyarakat kita seperti pembangunan kemahiran, dan keperluan pasaran dan industri?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda percaya bahawa terdapat jurang dalam pendidikan dan kemahiran di kalangan masyarakat kita seperti pembangunan kemahiran, dan keperluan pasaran dan industri?")

   tab21, tab22 = st.tabs(["Peratusan", "Bilangan"])

   with tab21:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda percaya bahawa terdapat jurang dalam pendidikan dan kemahiran di kalangan masyarakat kita seperti pembangunan kemahiran, dan keperluan pasaran dan industri?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab22:
      fig = px.bar(rows, x="Sejauh mana anda percaya bahawa terdapat jurang dalam pendidikan dan kemahiran di kalangan masyarakat kita seperti pembangunan kemahiran, dan keperluan pasaran dan industri?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
   st.subheader("Sosioekonomi")
   st.markdown("Sejauh mana usahawan merasakan bahawa **cabaran sosioekonomi** seperti modal dan stigma masyarakat mempengaruhi peluang pembangunan peribadi.")

   df = funcs_1.process_likert(df, "Sejauh mana anda merasakan bahawa cabaran sosioekonomi seperti modal dan stigma masyarakat mempengaruhi peluang pembangunan peribadi?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda merasakan bahawa cabaran sosioekonomi seperti modal dan stigma masyarakat mempengaruhi peluang pembangunan peribadi?")

   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   with tab31:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda merasakan bahawa cabaran sosioekonomi seperti modal dan stigma masyarakat mempengaruhi peluang pembangunan peribadi?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab32:
      fig = px.bar(rows, x="Sejauh mana anda merasakan bahawa cabaran sosioekonomi seperti modal dan stigma masyarakat mempengaruhi peluang pembangunan peribadi?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab4:
   st.subheader("Rangkaian")
   st.markdown("Sejauh mana usahawan mengalami **kesukaran dalam mendapatkan rangkaian (networking)** yang mencukupi untuk perkembangan peribadi atau perniagaan mereka.")

   df = funcs_1.process_likert(df, "Sejauh mana anda mengalami kesukaran dalam mendapatkan rangkaian (networking) yang mencukupi untuk perkembangan peribadi atau perniagaan anda?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda mengalami kesukaran dalam mendapatkan rangkaian (networking) yang mencukupi untuk perkembangan peribadi atau perniagaan anda?")

   tab41, tab42 = st.tabs(["Peratusan", "Bilangan"])

   with tab41:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda mengalami kesukaran dalam mendapatkan rangkaian (networking) yang mencukupi untuk perkembangan peribadi atau perniagaan anda?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab42:
      fig = px.bar(rows, x="Sejauh mana anda mengalami kesukaran dalam mendapatkan rangkaian (networking) yang mencukupi untuk perkembangan peribadi atau perniagaan anda?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab5:
   st.subheader("Keupayaan Bersaing")
   st.markdown("Sejauh mana usahawan percaya bahawa masyarakat kita **tidak mempunyai keupayaan bersaing** dalam ekonomi global.")

   df = funcs_1.process_likert(df, "Sejauh mana anda percaya bahawa masyarakat kita tidak mempunyai keupayaan bersaing dalam ekonomi global?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda percaya bahawa masyarakat kita tidak mempunyai keupayaan bersaing dalam ekonomi global?")

   tab51, tab52 = st.tabs(["Peratusan", "Bilangan"])

   with tab51:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda percaya bahawa masyarakat kita tidak mempunyai keupayaan bersaing dalam ekonomi global?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab52:
      fig = px.bar(rows, x="Sejauh mana anda percaya bahawa masyarakat kita tidak mempunyai keupayaan bersaing dalam ekonomi global?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab6:
   st.subheader("Perundangan")
   st.markdown("Sejauh mana usahawan menganggap bahawa **halangan perundangan dan peraturan (regulasi)** mempengaruhi perkembangan perniagaan atau aktiviti sosial.")

   df = funcs_1.process_likert(df, "Sejauh mana anda menganggap bahawa halangan perundangan dan peraturan (regulasi) mempengaruhi perkembangan perniagaan atau aktiviti sosial?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda menganggap bahawa halangan perundangan dan peraturan (regulasi) mempengaruhi perkembangan perniagaan atau aktiviti sosial?")

   tab61, tab62 = st.tabs(["Peratusan", "Bilangan"])

   with tab61:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda menganggap bahawa halangan perundangan dan peraturan (regulasi) mempengaruhi perkembangan perniagaan atau aktiviti sosial?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab62:
      fig = px.bar(rows, x="Sejauh mana anda menganggap bahawa halangan perundangan dan peraturan (regulasi) mempengaruhi perkembangan perniagaan atau aktiviti sosial?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab7:
   st.subheader("Wira Aspirasi")
   st.markdown("Sejauh mana usahawan bersetuju bahawa **kekurangan wira aspirasi (ikon / mentor / coach)** merupakan cabaran utama dalam mencapai matlamat peribadi atau profesional.")

   df = funcs_1.process_likert(df, "Sejauh mana anda bersetuju bahawa kekurangan wira aspirasi (ikon / mentor / coach) merupakan cabaran utama dalam mencapai matlamat peribadi atau profesional?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda bersetuju bahawa kekurangan wira aspirasi (ikon / mentor / coach) merupakan cabaran utama dalam mencapai matlamat peribadi atau profesional?")

   tab71, tab72 = st.tabs(["Peratusan", "Bilangan"])

   with tab71:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda bersetuju bahawa kekurangan wira aspirasi (ikon / mentor / coach) merupakan cabaran utama dalam mencapai matlamat peribadi atau profesional?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab72:
      fig = px.bar(rows, x="Sejauh mana anda bersetuju bahawa kekurangan wira aspirasi (ikon / mentor / coach) merupakan cabaran utama dalam mencapai matlamat peribadi atau profesional?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab8:
   st.subheader("Kelestarian")
   st.markdown("Sejauh mana usahawan melihat **kelestarian (sustainability) dan sistem sokongan komprehensif** sebagai elemen penting dalam membangunkan komuniti usahawan.")

   df = funcs_1.process_likert(df, "Sejauh mana anda melihat kelestarian (sustainability) dan sistem sokongan komprehensif sebagai elemen penting dalam membangunkan komuniti usahawan?")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda melihat kelestarian (sustainability) dan sistem sokongan komprehensif sebagai elemen penting dalam membangunkan komuniti usahawan?")

   tab81, tab82 = st.tabs(["Peratusan", "Bilangan"])

   with tab81:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda melihat kelestarian (sustainability) dan sistem sokongan komprehensif sebagai elemen penting dalam membangunkan komuniti usahawan?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab82:
      fig = px.bar(rows, x="Sejauh mana anda melihat kelestarian (sustainability) dan sistem sokongan komprehensif sebagai elemen penting dalam membangunkan komuniti usahawan?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.divider()
st.header("Reformasi Ekosistem Usahawan @ KKDW")

tab1, tab2, tab3, tab4 = st.tabs(["Penyeliaan", "Fungsi", "Sokongan", "Pelaburan"])

with tab1:
   st.subheader("Penyeliaan")
   st.markdown("Sejauh manakah usahawan bersetuju bahawa program keusahawanan patut di uruskan dengan lebih sistematik merentasi agensi di bawah selian KKDW dan juga di kementerian lain, untuk mengelakkan sebarang bentuk duplikasi (program sama).")

   df = funcs_1.process_likert(df, "Sejauh manakah anda bersetuju bahawa program keusahawanan patut di uruskan dengan lebih sistematik merentasi agensi di bawah selian KKDW dan juga di kementerian lain, untuk mengelakkan sebarang bentuk duplikasi (program sama)?")

   rows = funcs_1.calc_freq(df, "Sejauh manakah anda bersetuju bahawa program keusahawanan patut di uruskan dengan lebih sistematik merentasi agensi di bawah selian KKDW dan juga di kementerian lain, untuk mengelakkan sebarang bentuk duplikasi (program sama)?")

   tab11, tab12 = st.tabs(["Peratusan", "Bilangan"])

   with tab11:
      fig = px.pie(rows, values='Freq', names="Sejauh manakah anda bersetuju bahawa program keusahawanan patut di uruskan dengan lebih sistematik merentasi agensi di bawah selian KKDW dan juga di kementerian lain, untuk mengelakkan sebarang bentuk duplikasi (program sama)?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab12:
      fig = px.bar(rows, x="Sejauh manakah anda bersetuju bahawa program keusahawanan patut di uruskan dengan lebih sistematik merentasi agensi di bawah selian KKDW dan juga di kementerian lain, untuk mengelakkan sebarang bentuk duplikasi (program sama)?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
   st.subheader("Fungsi")
   st.markdown("Sejauh manakah usahawan percaya bahawa usaha penstrukturan semula patut di ambil terhadap fungsi dan peranan keusahawanan di setiap Bahagian, Jabatan, dan Agensi dalam KKDW")

   df = funcs_1.process_likert(df, "Sejauh manakah anda percaya bahawa usaha penstrukturan semula patut di ambil terhadap fungsi dan peranan keusahawanan di setiap Bahagian, Jabatan, dan Agensi dalam KKDW?")

   rows = funcs_1.calc_freq(df, "Sejauh manakah anda percaya bahawa usaha penstrukturan semula patut di ambil terhadap fungsi dan peranan keusahawanan di setiap Bahagian, Jabatan, dan Agensi dalam KKDW?")

   tab21, tab22 = st.tabs(["Peratusan", "Bilangan"])

   with tab21:
      fig = px.pie(rows, values='Freq', names="Sejauh manakah anda percaya bahawa usaha penstrukturan semula patut di ambil terhadap fungsi dan peranan keusahawanan di setiap Bahagian, Jabatan, dan Agensi dalam KKDW?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab22:
      fig = px.bar(rows, x="Sejauh manakah anda percaya bahawa usaha penstrukturan semula patut di ambil terhadap fungsi dan peranan keusahawanan di setiap Bahagian, Jabatan, dan Agensi dalam KKDW?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
   st.subheader("Sokongan")
   st.markdown("Sejauh manakah usahawan bersetuju bahawa KKDW perlu menyediakan ruang serta sokongan kepada usahawan agar mampu bersaing dan maju dalam perniagaan.")

   df = funcs_1.process_likert(df, "Sejauh manakah anda bersetuju bahawa KKDW perlu menyediakan ruang serta sokongan kepada usahawan agar mampu bersaing dan maju dalam perniagaan?")

   rows = funcs_1.calc_freq(df, "Sejauh manakah anda bersetuju bahawa KKDW perlu menyediakan ruang serta sokongan kepada usahawan agar mampu bersaing dan maju dalam perniagaan?")

   tab31, tab32 = st.tabs(["Peratusan", "Bilangan"])

   with tab31:
      fig = px.pie(rows, values='Freq', names="Sejauh manakah anda bersetuju bahawa KKDW perlu menyediakan ruang serta sokongan kepada usahawan agar mampu bersaing dan maju dalam perniagaan?")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab32:
      fig = px.bar(rows, x="Sejauh manakah anda bersetuju bahawa KKDW perlu menyediakan ruang serta sokongan kepada usahawan agar mampu bersaing dan maju dalam perniagaan?", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab4:
   st.subheader("Pelaburan")
   st.markdown("Sejauh mana usahawan bersetuju bahawa KKDW patut memberikan penekanan kepada impak setiap program bagi memastikan hasil pelaburan (*Return on Investment*) dikeluarkan kerajaan adalah setimpal.")

   df = funcs_1.process_likert(df, "Sejauh mana anda bersetuju bahawa KKDW patut memberikan penekanan kepada impak setiap program bagi memastikan hasil pelaburan (Return on Invesment) dikeluarkan kerajaan adalah setimpal.")

   rows = funcs_1.calc_freq(df, "Sejauh mana anda bersetuju bahawa KKDW patut memberikan penekanan kepada impak setiap program bagi memastikan hasil pelaburan (Return on Invesment) dikeluarkan kerajaan adalah setimpal.")

   tab41, tab42 = st.tabs(["Peratusan", "Bilangan"])

   with tab41:
      fig = px.pie(rows, values='Freq', names="Sejauh mana anda bersetuju bahawa KKDW patut memberikan penekanan kepada impak setiap program bagi memastikan hasil pelaburan (Return on Invesment) dikeluarkan kerajaan adalah setimpal.")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab42:
      fig = px.bar(rows, x="Sejauh mana anda bersetuju bahawa KKDW patut memberikan penekanan kepada impak setiap program bagi memastikan hasil pelaburan (Return on Invesment) dikeluarkan kerajaan adalah setimpal.", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.divider()
st.header("Pendapat Usahawan")
st.subheader("Analisa sentimen")