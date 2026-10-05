import pandas as pd
from multiprocessing import Pool
import sys
from your_module import RequestsBS4, DataProcessing
class Scraper:
    def __init__(self, site="https:
        self.site = site
    def get_url_categories(self):
        pass
    def get_url_products_test(self):
        pass
    def get_url_products(self, url=None):
        pass
    def scrape_and_save(self, url=None):
        pass
    def get_product_info(self):
        pass
    def execute_scraper(self):
        print("\nWelcome to Macy's Web Scraper!")
        while True:
            scrape_choice = input("\nEnter 't' to scrape a small sample, "
                                  "\n'f' to scrape full web, "
                                  "\n's' to search for product information, "
                                  "\nor press 'q' to quit the program: ").upper()
            if scrape_choice == 'Q':
                print("Exiting the program.")
                sys.exit()
            if scrape_choice in ['T', 'F', 'S']:
                break
            else:
                print("Invalid choice. Please try again.")
        if scrape_choice == 'T':
            self.scrape_small_sample()
        elif scrape_choice == 'F':
            self.scrape_full_web()
        elif scrape_choice == 'S':
            self.search_product_info()
    def scrape_small_sample(self):
        url = self.get_url_products_test()
        p = Pool(processes=2)
        p.map(self.scrape_and_save, url)
        p.close()
        p.join()
    def scrape_full_web(self):
        category_urls = self.get_url_categories()
        p1 = Pool(processes=4)
        url_scraping = p1.map(self.get_url_products, category_urls)
        p1.close()
        p1.join()
        product_urls = pd.read_csv("product-url.csv", names=["url"])
        url = product_urls["url"].values.tolist()
        p2 = Pool(processes=2)
        p2.map(self.scrape_and_save, url)
        p2.close()
        p2.join()
    def search_product_info(self):
        self.get_product_info()
if __name__ == "__main__":
    scraper = Scraper()
    scraper.execute_scraper()