from datetime import datetime, timedelta
import pandas as pd
from others.extract_candles import get_candle_data

def Strategy_weekly(stock_name, stock_value, today, signal):
    # Fetch historical price data for the stock_name for the specified date
    new_dt = today.replace(hour=0, minute=0, second=0, microsecond=0)
    week = new_dt.weekday()
    new_dt = new_dt - timedelta(days=week)

    data = get_candle_data(stock_name=stock_name, multiplier_val=15, timespan_val="minute",
                           from_val=new_dt,
                           to_val=today)
    data = pd.DataFrame(data)

    data1 = get_candle_data(stock_name=stock_name, multiplier_val=1, timespan_val="day",
                           from_val=new_dt,
                           to_val=today)
    data1 = pd.DataFrame(data1)

    # create Date column
    try:
        data['Date'] = data['timestamp'].apply(lambda x: pd.to_datetime(x * 1000000))
        data1['Date'] = data1['timestamp'].apply(lambda x: pd.to_datetime(x * 1000000))
    except:
        print("Please check the stock ticker name no data loaded")
    data = data.set_index('Date')
    data1 = data1.set_index('Date')


    # Extract closing prices and calculate metrics

    # Calculate Weekly Low
    weekly_low = min(data1['low'].iloc[:-1])

    # Calculate Weekly high
    weekly_high = max(data1['high'].iloc[:-1])  # Weekly high price

    # current_price, previous_close
    current_price = data['close'].iloc[-1]

    result = "No signal"

    print("close value :", current_price)

    #print(data1.tail())

    print("Weekly high value : {} and Weekly low value : {} and the current value : {}".format(weekly_high,
                                                                                                 weekly_low,
                                                                                                 current_price))

    # Week strategy
    if stock_value.lower() == 'high':
        if current_price > weekly_high:
            result = signal
    elif stock_value.lower() == 'low':
        if current_price < weekly_low:
            result = signal
    print(result)
    return result
