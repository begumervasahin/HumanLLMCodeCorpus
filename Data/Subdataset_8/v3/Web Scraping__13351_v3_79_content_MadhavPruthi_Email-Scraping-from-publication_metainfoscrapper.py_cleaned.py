import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
from selenium import webdriver
import time
EMAIL_REGEX = re.compile(r"([a-z0-9!{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                         r"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
def get_proxies():
    url = 'https:
    response = requests.get(url)
    parser = BeautifulSoup(response.text, 'html.parser')
    proxies = set()
    for row in parser.select('tbody tr')[:10]:
        ip = row.select_one('td:nth-of-type(1)').text
        port = row.select_one('td:nth-of-type(2)').text
        proxy = f"{ip}:{port}"
        proxies.add(proxy)
    return proxies
def download_pdf(link, download_folder, path_to_chrome_driver):
    options = webdriver.ChromeOptions()
    profile = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.default_directory": download_folder,
        "download.extensions_to_open": ""
    }
    options.add_experimental_option("prefs", profile)
    driver = webdriver.Chrome(path_to_chrome_driver, chrome_options=options)
    driver.get(link)
    time.sleep(10)
    driver.close()
def extract_emails_from_pdf(contents):
    matching_text = ''.join(contents)
    email_matches = EMAIL_REGEX.findall(matching_text)
    emails = ''.join(email for email in email_matches)
    return emails
def get_email(event_doi):
    doi_url = f'https:
    email = ''
    try:
        response = requests.get(doi_url)
        soup = BeautifulSoup(response.text, 'lxml')
        mailto_links = soup.find_all(href=re.compile("mailto"))
        for link in mailto_links:
            email = link.string
        if not email:
            email_matches = EMAIL_REGEX.findall(str(mailto_links[0]))
            if email_matches:
                email = next(email[0] for email in email_matches if not email[0].startswith('
    except Exception as e:
        print("Exception in getEmail: ", e)
    if not email:
        email = get_email_third_party(event_doi)
    return email
def get_email_third_party(doi):
    print("Trying Unpaywall..")
    email = unpaywall(doi)
    if not email:
        print("Trying Libgen..")
        email = libgen(doi)
        if not email:
            print("Trying Scihub..")
            email = scihub(doi)
    return email
if __name__ == "__main__":
    event_doi = "YOUR_EVENT_DOI"
    total_citations = get_total_citations("YOUR_TITLE")
    print("Total Citations:", total_citations)
    journal_ISSN = "YOUR_JOURNAL_ISSN"
    total_citations_journal = get_total_citations_for_journal(journal_ISSN)
    print("Total Citations for Journal:", total_citations_journal)