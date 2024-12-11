import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def fonk1(b8, search_regex):
    b1 = download_webpage(b8)
    b2 = re.findall(search_regex, b1)
    return b2
def fonk2(b1):
    b3 = BeautifulSoup(b1, 'html5lib')
    return b3
def fonk3(b1, b4 = []):
    b3 = fonk2(b1)
    b5 = b3.find_all("div", {"class": "w-product"})
    with open("soup_object.html", 'w') as soup_file:
        soup_file.write(str(b5))
    for product in b5:
        b6 = product.find("img")['title']
        b7 = product.find("span", class_="w-currentPrice").text
        b4.append((b6, b7))
    return b4
def fonk4():
    b8 = 'https:
    b9 = download_webpage(b8)
    b10 = fonk3(b9)
    print(b10)
if b11 = = '__main__':
    fonk4()