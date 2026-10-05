import requests
from bs4 import BeautifulSoup
import regex
import time
def get_to_philosophy(url, cache=[]):
    cache.append(url)
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    time.sleep(0.5)
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    no_wikilinks = True
    for paragraph in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for element in paragraph.find_all(class_=excluded_classes):
            element.extract()
        for element in paragraph.find_all(id=excluded_ids):
            element.extract()
        paragraph = BeautifulSoup(regex.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph)), features="lxml")
        for italic in paragraph.find_all('i'):
            italic.extract()
        try:
            link_suffix = paragraph.a.get('href')
        except:
            continue
        no_wikilinks = False
        break
    if no_wikilinks:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
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