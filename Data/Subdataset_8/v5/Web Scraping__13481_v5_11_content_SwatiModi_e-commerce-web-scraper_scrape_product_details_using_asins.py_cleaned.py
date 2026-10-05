import pandas as pd
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}
asin_df = pd.read_csv('ASINs.csv')
asin_list = asin_df['ASIN']
CSS_CLASSES = {
    'image_list_span': 'a-button-text',
    'brand_name': 'bylineInfo',
    'product_name': 'productTitle',
    'rating': 'a-icon-alt',
    'no_of_ratings': 'acrCustomerReviewText'
}
PRICE_IDS = ['priceblock_saleprice', 'priceblock_ourprice']
product_data = {
    'product_name': [],
    'brand_name': [],
    'images': [],
    'price': [],
    'product_rating': [],
    'no_of_ratings': []
}
for asin in asin_list:
    url = f"https:
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    image_list = soup.find_all('span', {'class': CSS_CLASSES['image_list_span']})
    brand_name = soup.find('a', {'id': CSS_CLASSES['brand_name']})
    product_name = soup.find('span', {'id': CSS_CLASSES['product_name']})
    rating = soup.find('span', {'class': CSS_CLASSES['rating']})
    no_of_ratings = soup.find('span', {'id': CSS_CLASSES['no_of_ratings']})
    price = soup.find('span', {'id': PRICE_IDS})
    image_urls = [image.find('img').get('src') for image in image_list if image.find('img')]
    product_data['brand_name'].append(brand_name.text.strip() if brand_name else '')
    product_data['product_name'].append(product_name.text.strip() if product_name else '')
    product_data['images'].append(str(image_urls))
    product_data['product_rating'].append(rating.text.strip() if rating else '')
    product_data['no_of_ratings'].append(no_of_ratings.text.strip() if no_of_ratings else '')
    product_data['price'].append(price.text.strip() if price else '')
df = pd.DataFrame(product_data)
df.to_csv('ASIN_product_details.csv', index=False)