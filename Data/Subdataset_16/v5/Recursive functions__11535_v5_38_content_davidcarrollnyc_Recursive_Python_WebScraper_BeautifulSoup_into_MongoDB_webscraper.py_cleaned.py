from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.error import HTTPError
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b1 = BeautifulSoup(body, 'b5.parser')
    b2 = b1.findAll(text=True)
    b3 = filter(tag_visible, b2)
    return " ".join(t.strip() for t in b3)
def fonk3(b7):
    try:
        b4 = urllib.request.urlopen(b7)
        return b4.read()
    except HTTPError as e:
        print(f"HTTP Error: {e.code} for URL: {b7}")
        return None
def fonk4(b5):
    b1 = BeautifulSoup(b5, "b5.parser")
    return [link.attrs['href'] for link in b1.select('a[href^="http"]') if link.has_attr('href')]
def fonk5(b7):
    b5 = fonk3(b7)
    if b5:
        print(fonk2(b5))
        b6 = fonk4(b5)
        for link in b6:
            print(link)
            fonk5(link)
def fonk6():
    b7 = 'http:
    fonk5(b7)
if b8 = = "__main__":
    fonk6()