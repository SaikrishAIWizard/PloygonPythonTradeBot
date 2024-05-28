from broker.polygon_broker import broker

def get_candle_data(stock_name,multiplier_val,timespan_val, from_val , to_val):
    data = broker.get_aggs(ticker=stock_name,
                           multiplier=multiplier_val,
                           timespan=timespan_val,
                           from_=from_val,
                           to=to_val)
    return data

