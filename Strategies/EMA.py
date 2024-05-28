import polygon
from others.ExtractNumeric import extract_numeric_value
from datetime import datetime, timedelta
import pandas as pd
from others.extract_candles import get_candle_data
import pytz


def Strategy_EMA(stock_name, stock_value, today, signal):
    # Fetch historical price data for the stock_name for the specified date
    new_dt = today.replace(hour=0, minute=0, second=0, microsecond=0)

    data = get_candle_data(stock_name=stock_name, multiplier_val=15, timespan_val="minute",
                           from_val=new_dt - timedelta(days=12),
                           to_val=today)
    data = pd.DataFrame(data)

    # Assuming 'data' is your DataFrame and 'timestamp' column contains datetime objects
    from datetime import time

    # Define market open and close times
    market_open = time(9, 30)  # Assuming market opens at 9:30 AM
    market_close = time(16, 0)  # Assuming market closes at 4:00 PM

    # Assuming 'data' is your DataFrame
    # Assuming 'data' is a DataFrame containing your data
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

    data = data[(data['timestamp'].dt.time >= market_open) & (data['timestamp'].dt.time <= market_close)]

    #create Date column
    try:
        data['Date'] = data['timestamp'].copy()
    except:
        print("Please check the stock ticker name no data loaded")
    data = data.set_index('Date')


    # Assuming 'data' is your DataFrame
    data.to_csv('output.csv')

    minute_closing_prices = data['close']
    numeric_values = int(extract_numeric_value(stock_value)[0])

    # Calculate Exponential Moving Average (EMA)
    ema_200 = minute_closing_prices.ewm(span=numeric_values,min_periods=0).mean().iloc[-1]
    result = "No signal"
    print("Input is stock: {} and strategy : {} and value : {}".format(stock_name,"EMA",numeric_values))
    print("closing value is:{} and 15 mins before the closing value is:{}".format(minute_closing_prices[-1],minute_closing_prices[-2]))
    print("ema value is: ",ema_200)
    if minute_closing_prices[-1] > ema_200 and minute_closing_prices[-2] < ema_200:
        # Check for EMA cross
        result = signal
    print(result)
    return result
