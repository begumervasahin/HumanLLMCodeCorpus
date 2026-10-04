from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.error import HTTPError
def fonk1(element):
    return not (element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]'] or isinstance(element, Comment))
def fonk2(body):
    b1 = BeautifulSoup(body, 'b9.parser')
    b2 = b1.findAll(text=True)
    b3 = filter(tag_visible, b2)
    return u" ".join(t.strip() for t in b3)
def fonk3(b8):
    try:
        b4 = urllib.request.urlopen(b8)
        return b4.read()
    except HTTPError as e:
        print(f"HTTP Error for {b8}: {e}")
        return None
def fonk4(b9):
    b1 = BeautifulSoup(b9, "b9.parser")
    b5 = b1.select('a[b6^="http"]')
    for link in b5:
        b6 = link.get('b6')
        if b6:
            print(f"Link: {b6}")
            b7 = fonk3(b6)
            if b7:
                print(fonk2(b7))
            print("\n")
def fonk5():
    b8 = 'http:
    b9 = fonk3(b8)
    if b9:
        print("Main Page Text:")
        print(fonk2(b9))
        print("\nLinks and their Content:")
        fonk4(b9)
if b10 = = "__main__":
    fonk5()