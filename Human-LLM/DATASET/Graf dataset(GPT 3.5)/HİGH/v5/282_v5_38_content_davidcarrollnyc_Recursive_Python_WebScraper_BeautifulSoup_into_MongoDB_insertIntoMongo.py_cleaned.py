from bs4 import BeautifulSoup, Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
b1 = "mongodb:
b2 = 'HTML_content'
b3 = MongoClient(b1)
b4 = b3['heroku_XXXXX']
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b5 = BeautifulSoup(body, 'b8.parser')
    b6 = b5.findAll(text=True)
    b7 = filter(is_visible, b6)
    return " ".join(t.strip() for t in b7)
def fonk3(b16):
    try:
        b8 = urllib.request.urlopen(b16).read()
        b5 = BeautifulSoup(b8, "b8.parser")
        b9 = b5.select('a[b10^="http"]')
        for link in b9:
            if link.has_attr('b10'):
                b10 = link.attrs['b10']
                print(b10)
                try:
                    b11 = urllib.request.urlopen(b10)
                    b12 = b11.read()
                    print(b12)
                    b13 = {
                        "link": b10,
                        "content": fonk2(b12)
                    }
                    b14 = b4.mytable.insert_one(b13)
                    print(b14)
                    print(b4.list_collection_names())
                except HTTPError as e:
                    continue
                print("")
                print(fonk2(b12))
    except Exception as e:
        print("Error:", e)
if b15 = = "__main__":
    b16 = 'http:
    fonk3(b16)