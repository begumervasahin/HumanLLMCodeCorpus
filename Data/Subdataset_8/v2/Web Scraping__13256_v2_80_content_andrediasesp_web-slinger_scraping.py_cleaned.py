import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def regex_scrap(url, search_regex):
    html_content = download_webpage(url)
    matches = re.findall(search_regex, html_content)
    return matches
def soup_html(html_content):
    soup = BeautifulSoup(html_content, 'html5lib')
    return soup
def search_soup(html_content, info=[]):
    soup = soup_html(html_content)
    products = soup.find_all("div", {"class": "w-product"})
    with open("soup_object.html", 'w') as soup_file:
        soup_file.write(str(products))
    for product in products:
        game = product.find("img")['title']
        price = product.find("span", class_="w-currentPrice").text
        info.append((game, price))
    return info
def main():
    url = 'https:
    page_content = download_webpage(url)
    scraped_info = search_soup(page_content)
    print(scraped_info)
if __name__ == '__main__':
    main()