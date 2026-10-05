import pandas as pd
from bs4 import BeautifulSoup
import requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}
def fetch_html(url):
    response = requests.get(url, headers=HEADERS)
    return response.text if response.status_code == 200 else None
def extract_product_data(soup):
    image_list = soup.find_all('span', {'class': 'a-button-text'})
    brand_name = soup.find('a', {'id': 'bylineInfo'})
    product_name = soup.find('span', {'id': 'productTitle'})
    rating = soup.find('span', {'class': 'a-icon-alt'})
    no_of_ratings = soup.find('span', {'id': 'acrCustomerReviewText'})
    sell_price_range = soup.find('span', {'id': 'priceblock_ourprice'})
    image_urls = [image.find('img').get('src') for image in image_list if image.find('img')]
    brand = brand_name.text.strip() if brand_name else ''
    name = product_name.text.strip() if product_name else ''
    rating_value = rating.text.strip() if rating else ''
    num_ratings = no_of_ratings.text.strip() if no_of_ratings else ''
    price = sell_price_range.text.strip() if sell_price_range else ''
    return {
        'brand_name': brand,
        'product_name': name,
        'images': str(image_urls),
        'price': price,
        'product_rating': rating_value,
        'no_of_ratings': num_ratings
    }
def get_product_details(asin_list):
    product_details = []
    for asin in asin_list:
        url = f"https:
        html_content = fetch_html(url)
        if html_content:
            soup = BeautifulSoup(html_content, 'lxml')
            product_data = extract_product_data(soup)
            product_details.append(product_data)
    return pd.DataFrame(product_details)
if __name__ == "__main__":
    asins_df = pd.read_csv('ASINs.csv')
    asin_list = asins_df['ASIN']
    df = get_product_details(asin_list)
    df.to_csv('ASIN_product_details.csv', index=False)