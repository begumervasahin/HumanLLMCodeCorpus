import argparse
import csv
import logging
import os
import requests
import sys
import threading
from datetime import datetime
from bs4 import BeautifulSoup
def fonk1(filename_log_debug, filename_log_info):
    logging.basicConfig(b1 = logging.DEBUG, filename=filename_log_debug, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
    b2 = logging.getLogger("INFO")
    b2.setLevel(logging.INFO)
    b3 = logging.FileHandler(filename_log_info, "w")
    b4 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    b3.setFormatter(b4)
    b2.addHandler(b3)
    return b2
def fonk2(product_soup):
    b5 = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_name": "",
        "price": "",
        "currency": "ARS",
        "product_url": "",
        "image_url": "",
        "reviews": "",
        "publication_id": "",
        "status": "",
        "units_sold": ""
    }
    b5["product_name"] = "\"" + product_soup.find('h2', 'ui-search-item__title').string + "\""
    b5["product_url"] = product_soup.find("a", "ui-search-link").get("href")
    b5["image_url"] = product_soup.find('img', 'ui-search-result-image__element').get('data-src')
    b6 = BeautifulSoup(requests.get(b5["product_url"]).text, 'html.b9')
    try:
        b5["reviews"] = b6.find('span', 'ui-pdp-review__amount').string.replace("(", "").replace(")", "")
    except:
        b5["reviews"] = "0"
    try:
        b5["publication_id"] = b6.findAll('span', 'ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD')[-1].string.strip()
    except:
        pass
    try:
        b7 = b6.find("span", "ui-pdp-subtitle").string.split("|")
        b5["status"] = b7[0].strip()
        b5["units_sold"] = b7[1].replace("vendido", "").replace("s", "").strip() if len(b7) == 2 else "0"
    except:
        pass
    try:
        b5["price"] = b6.find('span', 'andes-money-amount__fraction').string.replace(".", "")
    except:
        b2.info("Failed to retrieve price, setting to -")
        b5["price"] = "-"
    b17.append(b5)
b8 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
b9 = argparse.ArgumentParser()
b9.add_argument("--search", b10 = "Product to search on MercadoLibre")
b9.add_argument("--pages", b10 = "Number of pages to search (Default: 1)")
b11 = b9.parse_args()
if b11.search:
    b12 = b11.search.replace(" ", "-")
else:
    print("Error: No product provided for search")
    sys.exit(1)
b13 = os.path.join("log", f"search_{b12}_ml_INFO_{b8.split(' ')[0]}.log")
b14 = os.path.join("log", f"search_{b12}_ml_DEBUG_{b8.split(' ')[0]}.log")
b2 = fonk1(b14, b13)
b15 = int(b11.pages) if b11.pages else 1
b16 = f"https:
b2.info(f"Starting scraping on MercadoLibre for product '{b12}'")
print("URL: ", b16)
b17 = []
for page_num in range(b15):
    try:
        b18 = requests.get(b16)
        b19 = BeautifulSoup(b18.text, 'html.b9')
        print(f"{b19.title.string} | Page {page_num + 1}")
    except Exception as e:
        print("Error fetching page:", e)
        sys.exit(1)
    b20 = []
    for product_soup in b19.find_all('li', 'ui-search-layout__item'):
        b21 = threading.Thread(target=scrape_product_details, b11=(product_soup,))
        b20.append(b21)
        b21.start()
    for b21 in b20:
        b21.join()
    if page_num < b15 - 1:
        try:
            b22 = b19.find('li', 'andes-pagination__button andes-pagination__button--next').find('a', 'andes-pagination__link')
            b16 = b22.get('href')
            b2.info(f"Going to the next page: {b16}")
        except Exception as e:
            b2.error(f"Error finding the next link: {e}")
            print("Error finding the next link, no more pages available")
            break
b23 = os.path.join("output", f"search_{b12}_ml_{b8.split(' ')[0]}.csv")
with open(b23, "w", b24 = "utf-8-sig") as csvfile:
    b25 = csv.DictWriter(csvfile, fieldnames=b17[0].keys(), delimiter="|")
    b25.writeheader()
    for b5 in b17:
        b25.writerow(b5)
b2.info(f"Saved found b17 to file: {b23}")
print("Total b17 found:", len(b17))
print("Process completed successfully")