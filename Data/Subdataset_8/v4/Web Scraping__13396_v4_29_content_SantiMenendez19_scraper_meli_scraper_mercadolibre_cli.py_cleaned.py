import argparse
import csv
import json
import logging
import os
import requests
import sys
import threading
from datetime import datetime
from bs4 import BeautifulSoup
def start_log(filename_log_debug, filename_log_info):
    logging.basicConfig(level=logging.DEBUG, filename=filename_log_debug, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
    logger_info = logging.getLogger("INFO")
    logger_info.setLevel(logging.INFO)
    filehandler_info = logging.FileHandler(filename_log_info, "w")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler_info.setFormatter(formatter)
    logger_info.addHandler(filehandler_info)
    return logger_info
def scraping_product_details(product_soup):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    product_dict = {
        "fecha_hora": date_now,
        "producto": "",
        "precio": "",
        "moneda": "ARS",
        "url_producto": "",
        "url_img_producto": "",
        "reviews": "",
        "id_publicacion": "",
        "estado": "",
        "vendidos": ""
    }
    title_product = product_soup.find('h2', 'ui-search-item__title').string
    product_dict["producto"] = "\"" + title_product + "\""
    url_product = product_soup.find("a", "ui-search-link").get("href")
    product_dict["url_producto"] = url_product
    logger_info.info(f"Scraping current product from page {url_product}")
    img_product = product_soup.find('img', 'ui-search-result-image__element')
    product_dict["url_img_producto"] = img_product.get('data-src')
    product_soup_details = BeautifulSoup(requests.get(url_product).text, 'html.parser')
    try:
        reviews = product_soup_details.find('span', 'ui-pdp-review__amount').string
        reviews = reviews.replace("(", "")
        reviews = reviews.replace(")", "")
        product_dict["reviews"] = reviews
    except:
        product_dict["reviews"] = "0"
    try:
        id_publish = product_soup_details.findAll('span', 'ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD')[-1].string
        id_publish = id_publish.strip()
        product_dict["id_publicacion"] = id_publish
    except:
        pass
    try:
        subtext_status = product_soup_details.find("span", "ui-pdp-subtitle").string.split("|")
        status = subtext_status[0].strip()
        if len(subtext_status) == 2:
            count_selled = subtext_status[1].replace("vendido", "").replace("s", "").strip()
        else:
            count_selled = "0"
        product_dict["estado"] = status
        product_dict["vendidos"] = count_selled
    except:
        pass
    try:
        price = product_soup_details.find('span', 'andes-money-amount__fraction').string.replace(".", "")
        product_dict["precio"] = price
    except:
        logger_info.info("Failed to find price, setting to -")
        product_dict["precio"] = "-"
    products.append(product_dict)
date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
parser = argparse.ArgumentParser()
parser.add_argument("--busqueda", help="Product to search on MercadoLibre")
parser.add_argument("--paginas", help="Number of pages to search (Default: 1)")
args = parser.parse_args()
if args.busqueda:
    product_find = args.busqueda.replace(" ", "-")
else:
    print("Error: No product provided for search")
    sys.exit(1)
filename_log_info = os.path.join("log", "search_" + product_find + "_ml_INFO_" + date_now.split(" ")[0] + ".log")
filename_log_debug = os.path.join("log", "search_" + product_find + "_ml_DEBUG_" + date_now.split(" ")[0] + ".log")
logger_info = start_log(filename_log_debug, filename_log_info)
if args.paginas:
    try:
        count_pages = int(args.paginas)
    except BaseException as err:
        logger_info.error("Error in page count, the entered parameter is not a number or is negative")
        print("Error: the entered parameter is not a number")
        sys.exit(1)
    if count_pages < 1:
        logger_info.error("Error in page count, the entered parameter is not a number or is negative")
        print("Error: Pages cannot be less than 1")
        sys.exit(1)
    else:
        print(f"Searching {count_pages} pages")
else:
    print(f"No page count provided, defaulting to 1")
    count_pages = 1
url = "https:
url += product_find + "_OrderId_PRICE"
logger_info.info(f"Starting scraping on MercadoLibre for product {product_find}")
print("URL: ", url)
products = []
for i in range(0, count_pages):
    try:
        response = requests.get(url)
    except requests.RequestException as err:
        logger_info.error(f"Error while trying to fetch the next page ({i}), the page did not respond to the request")
        print("Error fetching page, it might be down or non-existent " + err)
        sys.exit(1)
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_url = soup.title.string
        print(title_url + " | Page " + str(i+1))
    except Exception as err:
        print(err)
    thread_list = []
    for product_soup in soup.find_all('li', 'ui-search-layout__item'):
        thread_scraping = threading.Thread(target=scraping_product_details, args=(product_soup,))
        thread_list.append(thread_scraping)
        thread_scraping.start()
    for thread in thread_list:
        thread.join()
    try:
        if i < count_pages - 1:
            link_next = (soup.find('li', 'andes-pagination__button andes-pagination__button--next')).find('a', 'andes-pagination__link')
            url = link_next.get('href')
            logger_info.info(f"Going to the next page of product {url}")
    except Exception as err:
        logger_info.error(f"Error finding the next link. " + str(err))
        print("Error finding the next link, pages exhausted")
        print(err)
        if len(products) == 0:
            print("No products found")
            sys.exit(1)
        break
logger_info.info(f"Saving found products to file " + os.path.join("output", "search_" + product_find + "_ml_" + date_now.split(" ")[0] + ".csv"))
filename = open(os.path.join("output