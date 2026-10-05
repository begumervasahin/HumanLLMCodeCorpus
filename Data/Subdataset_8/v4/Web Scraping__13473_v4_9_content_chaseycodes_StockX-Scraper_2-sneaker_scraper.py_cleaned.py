import requests
import json
import time
import os
import random
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, ChunkedEncodingError
BRANDS = ['nike', 'jordan', 'adidas', 'other']
with open('overall.json') as file:
    DATA = json.load(file)
def tsplit(string, delimiters):
    delimiters = tuple(delimiters)
    stack = [string,]
    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)
    return stack
def brand_dict(brand):
    return_dict = {}
    _dict = DATA[brand]
    for type, sneakers in _dict.items():
        for key, value in sneakers.items():
            return_dict[key] = {
                'url': value['href'],
                'img': value['src'],
                'type': type,
                'brand': brand
            }
    return return_dict
def sneaker_scraper():
    for brand in BRANDS:
        _dict = brand_dict(brand)
        urls, err = [], ['{}'.format(brand)]
        sneaker_dict = {}
        attribute_counter = 0
        while len(_dict) > 0:
            for key, value in _dict.items():
                print('\nError Count [{}]'.format(attribute_counter))
                print('Remaining: '+str(len(_dict))+'\n')
                try:
                    url = value['url']
                    _type = value['type'].replace('-', ' ')
                    shoe_html = requests.get(url).content
                    shoe_soup = BeautifulSoup(shoe_html, 'html.parser')
                    shoe_container = shoe_soup.find("div", {"class": "product-view"})
                    header_stat = shoe_container.find_all('div', {'class': 'header-stat'})
                    ticker = header_stat[1].get_text().strip().split(' ')[1]
                    product_info = shoe_container.find_all('div', {'class': 'detail'})
                    colorway, retail_price, release_date = '--', '--', '--'
                    for info in product_info:
                        if info.get_text().split(' ')[0] == 'Style':
                            pass
                        elif info.get_text().split(' ')[0] == 'Colorway':
                            colorway = info.get_text().replace('Colorway ', '').strip()
                        elif info.get_text().split(' ')[0] == 'Retail':
                            retail_price = info.get_text().split(' ')[2].strip()
                        elif info.get_text().split(' ')[0] == 'Release':
                            release_date = info.get_text().split(' ')[2].strip()
                    twelve_month_historical = shoe_container.find('div', {'class': 'gauges'}).get_text().strip()
                    twelve_data = tsplit(twelve_month_historical, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
                    total_sales = twelve_data[1]
                    avg_sale_price = twelve_data[3]
                    market_summary = shoe_container.find('div', {'class': 'product-market-summary'}).get_text().strip()
                    market_data = tsplit(market_summary, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
                    volatility = market_data[4]
                    if _type == 'footwear':
                        _type = 'other'
                    if brand == 'jordan':
                        check = value['type'].split('-')[-1]
                        if check.isdigit():
                            _type = check
                    data = {
                        "url": url,
                        "brand": brand,
                        "type": _type,
                        "image": value['img'],
                        "ticker": ticker,
                        "colorway": colorway,
                        "retail_price": retail_price,
                        "release_date": release_date,
                        "volatility": volatility,
                        "total_sales": total_sales,
                        "avg_sale_price": avg_sale_price
                    }
                    sneaker_dict[key] = data
                    time.sleep(1/(random.randint(1, 100) * 10000))
                    print('Extracted: '+key)
                    _dict.pop(key)
                except AttributeError as e:
                    attribute_counter += 1
                    print('Attribute Error [{}]: '.format(attribute_counter))
                    print(e)
                    if attribute_counter > 100:
                        print('Problem: '+key)
                        err.append(['a', key, url])
                        _dict.pop(key)
                        attribute_counter = 0
                    pass
                except ConnectionError as e:
                    print(e)
                    err.append(['c', key, url])
                    pass
                except ChunkedEncodingError as e:
                    print(e)
                    err.append(['c', key, url])
                    pass
        with open('{}.json'.format(brand), 'w') as f:
            json.dump(sneaker_dict, f, indent=4)
            f.close()
    with open('missing.json', 'a') as f:
        json.dump(err, f, indent=4)
        f.close()
    print("Done.")
if __name__ == "__main__":
    sneaker_scraper()