import requests
from bs4 import BeautifulSoup
import regex as re
import time
def get_to_philosophy(url, cache=None):
    if cache is None:
        cache = []
    cache.append(url)
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    time.sleep(0.5)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    no_wikilinks = True
    for paragraph in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for cls in excluded_classes:
            for element in paragraph.find_all(class_=cls):
                element.extract()
        for id_ in excluded_ids:
            for element in paragraph.find_all(id=id_):
                element.extract()
        cleaned_paragraph = re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph))
        cleaned_soup = BeautifulSoup(cleaned_paragraph, 'lxml')
        for italic in cleaned_soup.find_all('i'):
            italic.extract()
        first_link = cleaned_soup.find('a', href=True)
        if first_link:
            link_suffix = first_link['href']
            no_wikilinks = False
            break
    if no_wikilinks:
        print(f"No outgoing wikilinks in the article: {url[30:]}")
        return url
    link = "https:
    print(link)
    if link == "https:
        print("Philosophy page found!")
        return link
    elif link in cache:
        print("Stuck in a loop!")
        return link
    else:
        return get_to_philosophy(link, cache)
if __name__ == "__main__":
    random_url = "https:
    get_to_philosophy(random_url)