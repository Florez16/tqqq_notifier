import yfinance as yf
from datetime import datetime
import streamlit as st


def get_ma_prices(period1, period2):
    # Define the ticker symbol for TQQQ
    ticker_symbol = "TQQQ"

    # Retrieve historical stock data using yfinance
    data = yf.download(ticker_symbol)

    # Calculate the moving average prices
    data['MA_5'] = data['Close'].rolling(window=5).mean()
    data['MA_20'] = data['Close'].rolling(window=20).mean()

    #print(data.head())

    last_row = data.iloc[-1]

    # Extract the desired values
    #close_price = last_row['Close']
    ma_5 = last_row['MA_5']
    ma_20 = last_row['MA_20']

    # Return the values
    return ma_5, ma_20


def get_signal(ma1_price, ma2_price):
    if ma1_price >= ma2_price:
        return True

    return False

def gen_message(ma1, ma2, ma1_price, ma2_price, long_signal, current_datetime):
    """
    Generate message for display
    """
    msg = \
        f"""
            {current_datetime}
            QQQ Latest MA{ma1}: ${round(ma1_price, 2)}
            QQQ Latest MA{ma2}: ${round(ma2_price, 2)}
            Long Signal: {long_signal}
        """

    if long_signal:
        msg += "\tCan buy TQQQ if you haven't do so."
    else:
        msg += "\tTime to sell TQQQ."

    return msg


def main():
    ma1 = 5
    ma2 = 20

    # Getting the close, ma5 and ma20 prices of the latest trading day
    ma1_price, ma2_price = get_ma_prices(ma1, ma2)
    #print(f"MA5: {ma1_price}, MA20: {ma2_price}")

    long_signal = get_signal(ma1_price, ma2_price)
    #print(long_signal)

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Print the current date and time
    #print("Current Date and Time:", current_datetime)

    # Get message
    message = gen_message(ma1, ma2, ma1_price, ma2_price, long_signal, current_datetime)
    st.write(message)
    print(message)

st.write("TEST")
main()
