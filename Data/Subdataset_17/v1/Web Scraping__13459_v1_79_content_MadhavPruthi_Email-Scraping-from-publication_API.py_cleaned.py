import re
import urllib.parse
import subprocess
import requests
from crossref.restful import Works
from bs4 import BeautifulSoup
from MainApp.models import EmailInfo
import metainfoscrapper
works = Works()
citation_urls = []
def get_doi_by_title(title):
    try:
        args = {"q": title}
        url = "https:
        url_page = requests.get(url)
        soup = BeautifulSoup(url_page.content, 'html.parser')
        list = soup.find_all(href=re.compile("https:
        if list:
            match = re.search("(?P<url>https?:
            if match:
                return match.group(0)[16:-2]
    except Exception as e:
        print(f"Error fetching DOI: {e}")
    return None
def get_citations(title):
    try:
        command = f"python scholar.py -c 1 -A \"{title}\""
        result = subprocess.check_output(command, shell=True)
        if not result:
            print("Result fetching Error! IP blocking!")
            return None
        result_str = result.decode('windows-1252')
        citation_urls.extend(re.findall(r'http:
        if citation_urls:
            fetch_citation_details(citation_urls[0])
    except Exception as e:
        print(f"Error fetching citations: {e}")
def fetch_citation_details(main_url):
    i = 0
    while True:
        try:
            url = f"{main_url}&start={i}"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            citation_list = soup.find_all('h3', class_='gs_rt')
            if not citation_list:
                break
            for paper in citation_list:
                name = paper.get_text().split(' ', 1)[1] if paper.get_text().startswith('[') else paper.get_text()
                _doi = get_doi_by_title(name)
                email = metainfoscrapper.getEmail(_doi)
        except Exception as e:
            print(f"Error fetching citation details: {e}")
        i += 10
def main_search(_doi):
    try:
        title = works.doi(_doi)['title']
        get_citations(title)
    except Exception as e:
        print(f"Error in main search: {e}")
if __name__ == "__main__":
    doi = "10.1038/nphys1170"
    main_search(doi)