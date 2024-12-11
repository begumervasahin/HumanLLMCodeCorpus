
import datetime
import time
import pandas as pd
import requests
from lxml import html
from random import uniform
def fonk1(ticker, finish_time, delta):
    b1 = 'https:
    b2 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    b3 = []
    b4 = []
    b5 = []
    while datetime.datetime.now() < finish_time:
        b6 = requests.get(b1, b2=b2)
        time.sleep(uniform(2, 3))
        b7 = html.fromstring(b6.content)
        b8 = b7.xpath('
        b9 = b7.xpath('
        b3.append(b8)
        b4.append(datetime.datetime.now())
        b5.append(b9)
        time.sleep(delta * 60)
    b10 = pd.DataFrame({'scraperTime': b4, 'quotes': b3, 'YahooPriceTime': b5})
    return b10