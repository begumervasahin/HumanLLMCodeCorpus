import unicodedata
from datetime import date
import json
import requests
from bs4 import BeautifulSoup
import traceback
class HistoricalDataScraper:
    def __init__(self):
        self.base_url = "https:
        self.todays_date = date.today().strftime("%m/%d/%Y")
        self.start_date = "07/22/2000"
        self.number_of_required_calls = 0
        self.curr_id = 985854
        self.smlID = 25066198
        self.country = {}
        self.headers = {
            "Host": "www.investing.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Accept": "text/plain, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https:
            "Connection": "keep-alive"
        }
    def process_historical_data(self, data, link):
        pass
    def convert_unicode_to_text(self, data):
        return unicodedata.normalize('NFKD', data.text).encode('ascii', 'ignore')
    def fetch_historical_data(self, link, short_hand):
        url = self.base_url + "instruments/HistoricalDataAjax"
        payload = {
            "curr_id": str(self.curr_id),
            "smlID": str(self.smlID),
            "header": f"{short_hand}+Historical+Data",
            "st_date": self.start_date,
            "end_date": self.todays_date,
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        headers = self.headers.copy()
        headers["DNT"] = "1"
        headers["Content-Length"] = "173"
        headers["Referer"] = f"https:
        headers["Cookie"] = "Your cookie here"
        response = requests.post(url=url, data=payload, headers=headers)
        self.process_historical_data(response, link)
        self.number_of_required_calls += 1
        print(link)
    def fetch_company_stocks(self, country_ID):
        pass
    def search_for_country(self):
        pass
if __name__ == "__main__":
    historical_scraper = HistoricalDataScraper()
    historical_scraper.search_for_country()