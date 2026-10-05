import datetime
import time
import pandas as pd
import requests
from lxml import html
from random import uniform
def Yahoo_realTime(ticker, finish_time, delta):
    url  = 'https:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
    list_values = []
    list_timeNow = []
    list_timeYahoo = []
    while datetime.datetime.now() < finish_time:
        page = requests.get(url, headers=headers)
        time.sleep(uniform(2, 3))
        parser = html.fromstring(page.content)
        try:
            value = parser.xpath('
            yahooTime = parser.xpath('
        except IndexError:
            print("Error: Failed to extract data from Yahoo Finance.")
            continue
        list_values.append(value)
        list_timeNow.append(datetime.datetime.now())
        list_timeYahoo.append(yahooTime)
        time.sleep(delta * 60)
    dataframe = pd.DataFrame({
        'scraperTime': list_timeNow,
        'quotes': list_values,
        'YahooPriceTime': list_timeYahoo
    })
    return dataframe
finish_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
delta = 1
ticker = 'AAPL'
result_df = Yahoo_realTime(ticker, finish_time, delta)
print(result_df)