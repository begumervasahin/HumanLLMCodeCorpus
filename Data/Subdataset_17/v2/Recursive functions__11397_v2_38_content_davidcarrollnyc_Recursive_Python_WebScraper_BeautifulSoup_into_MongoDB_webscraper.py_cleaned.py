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
    return u" ".join(t.strip() for t in visible_texts)
def fetch_html(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except HTTPError as e:
        print(f"HTTP Error for {url}: {e}")
        return None
def print_links_and_text(html):
    soup = BeautifulSoup(html, "html.parser")
    possible_links = soup.select('a[href^="http"]')
    for link in possible_links:
        if link.has_attr('href'):
            href = link.attrs['href']
            print(href)
            linked_html = fetch_html(href)
            if linked_html:
                print(text_from_html(linked_html))
            print("")
def main():
    url = 'http:
    html = fetch_html(url)
    if html:
        print(text_from_html(html))
        print_links_and_text(html)
if __name__ == "__main__":
    main()