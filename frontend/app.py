import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Using the service name defined in docker-compose for internal networking

st.title("Trading Algorithm Dashboard")

# Display and control algorithm status
st.subheader("Algorithm Control")

response = requests.get(f"{API_URL}/status")
if response.status_code == 200:
    st.write(f"Algorithm Status: {response.json()['status']}")

if st.button("Start Algorithm"):
    response = requests.post(f"{API_URL}/start")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to start the algorithm")

if st.button("Stop Algorithm"):
    response = requests.post(f"{API_URL}/stop")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to stop the algorithm")
