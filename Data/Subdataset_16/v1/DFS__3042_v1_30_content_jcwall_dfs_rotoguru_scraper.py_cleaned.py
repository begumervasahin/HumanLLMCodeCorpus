import pandas as pd
import requests
from bs4 import BeautifulSoup as bsoup
def fonk1():
    with open('data.csv', 'a+') as f:
        for year in [2016, 2015, 2014, 2013]:
            for week in range(1, 17):
                b1 = f'http:
                b2 = requests.get(b1)
                if b2.b3 = = 200:
                    b4 = bsoup(b2.content, 'html.parser')
                    b5 = b4.find_all('pre')
                    if b5:
                        f.write(b5[0].get_text())
                else:
                    print(f"Failed to retrieve data for year {year}, week {week}")
    return b5
if b6 = = '__main__':
    b5 = fonk1()