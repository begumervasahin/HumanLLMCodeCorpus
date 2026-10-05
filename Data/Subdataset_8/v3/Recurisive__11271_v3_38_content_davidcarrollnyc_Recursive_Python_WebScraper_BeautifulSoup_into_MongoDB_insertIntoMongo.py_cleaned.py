from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
MONGODB_URI = "mongodb:
client = MongoClient(MONGODB_URI)
database = client['heroku_XXXXX']
collection = database['mytable']
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
def fetch_and_store_content(url):
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        possible_links = soup.select('a[href^="http"]')
        for link in possible_links:
            if link.has_attr('href'):
                print(link.attrs['href'])
                try:
                    check_for_200 = urllib.request.urlopen(link.attrs['href'])
                    html2 = check_for_200.read()
                    content = text_from_html(html2)
                    record = {"link": link.attrs['href'], "content": content}
                    inserted_id = collection.insert_one(record).inserted_id
                    print("Record inserted with ID:", inserted_id)
                    print("Collection names:", database.list_collection_names())
                    print("")
                    print(content)
                except HTTPError:
                    continue
    except HTTPError as e:
        print("Error accessing URL:", e)
if __name__ == '__main__':
    main_url = 'http:
    fetch_and_store_content(main_url)