from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
URL_PREFIX = 'https:
QUERY_SUFFIX = '?q=%3Arelevance%3AskuStockFlag%3Atrue&page='
NUM_PAGES = 10
MAX_PRODUCTS = 180
MAIN_FILENAME = "croma.csv"
PAST_DATA_FILENAME = "past_data_croma.csv"
main_file = open(MAIN_FILENAME, "w", encoding='utf-8')
past_data_file = open(PAST_DATA_FILENAME, "a", encoding='utf-8')
MAIN_HEADERS = "number,model,rating,offer_price,original_price,price_difference\n"
main_file.write(MAIN_HEADERS)
product_count = 1
page_count = 0
for page_num in range(1, NUM_PAGES + 1):
    page_url = f"{URL_PREFIX}{QUERY_SUFFIX}{page_num}"
    uClient = uReq(page_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'lxml')
    products = page_soup.find_all('li', {'class': 'product__list--item'})
    page_count += 1
    for product in products:
        if product_count > MAX_PRODUCTS:
            break
        title = product.find('a', class_='product__list--name').text.strip().lower().replace(",", "")
        if title.startswith('xiaomi'):
            title = title.replace('xiaomi', 'redmi')
        final_price = product.find('div', class_='col-md-4 col-xs-8').find('span', class_='pdpPrice').text.strip().replace("â¹", "").replace(",", "")
        try:
            original_price = product.find('span', class_='pdpPriceMrp').text.strip().replace("â¹", "").replace(",", "")
        except AttributeError:
            original_price = final_price
        try:
            rating = len(product.find('div', class_='col-xs-12 col-sm-4 col-md-3').find('div', class_='rating').find_all('span', class_='glyphicon glyphicon-star active'))
        except AttributeError:
            rating = 0
        price_diff = float(original_price) - float(final_price)
        main_file.write(f"{product_count},{title},{rating},{final_price},{original_price},{price_diff}\n")
        product_count += 1
data = list(csv.reader(open(MAIN_FILENAME, 'r')))
data.pop(0)
price_diffs = [float(row[5]) for row in data]
mean_price = np.mean(price_diffs)
print('Mean price of Croma:', mean_price)
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
past_data_file.write(f"{date},{mean_price}\n")
main_file.close()
past_data_file.close()