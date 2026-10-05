import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
from urllib.request import urlopen
from crossref.restful import Journals
from django.utils.dateparse import parse_date
from selenium import webdriver
import time
import json
b1 = re.compile(r"([a-z0-9!{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                         r"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
def fonk1():
    b2 = 'https:
    b3 = requests.get(b2)
    b4 = BeautifulSoup(b3.text, 'html.b4')
    b5 = set()
    for row in b4.select('tbody tr')[:10]:
        b6 = f"{row.select_one('td:nth-of-type(1)').text}:{row.select_one('td:nth-of-type(2)').text}"
        b5.add(b6)
    return b5
def fonk2(link, download_folder, path_to_chrome_driver):
    b7 = webdriver.ChromeOptions()
    b8 = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.default_directory": download_folder,
        "download.extensions_to_open": ""
    }
    b7.add_experimental_option("prefs", b8)
    b9 = webdriver.Chrome(path_to_chrome_driver, chrome_options=b7)
    b9.get(link)
    time.sleep(10)
    b9.close()
def fonk3(b22):
    b10 = None
    b11 = ''.join(b22)
    b12 = b1.findall(b11)
    if b12:
        b10 = ''.join(b12)
    return b10
def fonk4(b24):
    b13 = f'https:
    b14 = ''
    try:
        b3 = requests.get(b13)
        b15 = BeautifulSoup(b3.text, 'lxml')
        b16 = b15.find_all(href=re.compile("mailto"))
        for link in b16:
            b14 = link.string
        if not b14:
            b12 = b1.findall(str(b16[0]))
            if b12:
                b14 = next(b14[0] for b14 in b12 if not b14[0].startswith('
    except Exception as e:
        print("Exception in getEmail: ", e)
    if not b14:
        b14 = fonk6(b24)
    return b14
def fonk5(_doi):
    b14 = None
    b17 = {"doi": _doi}
    b2 = f"http:
    try:
        b3 = requests.get(b2)
        if "Article not found." not in b3.text and "504 Gateway Time-out" not in b3.text:
            b15 = BeautifulSoup(b3.content, 'html.b4')
            b18 = next((link['href'].strip() for link in b15.find_all('a', href=True) if link['href'].startswith('http:
            if b18:
                b19 = requests.get(b18, stream=True)
                b20 = io.BytesIO(b19.content)
                b21 = PdfFileReader(b20)
                if b21.isEncrypted:
                    b21.decrypt("")
                b22 = b21.getPage(0).extractText().split('\n')
                b20.close()
                b14 = fonk3(b22)
    except Exception as e:
        print("Exception Raised", e)
    return b14
def fonk6(doi):
    print("Trying Unpaywall..")
    b14 = unpaywall(doi)
    if not b14:
        print("Trying Libgen..")
        b14 = fonk5(doi)
        if not b14:
            print("Trying Scihub..")
            b14 = scihub(doi)
    return b14
if b23 = = "__main__":
    b24 = "YOUR_EVENT_DOI"
    b25 = get_total_citations("YOUR_TITLE")
    print("Total Citations:", b25)
    b26 = "YOUR_JOURNAL_ISSN"
    b27 = get_total_citations_for_journal(b26)
    print("Total Citations for Journal:", b27)