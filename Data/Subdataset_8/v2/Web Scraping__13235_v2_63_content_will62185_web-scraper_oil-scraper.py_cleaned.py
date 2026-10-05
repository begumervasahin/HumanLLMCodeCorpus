from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referrer': 'https:
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
def get_promotion_info(url, dealer_index):
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")
    promo_titles = soup.find_all("div", class_="promo-title text-center h1")
    promo_prices = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")
    for title, price in zip(promo_titles, promo_prices):
        title_text = title.get_text(strip=True)
        price_text = price.get_text(strip=True)
        if "oil" in title_text.lower():
            return {
                'Dealer': dealer_index,
                'URL': url,
                'Product': title_text,
                'Price': price_text[1:8]
            }
    return None
def main():
    urls = [
        "https:
        "https:
    ]
    promotions = []
    for dealer_index, url in enumerate(urls):
        promotion_info = get_promotion_info(url, dealer_index)
        if promotion_info:
            promotions.append(promotion_info)
    if promotions:
        promotions_df = pd.DataFrame(promotions)
        print(promotions_df)
    else:
        print("No oil change promotions were found.")
if __name__ == "__main__":
    main()