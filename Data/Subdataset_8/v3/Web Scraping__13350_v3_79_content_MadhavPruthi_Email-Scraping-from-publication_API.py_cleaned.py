import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup
from crossref.restful import Works
import metainfoscrapper
citation_urls = []
works = Works()
def search_doi_by_title(title):
    search_params = {"q": title}
    search_url = "https:
    search_page = requests.get(search_url)
    soup = BeautifulSoup(search_page.content, 'html.parser')
    doi_links = soup.find_all(href=re.compile("https:
    if doi_links:
        doi_match = re.search("(?P<url>https?:
        if doi_match:
            return doi_match.group(0)[16:-1]
    return None
def fetch_citations(title):
    command = f"python scholar.py -c 1 -A \"{title}\""
    try:
        result = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        print("Error occurred while fetching results! IP might be blocked.")
        return None
    citation_urls.clear()
    decoded_result = result.decode('windows-1252')
    strings = decoded_result.split(" ")
    for string in strings:
        if string.startswith('http:
            citation_urls.append(string.strip())
    main_url = citation_urls[0] if citation_urls else None
    i = 0
    while main_url:
        url_parts = main_url.split('?')
        url = f"{url_parts[0]}?start={i}&{url_parts[1]}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        citation_list = soup.find_all('h3', class_='gs_rt')
        if not citation_list:
            break
        for paper in citation_list:
            paper_title = paper.get_text().split(' ', 1)[1] if paper.get_text()[0] == '[' else paper.get_text()
            doi = search_doi_by_title(paper_title)
            if doi:
                email = metainfoscrapper.getEmail(doi)
        i += 10
def main_search(doi):
    title = works.doi(doi)['title']
    fetch_citations(title)
