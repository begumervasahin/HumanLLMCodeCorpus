import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
b1 = "https:
b2 = ScrapFunction.getTitle(b1)
if b2 = = None:
    print("b2 not found")
else:
    print("***b2 below here***")
    print(b2)
b3 = ScrapFunction.getBody(b1)
if b3 = = None:
    print("b3 not found")
else:
    print("***b3 below here***")
    print(b3)
b4 = ScrapFunction.getText(b1)
if b4 = = None:
    print("text not found")
else:
    print("***text below here***")
    for text in b4:
        print(text.get_text())
b5 = ScrapFunction.getHead(b1)
if b5 = = None:
    print("b5 not found")
else:
    print("***b5 below here***")
    print(b5)
b6 = ScrapFunction.getLink(b1)
if b6 = = None:
    print("b1 not found")
else:
    print("***link below here***")
    for link in b6:
        if "href" in link.attrs:
            print(link.attrs["href"])
b7 = ScrapFunction.getImg(b1)
if b7 = = None:
    print("b1 not found")
else:
    print("***link image below here***")
    for img in b7:
        print(img.attrs["data-src"])
        print(img.attrs["src"])