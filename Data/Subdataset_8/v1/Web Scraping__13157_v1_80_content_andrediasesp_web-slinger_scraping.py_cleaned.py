import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def regex_scrap(url, search_regex):
    html = download_webpage(url)
    content = re.findall(search_regex, html)
    return content
def soup_html(html):
    soup = BeautifulSoup(html, 'html5lib')
    return soup
def search_soup(html, info=[]):
    content = html.find_all("div", {"class": "w-product"})
    with open("soup_object.html", 'w') as soup_file:
        soup_file.write(str(content))
    for element in content:
        game = element.find("img")['title']
        price = element.find("span", class_="w-currentPrice").text
        info.append((game, price))
    return info
def main():
    url = 'https:
    page = download_webpage(url)
    soup = soup_html(page)
    info = search_soup(soup)
    print(info)
if __name__ == '__main__':
    main()