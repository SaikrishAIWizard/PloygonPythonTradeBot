from others.ExtractNumeric import extract_numeric_value
from datetime import datetime, timedelta
import pandas as pd
from others.extract_candles import get_candle_data


def Strategy_Above(stock_name, stock_value, today, signal):
    # Fetch historical price data for the stock_name for the specified date
    #data = get_candle_data(stock_name = stock_name, multiplier_val = 1, timespan_val = "day",from_val = today - timedelta(days=360) ,to_val = today)
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
    close_price = data["close"].iloc[-1]
    previous_price = data["close"].iloc[-2]

    print("close price value is : ",close_price)
    print("previous_price value is:", previous_price)
    result = "No signal"

    numeric_values = extract_numeric_value(stock_value)[0]

    print("Input is stock: {} and strategy : {} and value : {}".format(stock_name, "Above", numeric_values))
    print("closing value is:{} and previous_price value is:{}".format(close_price,
                                                                                  previous_price))
    print("x % value is: ", (close_price - previous_price) * 100 / previous_price)

    # Above x%
    if (close_price - previous_price) * 100 / previous_price > numeric_values:
        result = signal
    print(result)
    return result
