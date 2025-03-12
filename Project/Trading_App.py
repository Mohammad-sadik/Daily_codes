import streamlit as st
st.set_page_config(
    page_title = "Trading App",
    page_icon = 'heavy_dollar_sign:',
    layout = 'wide'
)
st.title("Trading Guid App :bar_chart:")

st.header("We provide the Greatest platform for you to collect all information prior to invest in stocks.")
st.image("app.png")
st.markdown("## We provide the following services:")

st.markdown("#### :one: Stock Information")
st.write("Through this page, you can see all information about stock. ")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing price for the next30 days based on historical stock data and adavantages.")

st.markdown("#### :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculate the expected return of different stocks.")

st.markdown("#### :four: CAPM Beta")
st.write("Calculate Best and Expected for Individual stocks.")
