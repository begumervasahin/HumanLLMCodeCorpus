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
    return u" ".join(t.strip() for t in b3)
def fonk3():
    b4 = 'http:
    try:
        b5 = urllib.request.urlopen(b4).read()
        print(fonk2(b5))
        b6 = BeautifulSoup(b5, "b5.parser")
        b7 = b6.select('a[href^="http"]')
        for link in b7:
            if link.has_attr('href'):
                print(link.attrs['href'])
                try:
                    b8 = urllib.request.urlopen(link.attrs['href'])
                    b9 = b8.read()
                    print(b9)
                except HTTPError as e:
                    print(f"HTTP Error for {link.attrs['href']}: {e}")
                    continue
                print("")
                print(fonk2(b9))
    except HTTPError as e:
        print(f"HTTP Error for {b4}: {e}")
if b10 = = "__main__":
    fonk3()