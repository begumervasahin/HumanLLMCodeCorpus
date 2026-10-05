from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
b1 = MongoClient("mongodb:
b2 = b1['heroku_XXXXX']
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b3 = BeautifulSoup(body, 'b7.parser')
    b4 = b3.findAll(text=True)
    b5 = filter(tag_visible, b4)
    return u" ".join(t.strip() for t in b5)
def fonk3():
    b6 = 'http:
    b7 = urllib.request.urlopen(b6).read()
    b8 = BeautifulSoup(b7, "b7.parser")
    b9 = b8.select('a[href^="http"]')
    for link in b9:
        if link.has_attr('href'):
            print(link.attrs['href'])
            try:
                b10 = urllib.request.urlopen(link.attrs['href'])
                b11 = b10.read()
                b12 = fonk2(b11)
                b13 = {
                    "link": link.attrs['href'],
                    "b12": b12
                }
                b14 = b2.mytable.insert_one(b13).inserted_id
                print("Record inserted with ID:", b14)
                print("Collection names:", b2.list_collection_names())
                print("")
                print(b12)
            except HTTPError as e:
                continue
if b15 = = '__main__':
    fonk3()