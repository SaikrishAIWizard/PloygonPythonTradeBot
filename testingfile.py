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
new_dt = new_dt.replace(second=0, microsecond=0)

from Strategies.EMA import Strategy_EMA
from Strategies.Above import Strategy_Above
from Strategies.Below import Strategy_Below
from Strategies.Monthly import Strategy_Monthly
from Strategies.Weekly import Strategy_weekly

import warnings

# Suppress DeprecationWarning
warnings.simplefilter("ignore")

Strategy_EMA('AAPL', "200", new_dt, "BUY")

Strategy_Above(stock_name = "QCOM", stock_value = "1", today = new_dt, signal="BUY")

Strategy_Below(stock_name = "AAPL", stock_value = "-3", today = new_dt, signal="BUY")

Strategy_Monthly(stock_name = "DTSS", stock_value = "HIGH", today = new_dt, signal="BUY")

Strategy_Monthly(stock_name = "OMH", stock_value = "LOW", today = new_dt, signal="BUY")

Strategy_weekly(stock_name = "AAPL", stock_value = "HIGH", today = new_dt, signal="BUY")