import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

def fetch_movers():
    # Mocked data for stock movers as an example
    # Replace this with actual scraping code from the NSE website
    return pd.DataFrame({
        'Stock': ['StockA', 'StockB', 'StockC'],
        'Previous Close': [100, 150, 200],
        'Current Price': [105, 140, 220],
        'Change (%)': [5, -6.67, 10]
    })

def fetch_gainers_losers():
    # Example for top gainers and losers
    return pd.DataFrame({
        'Stock': ['StockD', 'StockE'],
        'Current Price': [120, 90],
        'Change (%)': [4, -3.5]
    })

def fetch_specific_changes():
    # Example for stocks with specific changes
    return pd.DataFrame({
        'Stock': ['StockF', 'StockG'],
        'Current Price': [110, 95],
        'Change (%)': [2, 3]
    })

def fetch_sector_performance():
    # Example for sector performance
    return pd.DataFrame({
        'Sector': ['Sector1', 'Sector2'],
        'Change (%)': [1.5, 2.3]
    })

def fetch_fno_data():
    # Example for F&O data
    return pd.DataFrame({
        'Stock': ['StockH', 'StockI'],
        'Current Price': [115, 130],
        'Short Covering': [True, False],
        'Open Interest Gainer': [True, True]
    })
# Streamlit Dashboard Code

# Title of the Dashboard
st.title("NSE Stock Dashboard")

# Define tabs for each step
tabs = ["Movers", "Top Gainers and Losers", "Specific Change", "Sector Performance", "F&O Data", "Dashboard"]
selected_tab = st.sidebar.selectbox("Select Tab", tabs)

# Buttons for Refresh and Clean Data
if st.sidebar.button("Refresh Data"):
    st.experimental_rerun()  # This will refresh the page and reload data

if st.sidebar.button("Clean Data"):
    st.caching.clear_cache()
    st.write("Data cleaned!")

# Load data based on the selected tab
if selected_tab == "Movers":
    movers_data = fetch_movers()
    st.write("Movers (Change >5% or <-5%)")
    st.dataframe(movers_data)

elif selected_tab == "Top Gainers and Losers":
    gainers_losers_data = fetch_gainers_losers()
    st.write("Top Gainers and Losers at 9:10 AM")
    st.dataframe(gainers_losers_data)

elif selected_tab == "Specific Change":
    specific_change_data = fetch_specific_changes()
    st.write("Stocks with 2%, 3%, or 5% Change at 9:15 AM")
    st.dataframe(specific_change_data)

elif selected_tab == "Sector Performance":
    sector_performance_data = fetch_sector_performance()
    st.write("Sectors Performing Well at 9:20 AM")
    st.dataframe(sector_performance_data)

elif selected_tab == "F&O Data":
    fno_data = fetch_fno_data()
    st.write("F&O Data - Short Covering and Open Interest Gainers")
    st.dataframe(fno_data)

elif selected_tab == "Dashboard":
    # Combine data to highlight stocks matching conditions across multiple tabs
    movers_data = fetch_movers()
    gainers_losers_data = fetch_gainers_losers()
    specific_change_data = fetch_specific_changes()
    sector_performance_data = fetch_sector_performance()
    fno_data = fetch_fno_data()

    # Example highlight condition: stocks in F&O matching with other categories
    matched_stocks = fno_data[
        fno_data['Stock'].isin(movers_data['Stock']) |
        fno_data['Stock'].isin(gainers_losers_data['Stock']) |
        fno_data['Stock'].isin(specific_change_data['Stock'])
    ]

    st.write("Highlighted Stocks Matching Multiple Criteria")
    st.dataframe(matched_stocks)
