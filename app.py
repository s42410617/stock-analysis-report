import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Stock Analysis", page_icon="📈", layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("Data Filter")
selected_year = st.sidebar.selectbox("Select Year", ["2025", "2024", "2023", "2022", "2021", "2020"])
selected_season = st.sidebar.selectbox("Select Quarter", ["All", "Q1", "Q2", "Q3", "Q4"])

@st.cache_data
def get_industry_data():
    industries = ['Food', 'Medicine', 'Electronics', 'Banking', 'Finance', 'Machinery', 'Power', 'Defense', 'Coal', 'Steel']
    returns = [12.5, 8.5, 8.8, 5.1, 4.8, 7.8, 8.2, 9.8, 10.8, 10.5]
    pe_values = [32.5, 28.3, 35.8, 6.8, 14.5, 22.1, 26.8, 42.5, 8.2, 10.5]
    return pd.DataFrame({'Industry': industries, 'Return': returns, 'PE': pe_values})

df = get_industry_data()

st.title("📈 A-Shares Industry Rotation Analysis")
st.markdown("---")

st.markdown("### Market Overview")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Industries", "10")
with col2:
    st.metric("Average Return", f"{df['Return'].mean():.1f}%")

st.markdown("---")
st.markdown("### Industry Return Ranking")
fig = px.bar(df, x='Industry', y='Return', color='Return', title='Industry Returns')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### PE Comparison")
fig2 = px.bar(df, x='Industry', y='PE', color='PE', title='PE Comparison')
st.plotly_chart(fig2, use_container_width=True)