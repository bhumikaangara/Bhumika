import streamlit as st
import requests
import pandas as pd

st.title("Crypto Price Tracker")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,dogecoin",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

crypto_data = {
    "Crypto": ["Bitcoin", "Ethereum", "Dogecoin"],
    "Price (USD)": [
        data["bitcoin"]["usd"],
        data["ethereum"]["usd"],
        data["dogecoin"]["usd"]
    ]
}

df = pd.DataFrame(crypto_data)

st.table(df)

threshold = st.number_input("Set Bitcoin Alert Price", value=50000)

btc_price = data["bitcoin"]["usd"]

if btc_price > threshold:
    st.warning("Bitcoin price crossed alert!")