from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.error import HTTPError
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
    return " ".join(t.strip() for t in visible_texts)
def fetch_html(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except HTTPError as e:
        print(f"HTTP Error: {e.code} for URL: {url}")
        return None
def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    return [link.attrs['href'] for link in soup.select('a[href^="http"]') if link.has_attr('href')]
def process_url(url):
    html = fetch_html(url)
    if html:
        print(text_from_html(html))
        links = extract_links(html)
        for link in links:
            print(link)
            process_url(link)
def main():
    url = 'http:
    process_url(url)
if __name__ == "__main__":
    main()