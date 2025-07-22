import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write("""
# 📊 Stock Price Analyzer

Shown are Apple stock's **closing prices** and **volume of shares** traded.
""")

ticker_symbol = "AAPL"

# Date filter
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Input starting date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Input ending date", datetime.date(2019, 7, 6))

# Get stock data
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start=start_date, end=end_date)  # ✅ FIXED

# Show dataframe
st.dataframe(ticker_df)

# Show closing price chart
st.write("## Daily Closing Price")
st.line_chart(ticker_df.Close)

# Show volume chart
st.write("## Volume of Shares Traded")
st.line_chart(ticker_df.Volume)

# Optional explanation
with st.expander("See explanation"):
    st.write("""
        - The charts above show Apple stock's trends.
        - Hover to see tooltips. Zoom in/out for better clarity.
    """)
