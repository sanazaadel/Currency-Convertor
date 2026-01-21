import streamlit as st
from currency_convertor import get_exchange_rate, convert_currency
from constants import CURRENCIES


st.title(" :dollar: Currency Converter")
st.write("Convert amounts between different currencies using real-time exchange rates.")
from_currency = st.selectbox("From Currency", CURRENCIES)
to_currency = st.selectbox("To Currency", CURRENCIES)
amount = st.number_input("Amount", min_value=0.0, format="%.2f")    

if amount > 0 and from_currency and to_currency:
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    st.success(f"Exchange Rate: {exchange_rate:.4f}") 
    if exchange_rate:
        col1, col2, col3 = st.columns(3)
        converted_amount = convert_currency(amount, exchange_rate)
        col1.metric(label="Currency from", value=f"{amount:.2f} {from_currency}")
        col2.markdown("<div style='text-align:center; font-size:28px; padding-top:30px; color:red'>→</div>",
        unsafe_allow_html=True)
        col3.metric(label="Currency to", value=f"{converted_amount:.2f} {to_currency}")
       
    else:
        st.error("Failed to retrieve exchange rate. Please try again later.")
    
st.markdown("---")
st.markdown("### About this tool")
st.markdown("""
    This currency converter tool allows you to convert amounts between different currencies using real-time exchange rates.
    - **From Currency**: Select the currency you want to convert from.
    - **To Currency**: Select the currency you want to convert to.
    - **Amount**: Enter the amount you want to convert.
    - **Exchange Rate**: The current exchange rate between the selected currencies.
    - **Converted Amount**: The amount after conversion based on the exchange rate.
    """)