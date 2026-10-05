
import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https:
def print_section(section_name, content):
    if content is None:
        print(f"{section_name} not found")
    else:
        print(f"***{section_name} below here***")
        print(content)
title = ScrapFunction.getTitle(url)
print_section("Title", title)
body = ScrapFunction.getBody(url)
print_section("Body", body)
textList = ScrapFunction.getText(url)
if textList is None:
    print("Text not found")
else:
    print("***Text below here***")
    for text in textList:
        print(text.get_text())
head = ScrapFunction.getHead(url)
print_section("Head", head)
linkList = ScrapFunction.getLink(url)
if linkList is None:
    print("Links not found")
else:
    print("***Links below here***")
    for link in linkList:
        if "href" in link.attrs:
            print(link.attrs["href"])
imgList = ScrapFunction.getImg(url)
if imgList is None:
    print("Images not found")
else:
    print("***Image links below here***")
    for img in imgList:
        print(img.attrs["data-src"])
        print(img.attrs["src"])