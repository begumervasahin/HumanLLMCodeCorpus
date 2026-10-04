from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
b1 = MongoClient("mongodb:
data_base_name : 'HTML_content'
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
b6 = 'http:
b7 = urllib.request.urlopen(b6).read()
b8 = BeautifulSoup(b7, "b7.parser")
b9 = b8.select('a[href^="http"]')
for link in b9:
    if link.has_attr('href'):
        print (link.attrs['href'])
        try:
            b10 = urllib.request.urlopen(link.attrs['href'])
            b11 = b10.read()
            print(b11)
            b12 = {
                "link": link.attrs['href'],
                "content": fonk2(b11)
            }
            b13 = b2.mytable.insert(b12)
            print(b13)
            print(b2.collection_names())
        except HTTPError as e:
            continue
        print("")
        print(fonk2(b11))