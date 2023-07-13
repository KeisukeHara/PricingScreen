import streamlit as st
from datetime import date

class TradeData:
    def __init__(self, strike_price, expiration_date, option_type):
        self.strike_price = strike_price
        self.expiration_date = expiration_date
        self.option_type = option_type

# Streamlitアプリの設定
st.title("金利先物オプション 取引データ入力")

# 取引データの入力フォーム
strike_price = st.number_input("ストライク価格", value=100.0, step=0.1)
expiration_date = st.date_input("オプションの満期日", value=date.today())
option_type = st.selectbox("オプションのタイプ", ["Call", "Put"])

# 取引データの表示
trade_data = TradeData(strike_price, expiration_date, option_type)
st.header("取引データ")
st.write("ストライク価格:", trade_data.strike_price)
st.write("オプションの満期日:", trade_data.expiration_date)
st.write("オプションのタイプ:", trade_data.option_type)
