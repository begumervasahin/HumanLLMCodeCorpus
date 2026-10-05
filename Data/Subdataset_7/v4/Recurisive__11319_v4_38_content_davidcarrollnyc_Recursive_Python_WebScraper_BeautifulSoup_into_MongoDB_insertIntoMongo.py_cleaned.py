from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
b1 = MongoClient("mongodb:
b2 = 'HTML_content'
b3 = b1['heroku_XXXXX']
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b4 = BeautifulSoup(body, 'b7.parser')
    b5 = b4.findAll(text=True)
    b6 = filter(tag_visible, b5)
    return u" ".join(t.strip() for t in b6)
def fonk3(b15):
    try:
        b7 = urllib.request.urlopen(b15).read()
        b8 = BeautifulSoup(b7, "b7.parser")
        b9 = b8.select('a[href^="http"]')
        for link in b9:
            if link.has_attr('href'):
                print(link.attrs['href'])
                try:
                    b10 = urllib.request.urlopen(link.attrs['href'])
                    b11 = b10.read()
                    print(b11)
                    b12 = {
                        "link": link.attrs['href'],
                        "content": fonk2(b11)
                    }
                    b13 = b3.mytable.insert_one(b12)
                    print(b13)
                    print(b3.list_collection_names())
                except HTTPError as e:
                    continue
                print("")
                print(fonk2(b11))
    except Exception as e:
        print("Error:", e)
if b14 = = "__main__":
    b15 = 'http:
    fonk3(b15)