
import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
b1 = "https:
def fonk1(section_name, content):
    if content is None:
        print(f"{section_name} not found")
    else:
        print(f"***{section_name} below here***")
        print(content)
b2 = ScrapFunction.getTitle(b1)
fonk1("Title", b2)
b3 = ScrapFunction.getBody(b1)
fonk1("Body", b3)
b4 = ScrapFunction.getText(b1)
if b4 is None:
    print("Text not found")
else:
    print("***Text below here***")
    for text in b4:
        print(text.get_text())
b5 = ScrapFunction.getHead(b1)
fonk1("Head", b5)
b6 = ScrapFunction.getLink(b1)
if b6 is None:
    print("Links not found")
else:
    print("***Links below here***")
    for link in b6:
        if "href" in link.attrs:
            print(link.attrs["href"])
b7 = ScrapFunction.getImg(b1)
if b7 is None:
    print("Images not found")
else:
    print("***Image links below here***")
    for img in b7:
        print(img.attrs["data-src"])
        print(img.attrs["src"])