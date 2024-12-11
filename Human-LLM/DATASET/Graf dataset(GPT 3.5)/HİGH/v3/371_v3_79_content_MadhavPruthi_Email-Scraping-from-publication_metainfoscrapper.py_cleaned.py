import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
from selenium import webdriver
import time
b1 = re.compile(r"([a-z0-9!{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                         r"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
def fonk1():
    b2 = 'https:
    b3 = requests.get(b2)
    b4 = BeautifulSoup(b3.text, 'html.b4')
    b5 = set()
    for row in b4.select('tbody tr')[:10]:
        b6 = row.select_one('td:nth-of-type(1)').text
        b7 = row.select_one('td:nth-of-type(2)').text
        b8 = f"{b6}:{b7}"
        b5.add(b8)
    return b5
def fonk2(link, download_folder, path_to_chrome_driver):
    b9 = webdriver.ChromeOptions()
    b10 = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.default_directory": download_folder,
        "download.extensions_to_open": ""
    }
    b9.add_experimental_option("prefs", b10)
    b11 = webdriver.Chrome(path_to_chrome_driver, chrome_options=b9)
    b11.get(link)
    time.sleep(10)
    b11.close()
def fonk3(contents):
    b12 = ''.join(contents)
    b13 = b1.findall(b12)
    b14 = ''.join(b16 for b16 in b13)
    return b14
def fonk4(b20):
    b15 = f'https:
    b16 = ''
    try:
        b3 = requests.get(b15)
        b17 = BeautifulSoup(b3.text, 'lxml')
        b18 = b17.find_all(href=re.compile("mailto"))
        for link in b18:
            b16 = link.string
        if not b16:
            b13 = b1.findall(str(b18[0]))
            if b13:
                b16 = next(b16[0] for b16 in b13 if not b16[0].startswith('
    except Exception as e:
        print("Exception in getEmail: ", e)
    if not b16:
        b16 = fonk5(b20)
    return b16
def fonk5(doi):
    print("Trying Unpaywall..")
    b16 = unpaywall(doi)
    if not b16:
        print("Trying Libgen..")
        b16 = libgen(doi)
        if not b16:
            print("Trying Scihub..")
            b16 = scihub(doi)
    return b16
if b19 = = "__main__":
    b20 = "YOUR_EVENT_DOI"
    b21 = get_total_citations("YOUR_TITLE")
    print("Total Citations:", b21)
    b22 = "YOUR_JOURNAL_ISSN"
    b23 = get_total_citations_for_journal(b22)
    print("Total Citations for Journal:", b23)