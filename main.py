from datetime import datetime, timedelta
import pandas as pd
from Strategies.Above import Strategy_Above
from Strategies.Below import Strategy_Below
from Strategies.Monthly import Strategy_Monthly
from Strategies.EMA import Strategy_EMA
from Strategies.Weekly import Strategy_weekly
import time
from datetime import datetime
from others.UpdateOutput import update_excel
import warnings


# Suppress DeprecationWarning
warnings.simplefilter("ignore")


import datetime
# Get today's date
import pytz
# Get today's date
today = datetime.datetime.now()
# Convert to Eastern Standard Time (EST)
est_timezone = pytz.timezone('America/New_York')
est_dt = today.astimezone(est_timezone)
# Extract minutes value
minutes_value = est_dt.minute
flor_val = minutes_value//15
new_dt = est_dt.replace(minute=0)
new_dt = new_dt + datetime.timedelta(minutes=15*flor_val)
# Set seconds and milliseconds to zero
today = new_dt.replace(second=0, microsecond=0)

# Export DataFrame to Excel
excel_filename = "Input.xlsx"

# Read Excel sheet into DataFrame
df = pd.read_excel(excel_filename)


for j in range(len(df)):
    stock_name = (df['Stock Name'][j].strip()).upper()
    print("stock_name:",stock_name)
    stock_strategy = (df['Strategy'][j].strip()).lower()
    stock_value = str(df['value'][j]).strip()
    signal = df['Signal'][j].strip()
    result = "No signal"
    try:
        if stock_strategy == "ema":
            result = Strategy_EMA(stock_name, stock_value, today, signal)
        elif stock_strategy == "week":
            result = Strategy_weekly(stock_name, stock_value, today, signal)
        elif stock_strategy == "monthly":
            result = Strategy_Monthly(stock_name, stock_value, today, signal)
        elif stock_strategy == "above":
            result = Strategy_Above(stock_name, stock_value, today, signal)
        elif stock_strategy == "below":
            result = Strategy_Below(stock_name, stock_value, today, signal)
    except:
        print("got error while running the strategy")
        pass
    if result != "No signal":
        update_excel(stock_name, result)
        print("signal:",result)
    print(result)
    print("--------Due to using the free tier delaying 20 secs using time the API calls(4 calls per minute)--------\n")
    #time.sleep(25)