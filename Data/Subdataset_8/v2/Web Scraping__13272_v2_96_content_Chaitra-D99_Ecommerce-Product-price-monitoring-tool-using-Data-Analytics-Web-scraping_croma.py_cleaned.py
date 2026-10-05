from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
urls = [
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
]
output_filename = "croma.csv"
past_data_filename = "past_data_croma.csv"
output_file = open(output_filename, "w", encoding='utf-8')
past_data_file = open(past_data_filename, "a", encoding='utf-8')
output_headers = "number,model,rating,offer_price,original_price,price_difference\n"
output_file.write(output_headers)
product_count = 1
page_count = 0
for url in urls:
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    products = page_soup.find_all('li', {'class': 'product__list--item'})
    page_count += 1
    for product in products:
        if product_count == 181:
            break
        title = product.find('a', class_='product__list--name').text.strip().lower().replace(',', '')
        if title.startswith('xiaomi'):
            title = title.replace('xiaomi', 'redmi')
        final_price = product.find('span', class_='pdpPrice').text.strip().replace('â¹', '').replace(',', '')
        try:
            original_price = product.find('span', class_='pdpPriceMrp').text.strip().replace('â¹', '').replace(',', '')
        except AttributeError:
            original_price = final_price
        try:
            rating = len(product.find('div', class_='greenStars').find_all('span', class_='glyphicon glyphicon-star active'))
        except AttributeError:
            rating = 0
        price_diff = float(original_price) - float(final_price)
        output_file.write(f"{product_count},{title},{rating},{final_price},{original_price},{price_diff}\n")
        product_count += 1
output_file.close()
prices = []
with open(output_filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        prices.append(float(row[5]))
mean_price = np.mean(prices)
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
past_data_file.write(f"{current_date},{mean_price}\n")
past_data_file.close()
print("\nProducts Count:", product_count)
print("Pages Count:", page_count)
print('Mean price of Croma:', mean_price)
print("Date:", current_date)