import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup, Comment
from pymongo import MongoClient
client = MongoClient("mongodb:
mydb = client['heroku_XXXXX']
collection_name = 'HTML_content'
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
def fetch_html(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except HTTPError as e:
        print(f"Error fetching {url}: {e}")
        return None
def scrape_and_store_links(url):
    html = fetch_html(url)
    if html is None:
        return
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select('a[href^="http"]')
    for link in links:
        href = link.get('href')
        print(href)
        link_html = fetch_html(href)
        if link_html is None:
            continue
        content = text_from_html(link_html)
        print(content)
        record = {
            "link": href,
            "content": content
        }
        record_id = mydb[collection_name].insert_one(record).inserted_id
        print(f"Inserted record ID: {record_id}")
        print("")
def main():
    url = 'http:
    scrape_and_store_links(url)
if __name__ == "__main__":
    main()