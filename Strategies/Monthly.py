from datetime import datetime, timedelta
import pandas as pd
from others.extract_candles import get_candle_data

def Strategy_Monthly(stock_name, stock_value, today, signal):
    # Fetch historical price data for the stock_name for the specified date
    new_dt = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    print(new_dt)
    data = get_candle_data(stock_name=stock_name, multiplier_val=1, timespan_val="day",
                           from_val=new_dt,
                           to_val=today)

    data1 = get_candle_data(stock_name=stock_name, multiplier_val=15, timespan_val="minute",
                           from_val=today - timedelta(days=10),
                           to_val=today)

    data = pd.DataFrame(data)
    data1 = pd.DataFrame(data1)
    # print(data)
    # create Date column
    try:
        data['Date'] = data['timestamp'].apply(lambda x: pd.to_datetime(x * 1000000))
        data1['Date'] = data1['timestamp'].apply(lambda x: pd.to_datetime(x * 1000000))
    except:
        print("Please check the stock ticker name no data loaded")
    data = data.set_index('Date')
    data1 = data1.set_index('Date')


    #close_val = data['close']
    # Calculate Monthly Low
    monthly_low = min(data['low'].iloc[:-1])

    # Calculate Monthly High
    monthly_high = max(data['high'].iloc[:-1])

    # current_price, previous_close
    current_close_value = data1['close'].iloc[-1]

    print("current close value :",data['close'].iloc[-1])


    result = "No signal"

    print("Monthly low value  : {} and Monthly high value : {} and the current day high value : {}".format(monthly_low,monthly_high,current_close_value))

    # Monthly strategy
    if stock_value.lower() == 'low':
        if current_close_value < monthly_low:
            result = signal
    elif stock_value.lower() == 'high':
        if current_close_value > monthly_high:
            result = signal
    print(result)
    return result
