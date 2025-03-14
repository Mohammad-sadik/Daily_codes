import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta


st.set_page_config(
    page_title = "Stock Analysis",
    page_icon = 'page_with_curl:',
    layout = 'wide'
)
st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)
today = datetime.date.today()

with col1:
    ticket = st.text_input("Stock Ticker","TSLA")
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year-1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose End Date", datetime.date(today.year, today.month, today.day))
st.subheader(ticket)

stock = yf.Ticker(ticket)
st.write(stock.info['longBusinessSummary'])
st.write("**Sector:** ", stock.info["sector"])
st.write("**Full Time Employees:** " ,stock.info["fullTimeEmployees"])
st.write("**Website:** ", stock.info["website"])

col1, col2 = st.columns(2)
with col1:
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [stock.info['marketCap'], stock.info['beta'], stock.info['trailingEps'], stock.info['trailingPE']]
    #st.plotly_chart(df, use_container_width= True)

with col2:
    df =pd.DataFrame(index=['Qick Ratio', 'Revenue Per Share', 'Profit Margin', 'Debt to Equity', 'Return on Equity'])
    df['']=[stock.info['quickRatio'], stock.info['revenuePerShare'], stock.info['profitMargins'], stock.info['debtToEquity'], stock.info['returnOnEquity']]
    #st.plotly_chart(df, use_container_width= True)
