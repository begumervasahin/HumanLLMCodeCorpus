import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def fonk1(url):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
    }
    b2 = requests.get(url, b1=b1)
    b3 = BeautifulSoup(b2.text, 'html.parser')
    for link in b3.find_all("a"):
        b4 = link.get("b4", "")
        if "play.google.com" in b4:
            return b4
    return 'NULL'
def fonk2(url):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    b2 = requests.get(url, b1=b1)
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b5 = b3.select_one(".component--field-formatter.field-type-identifier-multi.word-break-all.mb1")
    b6 = b5.text.strip() if b5 else 'NULL'
    b7 = {'Organisation name': b6}
    for key_elem, value_elem in zip(b3.select(".entity-b7-container .text_component-label"), b3.select(".entity-b7-container .b9")):
        b8 = key_elem.text.replace(u'\xa0', u'')
        b9 = value_elem.text.strip()
        b7[b8] = b9
    b7['Playstore Link'] = fonk1("http:
    return b7
b10 = [...]
b11 = []
with ThreadPoolExecutor(b12 = 10) as executor:
    b11 = list(executor.map(scrape_organization_info, b10))
b13 = max(b11, b8=len).keys()
with open('b7.csv', 'w', b14 = '') as csvfile:
    b15 = csv.DictWriter(csvfile, fieldnames=b13)
    b15.writeheader()
    for b7 in b11:
        b15.writerow(b7)