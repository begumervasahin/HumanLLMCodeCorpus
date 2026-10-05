import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup
from crossref.restful import Works
import metainfoscrapper
works_api = Works()
def search_crossref_by_title(title):
    query_params = {"q": title}
    search_url = "https:
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    doi_links = soup.find_all(href=re.compile("https:
    match = re.search("(?P<url>https?:
    if match is not None:
        return match.group(0)[16:-2]
    return None
def get_citations(title):
    command = "python scholar.py -c 1 -A \"" + str(title[0]) + "\""
    result = subprocess.check_output(command, shell=True)
    if str(result) == "'b'":
        print("Error fetching results! IP might be blocked!")
        return None
    decoded_result = result.decode('windows-1252')
    citation_urls = [url.strip() for url in decoded_result.split() if url.startswith('http:
    for citation_url in citation_urls:
        i = 0
        while True:
            url_parts = citation_url.split('?')
            url_parts.insert(1, "?start=" + str(i) + "&")
            url = ''.join(url_parts)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            citation_list = soup.find_all('h3', class_='gs_rt')
            if not citation_list:
                break
            for paper in citation_list:
                paper_title = paper.get_text()
                if paper_title[0] == '[':
                    paper_title = paper_title.split(' ', 1)[1]
                doi = search_crossref_by_title(paper_title)
                email = metainfoscrapper.getEmail(doi)
            i += 10
def main_search(doi):
    paper_title = works_api.doi(doi)['title']
    return get_citations(paper_title)