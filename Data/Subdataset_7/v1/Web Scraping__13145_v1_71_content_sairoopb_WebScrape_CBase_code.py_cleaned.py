import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def fonk1(comp_url):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
    }
    b2 = requests.get(comp_url, b1=b1)
    b3 = BeautifulSoup(b2.text, 'html.parser')
    for link in b3.select("a"):
        b4 = link.get("b4", "")
        if "play.google.com" in b4:
            return b4
    return 'NULL'
def fonk2(org_url):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    b2 = requests.get(org_url, b1=b1)
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b5 = [elem.text for elem in b3.select("CSS_SELECTOR_FOR_INFO")]
    b6 = [elem.text.strip() for elem in b3.select("CSS_SELECTOR_FOR_VALUE")]
    b7 = dict(zip(b5, b6))
    if 'Website' in b7:
        b7['Playstore Link'] = fonk1("http:
    else:
        b7['Playstore Link'] = 'NULL'
    return b7
def fonk3():
    b8 = []
    b9 = []
    with ThreadPoolExecutor(b10 = 10) as executor:
        b9 = list(executor.map(scrape_org, b8))
    if b9:
        b11 = max(b9, key=lambda x: len(x.b5())).b5()
        with open('b7.csv', 'w', b12 = '') as csvfile:
            b13 = csv.DictWriter(csvfile, fieldnames=b11)
            b13.writeheader()
            for dictionary in b9:
                b13.writerow({key: dictionary.get(key, "NULL") for key in b11})
if b14 = = "__main__":
    fonk3()