import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="NexGen Med-Shield", layout="wide")

# Styling
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-header { background: linear-gradient(90deg, #001f54, #003566); color: white; padding: 40px; text-align: center; border-radius: 0 0 50px 50px; margin-top: -60px; }
    .metric-card { background: white; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-top: 5px solid #007bff; }
    .status-box { padding: 15px; border-radius: 12px; text-align: center; font-weight: bold; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>NexGen Med-Shield</h1><p>Automated Pill Sorting & Verification</p></div>', unsafe_allow_html=True)

@st.fragment(run_every=1)
def sync_data():
    try:
        data = requests.get("http://127.0.0.1:5000/get-data", timeout=0.5).json()
        w, c, s = data['weight'], data['result'], data['status']
    except:
        w, c, s = "0", "None", "OFFLINE"

    st.write("#")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metric-card"><small>CURRENT WEIGHT</small><h1>{w}g</h1></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><small>DETECTION RESULT</small><h1 style="color:#007bff">{c}</h1></div>', unsafe_allow_html=True)

    status_color = "#d4edda" if s == "Scan Complete" else "#fff3cd"
    st.markdown(f'<div class="status-box" style="background:{status_color}">SYSTEM STATUS: {s}</div>', unsafe_allow_html=True)

sync_data()

# Inventory Table
st.subheader("Inventory Log")
inventory_df = pd.DataFrame({
    "Medicine": ["Aspirin", "Paracetamol", "Amoxicillin"],
    "Weight Class": ["10g", "15g", "12g"],
    "Stock": [120, 85, 42],
    "Status": ["Verified", "Verified", "Low Stock"]
})
st.table(inventory_df)
