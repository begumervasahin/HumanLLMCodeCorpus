import unicodedata
from datetime import date
import json
import requests
from bs4 import BeautifulSoup
import traceback
class HistoricalDataScraper:
    def __init__(self):
        self.base_url = "https:
        self.today_date = date.today().strftime("%m/%d/%Y")
        self.start_date = "07/22/2000"
        self.num_required_calls = 0
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
    def scrape_historical_data(self, data, link):
        data_text = self.convert_unicode_to_text(data)
        soup = BeautifulSoup(data_text, 'html.parser')
        tables = soup.find_all('table')
        head_rows = [th.text for th in tables[0].find('thead').find('tr').find_all('th')]
        body_rows = tables[0].find('tbody').find_all('tr')
        for row in body_rows:
            cells = [cell.text for cell in row.find_all("td")]
    def convert_unicode_to_text(self, data):
        return unicodedata.normalize('NFKD', data.text).encode('ascii', 'ignore')
    def get_historical_data(self, link, short_hand):
        url = self.base_url + "instruments/HistoricalDataAjax"
        payload = {
            "curr_id": str(self.curr_id),
            "smlID": str(self.smlID),
            "header": short_hand + " Historical Data",
            "st_date": self.start_date,
            "end_date": self.today_date,
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        headers = self.headers
        headers["DNT"] = "1"
        headers["Content-Length"] = "173"
        headers["Referer"] = "https:
        headers["Cookie"] = "Add your cookie here"
        response = requests.post(url=url, data=payload, headers=headers)
        self.scrape_historical_data(response, link)
        self.num_required_calls += 1
        print(link)
    def get_company_stocks(self, country_id):
        url = self.base_url + "stock-screener/Service/SearchStocks"
        page = 1
        payload = {
            "country[]": country_id,
            "sector": "7, 5, 12, 3, 8, 9, 1, 6, 2, 4, 10, 11",
            "industry": "81, 56, 59, 41, 68, 67, 88, 51, 72, 47, 12, 8, 50, 2, 71, 9, 69, 45, 46, 13, 94, 102, 95, 58, 100, 101, 87, 31, 6, 38, 79, 30, 77, 28, 5, 60, 18, 26, 44, 35, 53, 48, 49, 55, 78, 7, 86, 10, 1, 34, 3, 11, 62, 16, 24, 20, 54, 33, 83, 29, 76, 37, 90, 85, 82, 22, 14, 17, 19, 43, 89, 96, 57, 84, 93, 27, 74, 97, 4, 73, 36, 42, 98, 65, 70, 40, 99, 39, 92, 75, 66, 63, 21, 25, 64, 61, 32, 91, 52, 23, 15, 80",
            "equityType": "ORD, DRC, Preferred, Unit, ClosedEnd, REIT, ELKS, OpenEnd, Right, ParticipationShare, CapitalSecurity, PerpetualCapitalSecurity, GuaranteeCertificate, IGC, Warrant, SeniorNote, Debenture, ETF, ADR, ETC, ETN",
            "pn": page,
            "order[col]": "eq_market_cap",
            "order[dir]": "d"
        }
        headers = self.headers
        headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        headers["Content-Length"] = "872"
        headers["Cookie"] = "Add your cookie here"
        headers["Referer"] = self.base_url + "stock-screener/?sp=country::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "same-origin"
        while True:
            response = requests.post(url, data=payload, headers=headers)
            try:
                if json.loads(response.text)["pageNumber"] == 1 and page != 1:
                    break
                historical_data = self.convert_unicode_to_text(response)
                for i in range(len(json.loads(historical_data)["hits"])):
                    link = json.loads(response.text)["hits"][i]["viewData"]["link"]
                    short_hand = json.loads(response.text)["hits"][i]["viewData"]["symbol"]
                    self.get_historical_data(link=link, short_hand=short_hand)
                    self.curr_id += 1
                    self.smlID += 1
                page += 1
                payload["pn"] = page
            except Exception:
                traceback.print_exc()
                page += 1
                payload["pn"] = page
                if page > 210:
                    break
    def search(self):
        url = self.base_url + "search/service/SearchInnerPage"
        payload = {
            "search_text": "kenya",
            "tab": "quotes",
            "isFilter": "true"
        }
        headers = self.headers
        headers["Content-Length"] = "173"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Referer"] = "https:
        headers["Cookie"] = "Add your cookie here"
        response = requests.post(url, data=payload, headers=headers)
        country_ids = []
        for i in range(1, len(json.loads(response.text)["filters"]["country"])):
            country_id = json.loads(response.text)["filters"]["country"][i]["country_ID"]
            self.country[country_id] = json.loads(response.text)["filters"]["country"][i]["country_name_translated"]
            country_ids.append(country_id)
        print(len(country_ids))
        return {"country_ids": country_ids}