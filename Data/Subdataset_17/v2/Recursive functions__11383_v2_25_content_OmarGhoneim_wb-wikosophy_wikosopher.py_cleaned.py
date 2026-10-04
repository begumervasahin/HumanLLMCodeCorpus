import requests
from bs4 import BeautifulSoup
import re
import time
def get_to_philosophy(url, cache=[]):
    cache.append(url)
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    time.sleep(0.5)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    no_wikilinks = True
    for paragraph in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for tag in paragraph.find_all(class_=excluded_classes):
            tag.extract()
        for tag in paragraph.find_all(id=excluded_ids):
            tag.extract()
        paragraph = BeautifulSoup(re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph)), 'lxml')
        for italic in paragraph.find_all('i'):
            italic.extract()
        try:
            link_suffix = paragraph.a.get('href')
            no_wikilinks = False
            break
        except AttributeError:
            continue
    if no_wikilinks:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        link = "https:
        print(link)
    if link == "https:
        print("Philosophy page found, just as expected!")
        return link
    elif link in cache:
        print("Stuck in a loop!")
        return link
    else:
        return get_to_philosophy(link, cache)
if __name__ == "__main__":
    random_url = "https:
    get_to_philosophy(random_url)