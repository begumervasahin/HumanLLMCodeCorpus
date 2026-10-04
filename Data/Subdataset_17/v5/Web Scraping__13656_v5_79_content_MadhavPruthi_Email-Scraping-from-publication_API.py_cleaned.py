import re
import urllib.parse
import subprocess
from crossref.restful import Works
from bs4 import BeautifulSoup
import requests
from MainApp.models import EmailInfo
import scholar
import metainfoscrapper
works = Works()
def get_doi_by_title(title):
    search_url = f"https:
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    doi_links = soup.find_all(href=re.compile("https:
    if doi_links:
        match = re.search(r"https?:
        if match:
            return match.group(1)
    return None
def get_citations(title):
    command = f'python scholar.py -c 1 -A "{title}"'
    try:
        result = subprocess.check_output(command, shell=True).decode('windows-1252')
    except subprocess.CalledProcessError:
        print("Result fetching Error! IP blocking!")
        return None
    citation_urls = [url for url in result.split() if url.startswith('http:
    if not citation_urls:
        return None
    main_url = citation_urls[0]
    i = 0
    while True:
        paginated_url = re.sub(r'(\?.*)', f'?start={i}&\\1', main_url)
        response = requests.get(paginated_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        citation_list = soup.find_all('h3', class_='gs_rt')
        if not citation_list:
            break
        for paper in citation_list:
            name = paper.get_text()
            if name.startswith('['):
                name = name.split(' ', 1)[1]
            doi = get_doi_by_title(name)
            if doi:
                email = metainfoscrapper.getEmail(doi)
        i += 10
def main_search(doi):
    title = works.doi(doi)['title']
    return get_citations(title)
