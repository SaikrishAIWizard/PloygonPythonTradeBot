from others.ExtractNumeric import extract_numeric_value
import polygon
from datetime import datetime, timedelta
import pandas as pd
from others.extract_candles import get_candle_data

def Strategy_Below(stock_name, stock_value, today, signal):

    # Fetch historical price data for the stock_name for the specified date
    #data = get_candle_data(stock_name=stock_name, multiplier_val=1, timespan_val="day",from_val=today - timedelta(days=360),to_val=today)
    data = get_candle_data(stock_name=stock_name, multiplier_val=1, timespan_val="day",
                           from_val=today - timedelta(days=10),
                           to_val=today)
    data = pd.DataFrame(data)

    # create Date column
    try:
        data['Date'] = data['timestamp'].apply(lambda x: pd.to_datetime(x * 1000000))
    except:
        print("Please check the stock ticker name no data loaded")
    data = data.set_index('Date')

    # Extract closing prices and calculate metrics
    closing_prices = data['close']

    # current_price, previous_close
    current_price = data["close"].iloc[-1]
    previous_close = data["close"].iloc[-2]

    result = "No signal"
    # Below x%
    numeric_values = extract_numeric_value(stock_value)[0]
    numeric_values = -1 * numeric_values
    print("current_price : {} previous_price : {} percentage_value : {}".format(current_price, previous_close,
                                                                                numeric_values))
    print("stock change percentage",(current_price - previous_close)*100 / previous_close)
    if (current_price - previous_close) * 100 / previous_close < numeric_values:
        result = signal
    print(result)
    return result
