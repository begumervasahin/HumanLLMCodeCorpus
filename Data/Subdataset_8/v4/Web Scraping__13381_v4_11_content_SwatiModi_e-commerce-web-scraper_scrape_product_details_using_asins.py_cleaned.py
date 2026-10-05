import pandas as pd
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}
asins_df = pd.read_csv('ASINs.csv')
asin_list = asins_df['ASIN']
image_list_span_class = 'a-button-text'
brand_name_class = 'bylineInfo'
product_name_class = 'productTitle'
rating_class = 'a-icon-alt'
no_of_rat_class = 'acrCustomerReviewText'
sell_price_id = 'priceblock_saleprice'
sell_price_range_id = 'priceblock_ourprice'
product_names = []
brand_names = []
ratings = []
no_of_ratings = []
product_images = []
product_prices = []
for asin in asin_list:
    url = "https:
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    image_list = soup.find_all('span', {'class': image_list_span_class})
    brand_name = soup.find_all('a', {'id': brand_name_class})
    product_name = soup.find_all('span', {'id': product_name_class})
    rating = soup.find_all('span', {'class': rating_class})
    no_of_rat = soup.find_all('span', {'id': no_of_rat_class})
    sell_price_range = soup.find('span', {'id': sell_price_range_id})
    image_urls = []
    for image in image_list:
        try:
            image_url = image.find('img').get('src')
            image_urls.append(image_url)
        except:
            pass
    product_images.append(str(image_urls))
    brand_names.append(brand_name[0].text.strip() if brand_name else '')
    product_names.append(product_name[0].text.strip() if product_name else '')
    ratings.append(rating[0].text.strip() if rating else '')
    no_of_ratings.append(no_of_rat[0].text.strip() if no_of_rat else '')
    product_prices.append(sell_price_range.text.strip() if sell_price_range else '')
df = pd.DataFrame({
    'product_name': product_names,
    'brand_name': brand_names,
    'images': product_images,
    'price': product_prices,
    'product_rating': ratings,
    'no. of ratings': no_of_ratings
})
df.to_csv('ASIN_product_details.csv', index=False)