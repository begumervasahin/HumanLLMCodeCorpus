import datetime
import time
import pandas as pd
import requests
from lxml import html
from random import uniform
def fonk1(b12, b11, a1):
    b1 = 'https:
    b2 = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
    b3 = []
    b4 = []
    b5 = []
    while datetime.datetime.now() < b11:
        b6 = requests.get(b1, b2=b2)
        time.sleep(uniform(2, 3))
        b7 = html.fromstring(b6.content)
        try:
            b8 = b7.xpath('
            b9 = b7.xpath('
        except IndexError:
            print("Error: Failed to extract data from Yahoo Finance.")
            continue
        b3.append(b8)
        b4.append(datetime.datetime.now())
        b5.append(b9)
        time.sleep(a1 * 60)
    b10 = pd.DataFrame({
        'scraperTime': b4,
        'quotes': b3,
        'YahooPriceTime': b5
    })
    return b10
b11 = datetime.datetime.now() + datetime.timedelta(minutes=5)
a1 = 1
b12 = 'AAPL'
b13 = fonk1(b12, b11, a1)
print(b13)