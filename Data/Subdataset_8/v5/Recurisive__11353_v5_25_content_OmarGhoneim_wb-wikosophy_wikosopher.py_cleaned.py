import requests
from bs4 import BeautifulSoup
import re
import time
def fetch_webpage_content(url):
    time.sleep(0.5)
    response = requests.get(url)
    return response.text
def extract_valid_link(soup):
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    for paragraph in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for c in paragraph.find_all(class_=excluded_classes):
            c.extract()
        for i in paragraph.find_all(id=excluded_ids):
            i.extract()
        paragraph = BeautifulSoup(re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph)), features="lxml")
        for italic in paragraph.find_all('i'):
            italic.extract()
        link_suffix = paragraph.a.get('href', None)
        if link_suffix:
            return link_suffix
    return None
def get_to_philosophy(url, cache=[]):
    cache.append(url)
    webpage_content = fetch_webpage_content(url)
    soup = BeautifulSoup(webpage_content, 'lxml')
    link_suffix = extract_valid_link(soup)
    if link_suffix is None:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    link = "https:
    print(link)
    if link == "https:
        print("Wikosopher found it, Just as expected !")
        return link
    elif link in cache:
        print("Stuck in a loop !")
        return link
    else:
        return get_to_philosophy(link, cache)
random_url = "https:
get_to_philosophy(random_url)