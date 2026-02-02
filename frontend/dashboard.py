
import streamlit as st
import requests
import plotly.express as px

st.set_page_config(page_title="Payment Funnel Analysis", layout="centered")

st.title("💳 Payment Funnel Analysis Dashboard")

API_URL = "http://localhost:5000/funnel"

try:
    response = requests.get(API_URL)
    data = response.json()

    steps = [d["step"] for d in data]
    counts = [d["user_id"] for d in data]

    fig = px.funnel(
        x=counts,
        y=steps,
        title="User Drop-Off Across Payment Funnel"
    )

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error("Backend not reachable. Start Flask backend first.")
