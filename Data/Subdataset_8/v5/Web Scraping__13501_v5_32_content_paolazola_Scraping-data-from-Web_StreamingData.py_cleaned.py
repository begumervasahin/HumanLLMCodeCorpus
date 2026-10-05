import datetime
import time
import pandas as pd
import requests
from lxml import html
from random import uniform
def fetch_yahoo_realtime_data(ticker, finish_time, delta):
    url = f'https:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
    values = []
    time_now = []
    yahoo_time = []
    while datetime.datetime.now() < finish_time:
        page = requests.get(url, headers=headers)
        time.sleep(uniform(2, 3))
        parser = html.fromstring(page.content)
        value = parser.xpath('
        yahoo_time_value = parser.xpath('
        values.append(value)
        time_now.append(datetime.datetime.now())
        yahoo_time.append(yahoo_time_value)
        time.sleep(delta * 60)
    df = pd.DataFrame({'scraperTime': time_now, 'quotes': values, 'YahooPriceTime': yahoo_time})
    return df