import requests
from bs4 import BeautifulSoup
import regex
import time
def get_to_philosophy(url, cache=[]):
    cache.append(url)
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA',
                        'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]
    time.sleep(0.5)
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt, 'lxml')
    no_wikilinks = True
    for p in soup.find(class_='mw-parser-output').find_all('p', recursive=False):
        for c in p.find_all(class_=excluded_classes):
            c.extract()
        for i in p.find_all(id=excluded_ids):
            i.extract()
        p = BeautifulSoup(regex.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))',
                                    '', str(p)), features="lxml")
        for italic in p.find_all('i'):
            italic.extract()
        try:
            link_suffix = p.a.get('href')
        except:
            continue
        no_wikilinks = False
        break
    if(no_wikilinks):
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        link = "https:
        print(link)
    if(link == "https:
        print("Wikosopher found it, Just as expected !")
        return link
    elif(link in cache):
        print("Stuck in a loop !")
        return link
    else:
        return(get_to_philosophy(link, cache))
random_url = "https:
get_to_philosophy(random_url)