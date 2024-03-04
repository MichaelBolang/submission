import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD DATA
@st.cache_resource
def load_data():
    data = pd.read_csv("data/day.csv")
    return data
data = load_data()

# TITLE DASHBOARD
# Set page title
st.title("Dashboard Streamlit Bike Sharing")

# SIDEBAR
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Michael Bolang**")
st.sidebar.markdown("**• Email: [michaelbolang9@gmail.com](michaelbolang9@gmail.com)**")

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Dataset")
    st.write(data)

# VISUALIZATION
# ### Pertanyaan 1: Bagaimana statistik rental sepeda di tahun 2012?
year_target = data.query('yr == 1')
statistik_2012 = year_target.groupby("mnth")["cnt"].sum().reset_index()
fig = px.line(statistik_2012, x="mnth", y="cnt", title="Statistik Rental Sepeda pada Tahun 2012").update_layout(xaxis_title="Bulan", yaxis_title="Jumlah Rental Sepeda")
st.plotly_chart(fig, use_container_width=True,height=400, width=600)

# ### Pertanyaan 2: Apa musim yang paling banyak terjadi rental sepeda di tahun 2011?
year_target = data.query('yr == 1')
season_2011 = year_target.groupby("season")["cnt"].sum().reset_index()
fig = px.bar(season_2011, x="season",y="cnt", title="Jumlah Sewa Sepeda Berdasarkan Musim pada Tahun 2011").update_layout(xaxis_title="Musim", yaxis_title="Jumlah Rental Sepeda")
st.plotly_chart(fig, use_container_width=True,height=400, width=600)
