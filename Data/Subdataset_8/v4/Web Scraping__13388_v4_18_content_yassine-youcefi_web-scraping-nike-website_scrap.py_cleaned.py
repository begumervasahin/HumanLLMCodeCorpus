import os
import requests
from bs4 import BeautifulSoup as Soup
import json
import pandas as pd
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE_PATH = os.path.join(BASE_DIRECTORY, 'data_json.json')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
def scrape_product_data(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return [], []
    page_soup = Soup(response.text, 'html.parser')
    products = page_soup.find_all('div', class_='product-card__body')
    csv_data = []
    json_data = []
    for product in products:
        product_name = product.find('div', class_='product-card__titles').text.strip()
        product_description = product.find('div', class_='product-card__subtitle').text.strip()
        product_colors = product.find('div', class_='product-card__product-count').text.strip()
        product_price = product.find('div', class_='product-price').text.strip()
        product_image = product.find('img', {'src': re.compile('.jpg')})['src']
        csv_data.append([product_name, product_description, product_colors, product_price, url])
        json_data.append({
            'name': product_name,
            'description': product_description,
            'colors': product_colors,
            'price': product_price,
            'image': product_image
        })
    return csv_data, json_data
def main():
    urls = [
        "https:
        "https:
    ]
    all_csv_data = []
    all_json_data = []
    for url in urls:
        csv_data, json_data = scrape_product_data(url)
        all_csv_data.extend(csv_data)
        all_json_data.extend(json_data)
    pd.DataFrame(all_csv_data, columns=['Name', 'Description', 'Colors', 'Price', 'Category']).to_csv(CSV_FILE_PATH, index=False)
    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(all_json_data, json_file, indent=4)
if __name__ == "__main__":
    main()