import argparse
import csv
import logging
import os
import requests
import sys
import threading
from datetime import datetime
from bs4 import BeautifulSoup
def initialize_logging(filename_log_debug, filename_log_info):
    logging.basicConfig(level=logging.DEBUG, filename=filename_log_debug, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
    logger_info = logging.getLogger("INFO")
    logger_info.setLevel(logging.INFO)
    filehandler_info = logging.FileHandler(filename_log_info, "w")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler_info.setFormatter(formatter)
    logger_info.addHandler(filehandler_info)
    return logger_info
def scrape_product_details(product_soup):
    product_info = {
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
    product_info["product_name"] = "\"" + product_soup.find('h2', 'ui-search-item__title').string + "\""
    product_info["product_url"] = product_soup.find("a", "ui-search-link").get("href")
    product_info["image_url"] = product_soup.find('img', 'ui-search-result-image__element').get('data-src')
    product_page = BeautifulSoup(requests.get(product_info["product_url"]).text, 'html.parser')
    try:
        product_info["reviews"] = product_page.find('span', 'ui-pdp-review__amount').string.replace("(", "").replace(")", "")
    except:
        product_info["reviews"] = "0"
    try:
        product_info["publication_id"] = product_page.findAll('span', 'ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD')[-1].string.strip()
    except:
        pass
    try:
        subtext_status = product_page.find("span", "ui-pdp-subtitle").string.split("|")
        product_info["status"] = subtext_status[0].strip()
        product_info["units_sold"] = subtext_status[1].replace("vendido", "").replace("s", "").strip() if len(subtext_status) == 2 else "0"
    except:
        pass
    try:
        product_info["price"] = product_page.find('span', 'andes-money-amount__fraction').string.replace(".", "")
    except:
        logger_info.info("Failed to retrieve price, setting to -")
        product_info["price"] = "-"
    products.append(product_info)
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
parser = argparse.ArgumentParser()
parser.add_argument("--search", help="Product to search on MercadoLibre")
parser.add_argument("--pages", help="Number of pages to search (Default: 1)")
args = parser.parse_args()
if args.search:
    search_query = args.search.replace(" ", "-")
else:
    print("Error: No product provided for search")
    sys.exit(1)
log_info_filename = os.path.join("log", f"search_{search_query}_ml_INFO_{current_timestamp.split(' ')[0]}.log")
log_debug_filename = os.path.join("log", f"search_{search_query}_ml_DEBUG_{current_timestamp.split(' ')[0]}.log")
logger_info = initialize_logging(log_debug_filename, log_info_filename)
num_pages = int(args.pages) if args.pages else 1
search_url = f"https:
logger_info.info(f"Starting scraping on MercadoLibre for product '{search_query}'")
print("URL: ", search_url)
products = []
for page_num in range(num_pages):
    try:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"{soup.title.string} | Page {page_num + 1}")
    except Exception as e:
        print("Error fetching page:", e)
        sys.exit(1)
    thread_list = []
    for product_soup in soup.find_all('li', 'ui-search-layout__item'):
        thread = threading.Thread(target=scrape_product_details, args=(product_soup,))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
    if page_num < num_pages - 1:
        try:
            next_page_link = soup.find('li', 'andes-pagination__button andes-pagination__button--next').find('a', 'andes-pagination__link')
            search_url = next_page_link.get('href')
            logger_info.info(f"Going to the next page: {search_url}")
        except Exception as e:
            logger_info.error(f"Error finding the next link: {e}")
            print("Error finding the next link, no more pages available")
            break
output_filename = os.path.join("output", f"search_{search_query}_ml_{current_timestamp.split(' ')[0]}.csv")
with open(output_filename, "w", encoding="utf-8-sig") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=products[0].keys(), delimiter="|")
    writer.writeheader()
    for product_info in products:
        writer.writerow(product_info)
logger_info.info(f"Saved found products to file: {output_filename}")
print("Total products found:", len(products))
print("Process completed successfully")