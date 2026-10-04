import requests
from bs4 import BeautifulSoup
import re
import time
def get_first_valid_link(soup):
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    for paragraph in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for tag in paragraph.find_all(class_=excluded_classes):
            tag.extract()
        for tag in paragraph.find_all(id=excluded_ids):
            tag.extract()
        paragraph_text = re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph))
        paragraph = BeautifulSoup(paragraph_text, 'lxml')
        for italic in paragraph.find_all('i'):
            italic.extract()
        link = paragraph.find('a', href=True)
        if link:
            return link['href']
    return None
def get_to_philosophy(url, visited_urls=None):
    if visited_urls is None:
        visited_urls = []
    visited_urls.append(url)
    time.sleep(0.5)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    link_suffix = get_first_valid_link(soup)
    if not link_suffix:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    next_link = "https:
    print(next_link)
    if next_link == "https:
        print("Philosophy page found, just as expected!")
        return next_link
    elif next_link in visited_urls:
        print("Stuck in a loop!")
        return next_link
    else:
        return get_to_philosophy(next_link, visited_urls)
if __name__ == "__main__":
    random_url = "https:
    get_to_philosophy(random_url)