from bs4 import BeautifulSoup, Comment
import urllib.request
from pymongo import MongoClient
from urllib.error import HTTPError
MONGO_URL = "mongodb:
DB_NAME = 'HTML_content'
client = MongoClient(MONGO_URL)
db = client['heroku_XXXXX']
def is_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def extract_visible_text(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(is_visible, texts)
    return " ".join(t.strip() for t in visible_texts)
def scrape_and_save(url):
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select('a[href^="http"]')
        for link in links:
            if link.has_attr('href'):
                href = link.attrs['href']
                print(href)
                try:
                    response = urllib.request.urlopen(href)
                    html_content = response.read()
                    print(html_content)
                    record = {
                        "link": href,
                        "content": extract_visible_text(html_content)
                    }
                    record_id = db.mytable.insert_one(record)
                    print(record_id)
                    print(db.list_collection_names())
                except HTTPError as e:
                    continue
                print("")
                print(extract_visible_text(html_content))
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    url = 'http:
    scrape_and_save(url)