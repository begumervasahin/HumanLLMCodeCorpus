
import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https:
title = ScrapFunction.getTitle(url)
if title == None:
    print("Title not found")
else:
    print("***Title below here***")
    print(title)
body = ScrapFunction.getBody(url)
if body == None:
    print("Body not found")
else:
    print("***Body below here***")
    print(body)
textList = ScrapFunction.getText(url)
if textList == None:
    print("Text not found")
else:
    print("***Text below here***")
    for text in textList:
        print(text.get_text())
head = ScrapFunction.getHead(url)
if head == None:
    print("Head not found")
else:
    print("***Head below here***")
    print(head)
linkList = ScrapFunction.getLink(url)
if linkList == None:
    print("Links not found")
else:
    print("***Links below here***")
    for link in linkList:
        if "href" in link.attrs:
            print(link.attrs["href"])
imgList = ScrapFunction.getImg(url)
if imgList == None:
    print("Images not found")
else:
    print("***Image links below here***")
    for img in imgList:
        print(img.attrs["data-src"])
        print(img.attrs["src"])