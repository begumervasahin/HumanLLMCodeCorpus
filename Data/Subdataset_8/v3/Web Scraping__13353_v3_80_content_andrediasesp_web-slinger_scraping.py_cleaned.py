import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def scrape_url_with_regex(url, search_regex):
    html_content = download_webpage(url)
    matches = re.findall(search_regex, html_content)
    return matches
def create_soup_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html5lib')
    return soup
def extract_product_info(soup):
    products = soup.find_all("div", {"class": "w-product"})
    with open("soup_object.html", 'w') as soup_file:
        soup_file.write(str(products))
    product_info = []
    for product in products:
        game = product.find("img")['title']
        price = product.find("span", class_="w-currentPrice").text
        product_info.append((game, price))
    return product_info
def main():
    url = 'https:
    page_content = download_webpage(url)
    soup = create_soup_from_html(page_content)
    product_info = extract_product_info(soup)
    print(product_info)
if __name__ == '__main__':
    main()