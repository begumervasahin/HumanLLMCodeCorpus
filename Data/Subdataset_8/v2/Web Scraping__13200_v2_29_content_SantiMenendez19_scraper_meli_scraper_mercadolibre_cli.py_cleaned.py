from bs4 import BeautifulSoup
import requests
import os
import sys
import threading
import argparse
from datetime import datetime
import logging
def start_logging(debug_log_filename, info_log_filename):
    logging.basicConfig(level=logging.DEBUG, filename=debug_log_filename, filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger_info = logging.getLogger("INFO")
    logger_info.setLevel(logging.INFO)
    file_handler_info = logging.FileHandler(info_log_filename, "w")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler_info.setFormatter(formatter)
    logger_info.addHandler(file_handler_info)
    return logger_info
def scrape_product_details(product_soup, logger_info):
    product_dict = {
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
    try:
        product_dict["producto"] = product_soup.find('h2', 'ui-search-item__title').get_text(strip=True)
        product_dict["url_producto"] = product_soup.find("a", "ui-search-link")["href"]
        logger_info.info(f"Scraping product: {product_dict['url_producto']}")
    except Exception as e:
        logger_info.error(f"Error scraping product details: {e}")
    products.append(product_dict)
def setup_argparse():
    parser = argparse.ArgumentParser(description="MercadoLibre Scraper")
    parser.add_argument("--busqueda", required=True, help="Product to search on MercadoLibre")
    parser.add_argument("--paginas", default=1, type=int, help="Number of pages to scrape (default is 1)")
    return parser.parse_args()
def main():
    args = setup_argparse()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    logger_info = start_logging(os.path.join(log_dir, f"debug_{now}.log"),
                                os.path.join(log_dir, f"info_{now}.log"))
    global products
    products = []
    logger_info.info(f"Starting scrape for: {args.busqueda}, Pages: {args.paginas}")
    mock_product_soup = BeautifulSoup("<html><body><h2 class='ui-search-item__title'>Test Product</h2><a class='ui-search-link' href='http:
    scrape_product_details(mock_product_soup, logger_info)
    logger_info.info(f"Scraping complete. Products found: {len(products)}")
    print(f"Products found: {len(products)}")
if __name__ == "__main__":
    main()