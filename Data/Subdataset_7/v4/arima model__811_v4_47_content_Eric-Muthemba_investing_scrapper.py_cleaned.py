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
    def fonk2(self, data, b18):
        b7 = self.fonk3(data)
        b8 = BeautifulSoup(b7, 'html.parser')
        b9 = b8.find_all('table')
        b10 = [th.text for th in b9[0].find('thead').find('tr').find_all('th')]
        b11 = b9[0].find('tbody').find_all('tr')
        for row in b11:
            b12 = [cell.text for cell in row.find_all("td")]
    def fonk3(self, data):
        return unicodedata.normalize('NFKD', data.text).encode('ascii', 'ignore')
    def fonk4(self, b18, b19):
        b13 = self.b1 + "instruments/HistoricalDataAjax"
        b14 = {
            "a2": str(self.a2),
            "a3": str(self.a3),
            "header": b19 + " Historical Data",
            "st_date": self.b3,
            "end_date": self.b2,
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "b17"
        }
        b5 = self.b5
        b5["DNT"] = "1"
        b5["Content-Length"] = "173"
        b5["Referer"] = "https:
        b5["Cookie"] = "Add your cookie here"
        b15 = requests.post(b13=b13, data=b14, b5=b5)
        self.fonk2(b15, b18)
        self.a1 += 1
        print(b18)
    def fonk5(self, b21):
        b13 = self.b1 + "stock-screener/Service/SearchStocks"
        a4 = 1
        b14 = {
            "b4[]": b21,
            "sector": "7, 5, 12, 3, 8, 9, 1, 6, 2, 4, 10, 11",
            "industry": "81, 56, 59, 41, 68, 67, 88, 51, 72, 47, 12, 8, 50, 2, 71, 9, 69, 45, 46, 13, 94, 102, 95, 58, 100, 101, 87, 31, 6, 38, 79, 30, 77, 28, 5, 60, 18, 26, 44, 35, 53, 48, 49, 55, 78, 7, 86, 10, 1, 34, 3, 11, 62, 16, 24, 20, 54, 33, 83, 29, 76, 37, 90, 85, 82, 22, 14, 17, 19, 43, 89, 96, 57, 84, 93, 27, 74, 97, 4, 73, 36, 42, 98, 65, 70, 40, 99, 39, 92, 75, 66, 63, 21, 25, 64, 61, 32, 91, 52, 23, 15, 80",
            "equityType": "ORD, DRC, Preferred, Unit, ClosedEnd, REIT, ELKS, OpenEnd, Right, ParticipationShare, CapitalSecurity, PerpetualCapitalSecurity, GuaranteeCertificate, IGC, Warrant, SeniorNote, Debenture, ETF, ADR, ETC, ETN",
            "pn": a4,
            "order[col]": "eq_market_cap",
            "order[dir]": "d"
        }
        b5 = self.b5
        b5["Accept"] = "application/json, text/javascript, */*; b6 = 0.01"
        b5["Content-Length"] = "872"
        b5["Cookie"] = "Add your cookie here"
        b5["Referer"] = self.b1 + "stock-screener/?b16 = b4::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1"
        b5["Sec-Fetch-Mode"] = "cors"
        b5["Sec-Fetch-Site"] = "same-origin"
        while True:
            b15 = requests.post(b13, data=b14, b5=b5)
            try:
                if json.loads(b15.text)["pageNumber"] == 1 and a4 != 1:
                    break
                b17 = self.fonk3(b15)
                for i in range(len(json.loads(b17)["hits"])):
                    b18 = json.loads(b15.text)["hits"][i]["viewData"]["b18"]
                    b19 = json.loads(b15.text)["hits"][i]["viewData"]["symbol"]
                    self.fonk4(b18 = b18, b19=b19)
                    self.a2 += 1
                    self.a3 += 1
                a4 += 1
                b14["pn"] = a4
            except Exception:
                traceback.print_exc()
                a4 += 1
                b14["pn"] = a4
                if a4 > 210:
                    break
    def fonk6(self):
        b13 = self.b1 + "search/service/SearchInnerPage"
        b14 = {
            "search_text": "kenya",
            "tab": "quotes",
            "isFilter": "true"
        }
        b5 = self.b5
        b5["Content-Length"] = "173"
        b5["Sec-Fetch-Mode"] = "same-origin"
        b5["Referer"] = "https:
        b5["Cookie"] = "Add your cookie here"
        b15 = requests.post(b13, data=b14, b5=b5)
        b20 = []
        for i in range(1, len(json.loads(b15.text)["filters"]["b4"])):
            b21 = json.loads(b15.text)["filters"]["b4"][i]["country_ID"]
            self.b4[b21] = json.loads(b15.text)["filters"]["b4"][i]["country_name_translated"]
            b20.append(b21)
        print(len(b20))
        return {"b20": b20}