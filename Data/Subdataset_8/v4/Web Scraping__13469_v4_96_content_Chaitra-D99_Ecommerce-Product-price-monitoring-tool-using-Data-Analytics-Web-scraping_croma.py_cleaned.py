from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
my_urls = ['https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
filename = "croma.csv"
filename1 = "past_data_croma.csv"
f = open(filename, "w", encoding='utf-8')
f1 = open(filename1, "a", encoding='utf-8')
headers = "number,model,rating,offer_price,original_price,price_difference\n"
f.write(headers)
count = 1
no_of_pages = 0
for url in my_urls:
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'lxml')
    products = page_soup.find_all('li', {'class': 'product__list--item'})
    no_of_pages += 1
    for product in products:
        if count == 181:
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
        f.write(f"{count},{title},{rating},{final_price},{original_price},{price_diff}\n")
        count += 1
data = list(csv.reader(open(filename, 'r')))
data.pop(0)
price_diffs = [float(row[5]) for row in data]
mean_price = np.mean(price_diffs)
print('Mean price of Croma:', mean_price)
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
f1.write(f"{date},{mean_price}\n")
f.close()
f1.close()