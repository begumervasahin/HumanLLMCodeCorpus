from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b1 = BeautifulSoup(body, 'b4.parser')
    b2 = b1.findAll(text=True)
    b3 = filter(tag_visible, b2)
    return u" ".join(t.strip() for t in b3)
b4 = urllib.request.urlopen('http:
print(fonk2(b4))
b4 = urllib.request.urlopen('http:
b5 = BeautifulSoup(b4, "b4.parser")
b6 = b5.select('a[href^="http"]')
for link in b6:
    if link.has_attr('href'):
        print (link.attrs['href'])
        try:
            b7 = urllib.request.urlopen(link.attrs['href'])
            b8 = b7.read()
            print(b8)
        except HTTPError as e:
            continue
        print("")
        print(fonk2(b8))