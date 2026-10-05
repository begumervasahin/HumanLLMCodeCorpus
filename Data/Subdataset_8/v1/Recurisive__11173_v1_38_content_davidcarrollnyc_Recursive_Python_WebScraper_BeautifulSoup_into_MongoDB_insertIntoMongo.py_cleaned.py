from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
client = MongoClient("mongodb:
mydb = client['heroku_XXXXX']
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)
def main():
    url = 'http:
    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, "html.parser")
    possible_links = bs.select('a[href^="http"]')
    for link in possible_links:
        if link.has_attr('href'):
            print(link.attrs['href'])
            try:
                checkFor200 = urllib.request.urlopen(link.attrs['href'])
                html2 = checkFor200.read()
                content = text_from_html(html2)
                myrecord = {
                    "link": link.attrs['href'],
                    "content": content
                }
                record_id = mydb.mytable.insert_one(myrecord).inserted_id
                print("Record inserted with ID:", record_id)
                print("Collection names:", mydb.list_collection_names())
                print("")
                print(content)
            except HTTPError as e:
                continue
if __name__ == '__main__':
    main()