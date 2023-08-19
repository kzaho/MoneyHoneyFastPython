import os
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Using the service name defined in docker-compose for internal networking
API_URL = "http://api:8000"

dev_mode = os.environ.get("DEV", False)
if dev_mode:
    API_URL = "http://127.0.0.1:8000"

st.title("Trading Algorithm Dashboard")

col1, col2 = st.columns(2)

with col1:
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


def get_balance_from_api():
    # Change this URL to the address where your FastAPI server is running
    url = API_URL + "/balances/balance"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.write("Error fetching balance.")
        return None


st.sidebar.subheader("Binance Balance Viewer")

# A button to trigger the balance fetch action
# if st.sidebar.button("Check Balance"):
balance_data = get_balance_from_api()
balance_data = pd.DataFrame(balance_data["balances"]).set_index("asset")
balance_data = balance_data.astype(float)
balance_data = balance_data[balance_data.sum(axis=1) > 0]
if len(balance_data) > 0:
    st.sidebar.dataframe(data=balance_data)
    # Update the 'last_clicked' in the session state with the current time
    st.sidebar.write(f"Last update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
