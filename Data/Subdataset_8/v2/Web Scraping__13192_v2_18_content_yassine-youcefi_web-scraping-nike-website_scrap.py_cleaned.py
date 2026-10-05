import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')
def extract_urls(url_list):
    category_urls = {}
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        category_name = soup.find("h1", {"class": "wall-header__title"}).text
        category_urls[category_name] = url
    return category_urls
def scrape_data(url, category):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("div", {"class": "product-card__body"})
    data_json = []
    data_csv = []
    for product in products:
        try:
            product_name = product.find('div', {"class": "product-card__titles"}).text.strip()
            product_description = product.find('div', {"class": "product-card__subtitle"}).text.strip()
            product_colors = product.find('div', {"class": "product-card__product-count"}).text.strip()
            product_price = product.find('div', {"class": "product-price css-11s12ax is--current-price"}).text.strip()
            product_image = product.find('img')['src']
            data_csv.append([product_name, product_description, product_colors, product_price, category])
            data_json.append({"name": product_name, "description": product_description, "colors": product_colors, "price": product_price, "image": product_image})
        except Exception as e:
            print("Error processing product:", e)
    return data_csv, data_json
if __name__ == '__main__':
    urls = ["https:
            "https:
    category_urls = extract_urls(urls)
    all_csv_data = []
    all_json_data = []
    for category, url in category_urls.items():
        csv_data, json_data = scrape_data(url, category)
        all_csv_data.extend(csv_data)
        all_json_data.extend(json_data)
    df_csv = pd.DataFrame(all_csv_data, columns=["Name", "Description", "Colors", "Price", "Category"])
    df_csv.to_csv(CSV_FILE, index=False)
    with open(JSON_FILE, 'w') as json_f:
        json_f.write(json.dumps(all_json_data, indent=4))