import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_resource
def aksesdata():
    set_day = pd.read_csv("data/day.csv")
    return set_day
ds = aksesdata()

#Title
st.title("Dashboard Streamlit Bike Sharing")

# Visualisasi Data
# ### Pertanyaan 1: Bagaimana statistik rental sepeda di tahun 2012?
year_target = ds.query('yr == 1')
statistik_2012 = year_target.groupby("mnth")["cnt"].sum().reset_index()
fig = px.line(statistik_2012, x="mnth", y="cnt", title="Statistik Rental Sepeda pada Tahun 2012").update_layout(xaxis_title="Bulan", yaxis_title="Jumlah Rental Sepeda")
st.plotly_chart(fig, use_container_width=True,height=400, width=600)

# ### Pertanyaan 2: Apa musim yang paling banyak terjadi rental sepeda di tahun 2011?
year_target = ds.query('yr == 1')
season_2011 = year_target.groupby("season")["cnt"].sum().reset_index()
fig = px.bar(season_2011, x="season",y="cnt", title="Jumlah Sewa Sepeda Berdasarkan Musim pada Tahun 2011").update_layout(xaxis_title="Musim", yaxis_title="Jumlah Rental Sepeda")
st.plotly_chart(fig, use_container_width=True,height=400, width=600)
