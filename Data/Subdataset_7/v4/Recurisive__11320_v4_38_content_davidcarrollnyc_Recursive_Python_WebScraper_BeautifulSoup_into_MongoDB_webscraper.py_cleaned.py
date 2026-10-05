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
    b1 = BeautifulSoup(body, 'b4.parser')
    b2 = b1.find_all(text=True)
    b3 = filter(tag_visible, b2)
    return u" ".join(t.strip() for t in b3)
b4 = urllib.request.urlopen('http:
print(fonk2(b4))
b4 = urllib.request.urlopen('http:
b1 = BeautifulSoup(b4, "b4.parser")
b5 = b1.select('a[href^="http"]')
for link in b5:
    if link.has_attr('href'):
        print(link.attrs['href'])
        try:
            b6 = urllib.request.urlopen(link.attrs['href'])
            b7 = b6.read()
            print(b7)
        except HTTPError as e:
            continue
        print("")
        print(fonk2(b7))