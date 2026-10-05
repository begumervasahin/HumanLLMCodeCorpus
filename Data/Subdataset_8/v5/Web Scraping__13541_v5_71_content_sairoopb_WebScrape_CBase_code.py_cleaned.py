import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def extract_play_store_link(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all("a"):
        href = link.get("href", "")
        if "play.google.com" in href:
            return href
    return 'NULL'
def scrape_organization_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    org_name_elem = soup.select_one(".component--field-formatter.field-type-identifier-multi.word-break-all.mb1")
    org_name = org_name_elem.text.strip() if org_name_elem else 'NULL'
    info = {'Organisation name': org_name}
    for key_elem, value_elem in zip(soup.select(".entity-info-container .text_component-label"), soup.select(".entity-info-container .value")):
        key = key_elem.text.replace(u'\xa0', u'')
        value = value_elem.text.strip()
        info[key] = value
    info['Playstore Link'] = extract_play_store_link("http:
    return info
list_of_urls = [...]
list_of_info = []
with ThreadPoolExecutor(max_workers=10) as executor:
    list_of_info = list(executor.map(scrape_organization_info, list_of_urls))
max_keys = max(list_of_info, key=len).keys()
with open('info.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=max_keys)
    writer.writeheader()
    for info in list_of_info:
        writer.writerow(info)