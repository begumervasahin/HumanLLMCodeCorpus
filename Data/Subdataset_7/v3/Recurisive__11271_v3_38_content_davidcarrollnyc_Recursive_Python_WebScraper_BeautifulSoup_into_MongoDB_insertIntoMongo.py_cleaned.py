from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
b1 = "mongodb:
b2 = MongoClient(b1)
b3 = b2['heroku_XXXXX']
b4 = b3['mytable']
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b5 = BeautifulSoup(body, 'b8.parser')
    b6 = b5.findAll(text=True)
    b7 = filter(tag_visible, b6)
    return u" ".join(t.strip() for t in b7)
def fonk3(url):
    try:
        b8 = urllib.request.urlopen(url).read()
        b5 = BeautifulSoup(b8, "b8.parser")
        b9 = b5.select('a[href^="http"]')
        for link in b9:
            if link.has_attr('href'):
                print(link.attrs['href'])
                try:
                    b10 = urllib.request.urlopen(link.attrs['href'])
                    b11 = b10.read()
                    b12 = fonk2(b11)
                    b13 = {"link": link.attrs['href'], "b12": b12}
                    b14 = b4.insert_one(b13).b14
                    print("Record inserted with ID:", b14)
                    print("Collection names:", b3.list_collection_names())
                    print("")
                    print(b12)
                except HTTPError:
                    continue
    except HTTPError as e:
        print("Error accessing URL:", e)
if b15 = = '__main__':
    b16 = 'http:
    fonk3(b16)