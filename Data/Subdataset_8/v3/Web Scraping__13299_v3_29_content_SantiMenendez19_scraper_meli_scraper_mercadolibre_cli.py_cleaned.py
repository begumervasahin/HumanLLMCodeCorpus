from bs4 import BeautifulSoup
import requests
import os
import argparse
import logging
from datetime import datetime
def setup_logging(debug_log_filename, info_log_filename):
    logging.basicConfig(level=logging.DEBUG, filename=debug_log_filename, filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger_info = logging.getLogger("INFO")
    logger_info.setLevel(logging.INFO)
    file_handler_info = logging.FileHandler(info_log_filename, "w")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler_info.setFormatter(formatter)
    logger_info.addHandler(file_handler_info)
    return logger_info
def scrape_product(product_soup, logger_info):
    product_details = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": "",
        "price": "",
        "currency": "ARS",
        "url": "",
        "image_url": "",
        "reviews": "",
        "publication_id": "",
        "status": "",
        "sold_count": ""
    }
    try:
        product_details["name"] = product_soup.find('h2', 'ui-search-item__title').get_text(strip=True)
        product_details["url"] = product_soup.find("a", "ui-search-link")["href"]
        logger_info.info(f"Scraping product: {product_details['url']}")
    except Exception as e:
        logger_info.error(f"Error scraping product details: {e}")
    products.append(product_details)
def parse_arguments():
    parser = argparse.ArgumentParser(description="MercadoLibre Scraper")
    parser.add_argument("--query", required=True, help="Product to search on MercadoLibre")
    parser.add_argument("--pages", default=1, type=int, help="Number of pages to scrape (default is 1)")
    return parser.parse_args()
def main():
    args = parse_arguments()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    logger_info = setup_logging(os.path.join(log_directory, f"debug_{now}.log"),
                                os.path.join(log_directory, f"info_{now}.log"))
    global products
    products = []
    logger_info.info(f"Starting scrape for: {args.query}, Pages: {args.pages}")
    mock_product_soup = BeautifulSoup("<html><body><h2 class='ui-search-item__title'>Test Product</h2><a class='ui-search-link' href='http:
    scrape_product(mock_product_soup, logger_info)
    logger_info.info(f"Scraping complete. Products found: {len(products)}")
    print(f"Products found: {len(products)}")
if __name__ == "__main__":
    main()