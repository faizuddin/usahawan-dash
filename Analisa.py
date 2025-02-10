import streamlit as st
import pandas as pd
import funcs_1
import funcs_2
import matplotlib.pyplot as plt

import plotly.express as px

from wordcloud import WordCloud

st.set_page_config(
    page_title="Dashboard",
    page_icon="assets/favicon.png",
    layout="wide",
)

st.title("Dashboard Ekosistem Usahawan")
st.sidebar.header("Analisa Data Usahawan")

# def sidebar_logo():
#    add_logo("assets/KKDW-dash-sidebar-logo.png", height=220)

# # add logo
# sidebar_logo()

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

col1, col2 = st.columns(2)

with col1:
   st.subheader("Jantina")
   st.markdown("Taburan usahawan mengikut jantina.")

   rows = funcs_1.calc_freq(df, "Jantina")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Jantina")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   
   with tab2:
      fig = px.bar(rows, x='Jantina', y="Freq")
      fig.update_layout(yaxis_title="Bilangan", bargap=0.2)
      fig.update_traces(width=0.5)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
   st.subheader("Umur")
   st.markdown("Taburan usahawan mengikut umur.")

   rows = funcs_1.calc_freq(df, "Umur")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Umur")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   
   with tab2:
      fig = px.bar(rows, x='Umur', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

col1, col2 = st.columns(2)

with col1:
   st.subheader("Bangsa")
   st.markdown("Taburan usahawan mengikut bangsa.")

   rows = funcs_1.calc_freq(df, "Bangsa")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Bangsa")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x='Bangsa', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
   st.subheader("Negeri")
   st.markdown("Taburan usahawan mengikut negeri.")

   rows = funcs_1.calc_freq(df, "Negeri")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Negeri")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x='Negeri', y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

col1, col2 = st.columns(2)

with col1:
   st.subheader("Tahap Pendidikan")
   st.markdown("Taburan usahawan berdasarkan tahap pendidikan.")

   rows = funcs_1.calc_freq(df, "Tahap Pendidikan")
   tab1, tab2 = st.tabs(["Peratusan", "Bilangan"])

   with tab1:
      fig = px.pie(rows, values='Freq', names="Tahap Pendidikan")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)
   with tab2:
      fig = px.bar(rows, x="Tahap Pendidikan", y="Freq")
      fig.update_layout(yaxis_title="Bilangan") 
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
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
   for r in df["Jenis bantuan / kemudahan yang telah di terima  (boleh lebih daripada 1 jawapan)"].dropna():
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
      fig.update_layout(xaxis_title="Bilangan") 
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5) 
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
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
      fig.update_traces(width=0.5)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.divider()
st.header("Persepsi Subjektif Usahawan")
st.markdown("Analisa berikut menunjukkan sentimen persepsi usawahan terhadap Ekosistem Usahawan @ KKDW. Model *pra-terlatih* yang digunakan untuk menganalisa teks survey usahawan di KUD Putrajaya 2023 telah dilatih menggunakan [Malaya](https://malaya.readthedocs.io/en/stable/index.html) *Natural Language Processing (NLP) toolkit*.")

col1, col2, col3 = st.columns(3)

with col1:
   custom = st.toggle("Guna tetapan lalai", value=True)
   
   if not custom:
      # list available models
      # model_list = funcs_2.list_avail_model()
      selected_model = st.selectbox("Pilih model *pra-terlatih*:", ["Malaysian cased (tiny)", "Malaysian cased (small)"])
      if selected_model == "Malaysian cased (tiny)":
         pt_model = "mesolitica/sentiment-analysis-nanot5-tiny-malaysian-cased"
      else:
         pt_model = "mesolitica/sentiment-analysis-nanot5-small-malaysian-cased"
   else:
      pt_model = "mesolitica/sentiment-analysis-nanot5-tiny-malaysian-cased"
   
# with col2:
#    on = st.toggle("Guna model ringkas", value=True)

#    if on:
#       st.warning("Ketepatan ramalan kemungkinan lebih rendah menggunakan model ringkas", icon="⚠️")
#       quantized = True
#    else:
#       quantized = False


# load prediction model
sent_model = funcs_2.load_model(pt_model)

tab1, tab2 = st.tabs(["Analisa Sentimen", "Awan Perkataan"])

with tab1:
   st.subheader("Analisa Sentimen")

   df_sent = df[df["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."].notna()]

   preds = sent_model.predict(df_sent["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."].tolist())

   tab11, tab12, tab13 = st.tabs(["Peratusan", "Bilangan", "Ramal Sentimen"])

   df_sent["Sentiment"] = preds

   tmp1 = df_sent[df_sent["Sentiment"]=="positive"]
   Positif = ''.join(tmp1["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."].astype(str))
   tmp2 = df_sent[df_sent["Sentiment"]=="neutral"]
   Neutral = ''.join(tmp2["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."].astype(str))
   tmp3 = df_sent[df_sent["Sentiment"]=="negative"]
   Negatif = ''.join(tmp3["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."].astype(str))

   rows = funcs_1.calc_freq(df_sent, "Sentiment")

   with tab11:
      fig = px.pie(rows, values='Freq', names="Sentiment")
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab12:
      fig = px.bar(rows, x="Sentiment", y="Freq")
      fig.update_layout(yaxis_title="Bilangan")
      fig.update_traces(width=0.5)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

   with tab13:
      st.subheader("Ramal Sentimen")
      st.markdown("Ramal sentimen dari pendapat-pendapat subjektif usahawan menggunakan model *pra-terlatih* secara interaktif.")
      
      with st.form("sentiment-example"):
         text = st.selectbox("Pilih pendapat: ", df_sent["Sila nyatakan pandangan dan cadangan anda bagi menambahbaik program keusahawanan di bawah KKDW."])

         # Every form must have a submit button.
         submitted = st.form_submit_button("Ramal sentimen pendapat ini")

         if submitted:
            # do prediction
            preds = sent_model.predict_proba([text])
            prob_pos = [p["positive"] for p in preds]
            prob_neu = [p["neutral"] for p in preds]
            prob_neg = [p["negative"] for p in preds]

            st.subheader("Hasil Ramalan")
            st.markdown("Nilai kebarangkalian ramalan sentimen pendapat adalah diantara 0 (model tidak yakin dengan ramalan) dan 1 (model sangat yakin dengan ramalan).")

            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="😊 Positif", value="%.4f" % prob_pos[0])
            
            with col2:
                st.metric(label="😐 Neutral", value="%.4f" % prob_neu[0])
            
            with col3:
                st.metric(label="🙁 Negatif", value="%.4f" % prob_neg[0])

with tab2:
   st.subheader("Awan Perkataan")
   st.markdown("*Wordcloud* di bawah menunjukkan perkataan-perkataan yang digunakan didalam pendapat-pendapat yang dikemukakan oleh usahawan. Size perkataan mewakili frekuensi penggunaan perkataan tersebut di dalam survey.")

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
   ax.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   st.pyplot(fig)