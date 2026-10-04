import pandas as pd
import requests
from bs4 import BeautifulSoup as bsoup
def fetch_and_write_data():
    with open('data.csv', 'a+') as f:
        for year in [2016, 2015, 2014, 2013]:
            for week in range(1, 17):
                url = f'http:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = bsoup(response.content, 'html.parser')
                    pre_tags = soup.find_all('pre')
                    if pre_tags:
                        f.write(pre_tags[0].get_text())
                else:
                    print(f"Failed to retrieve data for year {year}, week {week}")
    return pre_tags
if __name__ == '__main__':
    pre_tags = fetch_and_write_data()