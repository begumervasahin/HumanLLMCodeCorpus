import unicodedata
from datetime import date
import json
import requests
from bs4 import BeautifulSoup
import traceback
class class1:
    def fonk1(self):
        self.b1 = "https:
        self.b2 = date.today().strftime("%m/%d/%Y")
        self.b3 = "07/22/2000"
        self.a1 = 0
        self.a2 = 985854
        self.a3 = 25066198
        self.b4 = {}
        self.b5 = {
            "Host": "www.investing.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Accept": "text/plain, */*; b6 = 0.01",
            "Accept-Language": "en-US,en;b6 = 0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https:
            "Connection": "keep-alive"
        }
    def fonk2(self, data, link):
        pass
    def fonk3(self, data):
        return unicodedata.normalize('NFKD', data.text).encode('ascii', 'ignore')
    def fonk4(self, link, short_hand):
        b7 = self.b1 + "instruments/HistoricalDataAjax"
        b8 = {
            "a2": str(self.a2),
            "a3": str(self.a3),
            "header": f"{short_hand}+Historical+Data",
            "st_date": self.b3,
            "end_date": self.b2,
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        b5 = self.b5.copy()
        b5["DNT"] = "1"
        b5["Content-Length"] = "173"
        b5["Referer"] = f"https:
        b5["Cookie"] = "Your cookie here"
        b9 = requests.post(b7=b7, data=b8, b5=b5)
        self.fonk2(b9, link)
        self.a1 += 1
        print(link)
    def fonk5(self, country_ID):
        pass
    def fonk6(self):
        pass
if b10 = = "__main__":
    b11 = class1()
    b11.fonk6()