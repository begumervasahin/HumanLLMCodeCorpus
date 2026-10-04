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
        url = f"https:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        doi_link = soup.find(href=re.compile("https:
        if doi_link:
            match = re.search("(?P<url>https?:
            if match:
                return match.group("url")[16:-2]
    except requests.RequestException as e:
        print(f"Error fetching DOI: {e}")
    return None
def get_citations(title):
    try:
        command = f'python scholar.py -c 1 -A "{title}"'
        result = subprocess.check_output(command, shell=True)
        if not result:
            print("Result fetching Error! IP blocking!")
            return
        result_str = result.decode('windows-1252')
        citation_urls.extend(re.findall(r'http:
        if citation_urls:
            fetch_citation_details(citation_urls[0])
    except subprocess.CalledProcessError as e:
        print(f"Error fetching citations: {e}")
def fetch_citation_details(main_url):
    i = 0
    while True:
        try:
            url = f"{main_url}&start={i}"
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            citation_list = soup.find_all('h3', class_='gs_rt')
            if not citation_list:
                break
            for paper in citation_list:
                name = paper.get_text().split(' ', 1)[1] if paper.get_text().startswith('[') else paper.get_text()
                doi = get_doi_by_title(name)
                if doi:
                    email = metainfoscrapper.getEmail(doi)
        except requests.RequestException as e:
            print(f"Error fetching citation details: {e}")
        i += 10
def main_search(doi):
    try:
        title = works.doi(doi)['title']
        get_citations(title)
    except requests.RequestException as e:
        print(f"Error in main search: {e}")
if __name__ == "__main__":
    doi = "10.1038/nphys1170"
    main_search(doi)