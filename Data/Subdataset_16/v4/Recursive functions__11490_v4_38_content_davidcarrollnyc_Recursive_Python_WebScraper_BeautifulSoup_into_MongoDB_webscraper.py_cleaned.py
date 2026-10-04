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
    b1 = BeautifulSoup(body, 'b6.parser')
    b2 = b1.findAll(text=True)
    b3 = filter(tag_visible, b2)
    return u" ".join(t.strip() for t in b3)
def fonk3(b5):
    try:
        b4 = urllib.request.urlopen(b5)
        return b4.read()
    except HTTPError as e:
        print(f"HTTP Error: {e.code} for URL: {b5}")
        return None
def fonk4(b6):
    b1 = BeautifulSoup(b6, "b6.parser")
    return [link.attrs['href'] for link in b1.select('a[href^="http"]') if link.has_attr('href')]
def fonk5():
    b5 = 'http:
    b6 = fonk3(b5)
    if b6:
        print(fonk2(b6))
        b7 = fonk4(b6)
        for link in b7:
            print(link)
            b8 = fonk3(link)
            if b8:
                print("")
                print(fonk2(b8))
if b9 = = "__main__":
    fonk5()