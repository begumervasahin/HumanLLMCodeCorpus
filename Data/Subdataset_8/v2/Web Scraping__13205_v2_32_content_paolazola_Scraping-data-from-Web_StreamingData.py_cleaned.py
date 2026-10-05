import datetime
import time
import pandas as pd
import requests
from lxml import html
from random import uniform
def fetch_real_time_stock_data(ticker, finish_time, delta_minutes):
    yahoo_finance_url = 'https:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
    stock_values = []
    scraper_timestamps = []
    yahoo_price_timestamps = []
    while datetime.datetime.now() < finish_time:
        response = requests.get(yahoo_finance_url, headers=headers)
        time.sleep(uniform(2, 3))
        parsed_content = html.fromstring(response.content)
        try:
            stock_value = parsed_content.xpath('
            yahoo_timestamp = parsed_content.xpath('
        except IndexError:
            print("Error: Failed to extract data from Yahoo Finance.")
            continue
        stock_values.append(stock_value)
        scraper_timestamps.append(datetime.datetime.now())
        yahoo_price_timestamps.append(yahoo_timestamp)
        time.sleep(delta_minutes * 60)
    data = {
        'scraper_timestamp': scraper_timestamps,
        'stock_value': stock_values,
        'yahoo_price_timestamp': yahoo_price_timestamps
    }
    df = pd.DataFrame(data)
    return df
finish_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
delta_minutes = 1
ticker_symbol = 'AAPL'
result_dataframe = fetch_real_time_stock_data(ticker_symbol, finish_time, delta_minutes)
print(result_dataframe)