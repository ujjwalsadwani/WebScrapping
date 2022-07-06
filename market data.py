import string
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import sys

api_key = "<Your API key>"  # Get your API key from alpha vantage website

series = TimeSeries(key=api_key, output_format="pandas")
sym = input("Enter the 'SYMBOL' of the Stock:\n")
try:
    data, meta_data = series.get_intraday(symbol=sym, interval="1min", outputsize="full")
    print(data)
except Exception as e:
    print(f"Oops! {e.__class__} occurred.")

i=1
while i==1:
    data, meta_data = series.get_intraday(symbol=sym, interval="1min", outputsize="full")
    print(data)
    data.to_csv("output.csv")
    time.sleep(30)
