from bs4 import BeautifulSoup, Comment
import urllib.request
from urllib.error import HTTPError
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def extract_visible_text(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)
def fetch_html_content(url):
    try:
        html = urllib.request.urlopen(url).read()
        return html
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        return None
def print_links_with_content_and_visible_text(html):
    soup = BeautifulSoup(html, "html.parser")
    possible_links = soup.select('a[href^="http"]')
    for link in possible_links:
        if link.has_attr('href'):
            link_href = link.attrs['href']
            print(link_href)
            check_for_200 = urllib.request.urlopen(link_href)
            html2 = check_for_200.read()
            print(html2)
            print("")
            print(extract_visible_text(html2))
def main():
    url = 'http:
    html = fetch_html_content(url)
    if html:
        visible_text = extract_visible_text(html)
        print(visible_text)
        print_links_with_content_and_visible_text(html)
if __name__ == "__main__":
    main()