
import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
b1 = "https:
b2 = ScrapFunction.getTitle(b1)
if b2 = = None:
    print("Title not found")
else:
    print("***Title below here***")
    print(b2)
b3 = ScrapFunction.getBody(b1)
if b3 = = None:
    print("Body not found")
else:
    print("***Body below here***")
    print(b3)
b4 = ScrapFunction.getText(b1)
if b4 = = None:
    print("Text not found")
else:
    print("***Text below here***")
    for text in b4:
        print(text.get_text())
b5 = ScrapFunction.getHead(b1)
if b5 = = None:
    print("Head not found")
else:
    print("***Head below here***")
    print(b5)
b6 = ScrapFunction.getLink(b1)
if b6 = = None:
    print("Links not found")
else:
    print("***Links below here***")
    for link in b6:
        if "href" in link.attrs:
            print(link.attrs["href"])
b7 = ScrapFunction.getImg(b1)
if b7 = = None:
    print("Images not found")
else:
    print("***Image links below here***")
    for img in b7:
        print(img.attrs["data-src"])
        print(img.attrs["src"])