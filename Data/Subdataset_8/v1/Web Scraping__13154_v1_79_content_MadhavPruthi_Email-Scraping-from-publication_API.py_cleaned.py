import re
import urllib.parse
import subprocess
from bs4 import BeautifulSoup
import requests
from crossref.restful import Works
import metainfoscrapper
citation_urls = []
works = Works()
def GetDoiByTitle(title):
    args = {"q": title}
    url = "https:
    url_page = requests.get(url)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    links = soup.find_all(href=re.compile("https:
    match = re.search("(?P<url>https?:
    if match is not None:
        return match.group(0)[16:-1]
    return None
def get_citations(title):
    command = f"python scholar.py -c 1 -A \"{title}\""
    result = subprocess.check_output(command, shell=True)
    if str(result) == "'b'":
        print("Result fetching Error! IP blocking!")
        return None
    a = result.decode('windows-1252')
    strings = a.split(" ")
    for string in strings:
        if string.startswith('http:
            string = string.strip()
            citation_urls.append(string)
    main_url = citation_urls[0]
    i = 0
    while True:
        url = main_url.split('?')
        url.insert(1, "?start=" + str(i) + "&")
        url = ''.join(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        citation_list = soup.find_all('h3', class_='gs_rt')
        if not citation_list:
            break
        for paper in citation_list:
            name = paper.get_text()
            if name[0] == '[':
                name = name.split(' ', 1)[1]
            _doi = GetDoiByTitle(name)
            email = metainfoscrapper.getEmail(_doi)
        i += 10
def mainSearch(_doi):
    return get_citations(works.doi(_doi)['title'])
