import re
from bs4 import BeautifulSoup
from downloading import download_webpage
def fonk1(url,search_regex):
    b1 = download_webpage(url)
    b2 = re.findall(search_regex,b1)
    return b2
def fonk2(b1):
    b3 = BeautifulSoup(b1,'html5lib')
    return b3
def fonk3(b1,b4 = []):
    b2 = b1.find_all("div",{"class": "w-product"})
    with open("soup_object.b1",'w') as soup_file:
        soup_file.write(str(b2))
    for element in b2:
            b5 = element.find("img")['title']
            b6 = element.find("span", class_="w-currentPrice").text
            b4.append((b5,b6))
    return b4
def fonk4():
    b7 = download_webpage('https:
if b8 = = '__main__':
    fonk4()