from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.error import HTTPError
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
def main():
    url = 'http:
    try:
        html = urllib.request.urlopen(url).read()
    except HTTPError as e:
        print(f"Error fetching {url}: {e}")
        return
    bs = BeautifulSoup(html, "html.parser")
    possible_links = bs.select('a[href^="http"]')
    for link in possible_links:
        if link.has_attr('href'):
            href = link.attrs['href']
            print(href)
            try:
                response = urllib.request.urlopen(href)
                html2 = response.read()
                content = text_from_html(html2)
                print(content)
                myrecord = {
                    "link": href,
                    "content": content
                }
                record_id = mydb[collection_name].insert_one(myrecord).inserted_id
                print(f"Inserted record ID: {record_id}")
            except HTTPError as e:
                print(f"Error fetching {href}: {e}")
                continue
            print("")
if __name__ == "__main__":
    main()