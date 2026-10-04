import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup, Comment
from pymongo import MongoClient
MONGO_URI = "mongodb:
DB_NAME = 'heroku_XXXXX'
COLLECTION_NAME = 'mytable'
client = MongoClient(MONGO_URI)
mydb = client[DB_NAME]
def tag_visible(element):
    invisible_tags = {'style', 'script', 'head', 'title', 'meta', '[document]'}
    return not (element.parent.name in invisible_tags or isinstance(element, Comment))
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)
def fetch_and_store_url_content(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        content = text_from_html(html)
        record = {
            "link": url,
            "content": content
        }
        record_id = mydb[COLLECTION_NAME].insert_one(record).inserted_id
        print(f"Record inserted with ID: {record_id}")
        print(f"Collections in the database: {mydb.list_collection_names()}")
        print(content)
    except HTTPError as e:
        print(f"Failed to fetch URL: {url} with error: {e}")
def main():
    nytimes_url = 'http:
    try:
        html = urllib.request.urlopen(nytimes_url).read()
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select('a[href^="http"]')
        for link in links:
            href = link.get('href')
            if href:
                print(href)
                fetch_and_store_url_content(href)
    except HTTPError as e:
        print(f"Failed to fetch NYTimes homepage with error: {e}")
if __name__ == '__main__':
    main()