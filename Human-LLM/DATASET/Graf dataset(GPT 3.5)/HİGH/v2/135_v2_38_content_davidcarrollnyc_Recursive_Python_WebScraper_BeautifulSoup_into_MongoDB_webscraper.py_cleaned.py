from bs4 import BeautifulSoup, Comment
import urllib.request
from urllib.error import HTTPError
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b1 = BeautifulSoup(body, 'b10.parser')
    b2 = b1.find_all(text=True)
    b3 = filter(tag_visible, b2)
    return u" ".join(t.strip() for t in b3)
def fonk3(b10):
    b4 = BeautifulSoup(b10, "b10.parser")
    b5 = b4.select('a[href^="http"]')
    for link in b5:
        if link.has_attr('href'):
            print("Link:", link.attrs['href'])
            try:
                b6 = urllib.request.urlopen(link.attrs['href'])
                b7 = b6.read()
                print("HTML Content:", b7)
                print("")
                print("Text from HTML:", fonk2(b7))
            except HTTPError as e:
                print("HTTP Error:", e)
                continue
if b8 = = "__main__":
    b9 = 'http:
    try:
        b10 = urllib.request.urlopen(b9).read()
        print("Visible Text from HTML:", fonk2(b10))
        print("\nExtracted Links with Text:")
        fonk3(b10)
    except HTTPError as e:
        print("HTTP Error:", e)