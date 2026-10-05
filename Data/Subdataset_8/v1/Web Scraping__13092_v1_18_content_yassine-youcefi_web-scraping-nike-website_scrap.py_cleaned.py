import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as soup
from random import randint
from time import sleep
import json
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')
def scrape_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_soup = soup(response.text, 'html.parser')
        products = page_soup.find_all('div', class_='product-card__body')
        data_csv = ""
        data_json = []
        for product in products:
            product_name = product.find('div', class_='product-card__titles').text.strip()
            product_description = product.find('div', class_='product-card__subtitle').text.strip()
            product_colors = product.find('div', class_='product-card__product-count').text.strip()
            product_price = product.find('div', class_='product-price').text.strip()
            product_image = product.find('img', {'src': re.compile('.jpg')})['src']
            data_csv += f"{product_name},{product_description},{product_colors},{product_price},{url}\n"
            data_json.append({
                'name': product_name,
                'description': product_description,
                'colors': product_colors,
                'price': product_price,
                'image': product_image
            })
        return data_csv, data_json
    else:
        print(f"Failed to retrieve data from {url}")
        return "", []
def main():
    urls = [
        "https:
        "https:
    ]
    all_data_csv = ""
    all_data_json = []
    for url in urls:
        data_csv, data_json = scrape_data(url)
        all_data_csv += data_csv
        all_data_json += data_json
    with open(CSV_FILE, 'w') as csv_file:
        csv_file.write("name_product,description_product,colors_product,price_product,category\n")
        csv_file.write(all_data_csv)
    with open(JSON_FILE, 'w') as json_file:
        json.dump(all_data_json, json_file, indent=4)
if __name__ == "__main__":
    main()