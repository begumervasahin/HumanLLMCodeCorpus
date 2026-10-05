import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def get_playstore_link(company_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
    }
    response = requests.get(company_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.select("a"):
        href = link.get("href", "")
        if "play.google.com" in href:
            return href
    return 'NULL'
def scrape_organization(org_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    response = requests.get(org_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    keys = [elem.text for elem in soup.select("CSS_SELECTOR_FOR_INFO")]
    values = [elem.text.strip() for elem in soup.select("CSS_SELECTOR_FOR_VALUE")]
    info = dict(zip(keys, values))
    if 'Website' in info:
        info['Playstore Link'] = get_playstore_link("http:
    else:
        info['Playstore Link'] = 'NULL'
    return info
def main():
    list_of_urls = []
    list_of_info = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        list_of_info = list(executor.map(scrape_organization, list_of_urls))
    if list_of_info:
        max_keys = max(list_of_info, key=lambda x: len(x.keys())).keys()
        with open('info.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=max_keys)
            writer.writeheader()
            for dictionary in list_of_info:
                writer.writerow({key: dictionary.get(key, "NULL") for key in max_keys})
if __name__ == "__main__":
    main()