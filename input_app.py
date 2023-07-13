import streamlit as st
import requests
import json
from datetime import date

# リクエストURL
URL = "https://intfutoppricing.onrender.com/calc/calc_pv/"

# Streamlitアプリの設定
st.title("金利先物オプション時価計算画面")

# 取引データの入力フォーム
st.header("取引データ入力")
strike_price = st.number_input("ストライク価格", value=100.0, step=0.1)
expiration_date = st.text_input("オプションの満期日", value="20230914")
amount = st.number_input("額面", value=1000000)
call_put = st.selectbox("Call/Put", ["C", "P"])
buy_sell = st.selectbox("Buy/Sell", ["B", "S"])

# マーケットデータの入力フォーム
st.header("マーケットデータ入力")
evaluation_date = st.text_input("評価日", value="20230712")
spot_date = st.text_input("スポット日", value="20230714")
interest_rate = st.number_input("金利", value=0.01, step=0.001)
volatility = st.number_input("ボラティリティ", value=0.2, step=0.001)
underlying_price = st.number_input("原資産価格", value=105.0, step=0.001)

# 計算リクエスト
body = {
  "trade_data": {
    "trade_id": "string",
    "ccy": "string",
    "strike": strike_price,
    "expiration_date": expiration_date,
    "call_put": call_put,
    "buy_sell": buy_sell,
    "amount": amount
  },
  "market_data": {
    "evaluation_date": evaluation_date,
    "spot_date": spot_date,
    "interest_rate": interest_rate,
    "volatility": volatility,
    "underlying_price": underlying_price
  }
}

res = requests.post(URL, json.dumps(body))

# 計算結果の表示
st.header("計算結果")
st.write("premium:", res.json()["premium"])
st.write("pv:", res.json()["pv"])