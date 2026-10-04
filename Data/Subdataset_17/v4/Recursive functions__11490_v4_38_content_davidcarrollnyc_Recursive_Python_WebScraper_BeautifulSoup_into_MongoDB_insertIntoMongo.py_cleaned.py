import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup, Comment
from pymongo import MongoClient
client = MongoClient("mongodb:
db_name = 'heroku_XXXXX'
mydb = client[db_name]
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
def fetch_and_store_url_content(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        content = text_from_html(html)
        record = {
            "link": url,
            "content": content
        }
        record_id = mydb.mytable.insert_one(record).inserted_id
        print(f"Record inserted with ID: {record_id}")
        print(f"Collections in the database: {mydb.list_collection_names()}")
        print(content)
    except HTTPError as e:
        print(f"Failed to fetch URL: {url} with error: {e}")
def main():
    url = 'http:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select('a[href^="http"]')
    for link in links:
        href = link.get('href')
        if href:
            print(href)
            fetch_and_store_url_content(href)
if __name__ == '__main__':
    main()