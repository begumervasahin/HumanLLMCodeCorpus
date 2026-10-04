from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.error import HTTPError
from pymongo import MongoClient
b1 = MongoClient("mongodb:
b2 = b1['heroku_XXXXX']
b3 = 'HTML_content'
def fonk1(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b4 = BeautifulSoup(body, 'b8.parser')
    b5 = b4.findAll(text=True)
    b6 = filter(tag_visible, b5)
    return u" ".join(t.strip() for t in b6)
def fonk3():
    b7 = 'http:
    b8 = urllib.request.urlopen(b7).read()
    b9 = BeautifulSoup(b8, "b8.parser")
    b10 = b9.select('a[href^="http"]')
    for link in b10:
        if link.has_attr('href'):
            print(link.attrs['href'])
            try:
                b11 = urllib.request.urlopen(link.attrs['href'])
                b12 = b11.read()
                print(b12)
                b13 = {
                    "link": link.attrs['href'],
                    "content": fonk2(b12)
                }
                b14 = b2.HTML_content.insert_one(b13).inserted_id
                print(f"Inserted record ID: {b14}")
                print(f"Collections: {b2.list_collection_names()}")
            except HTTPError as e:
                continue
            print("")
            print(fonk2(b12))
if b15 = = "__main__":
    fonk3()