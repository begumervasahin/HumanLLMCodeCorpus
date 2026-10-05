import unicodedata
from datetime import date
import json
import requests
from bs4 import BeautifulSoup
import traceback
class b21(object):
    def fonk1(self):
        self.b1 = "https:
        self.b2 = (date.today()).strftime("%m/%d/%Y")
        self.b3 = "07/22/2000"
        self.a1 = 0
        self.a2 = 985854
        self.a3 = 25066198
        self.b4 = {}
        self.b5 = {"Host": "www.investing.com",
                                    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                                    "Accept": "text/plain, */*; b6 = 0.01",
                                    "Accept-Language": "en-US,en;b6 = 0.5",
                                    "Accept-Encoding": "gzip, deflate, br",
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "Origin" : "https:
                                    "Connection": "keep-alive"}
    def fonk2(self,b7,b22):
        b7 = self.fonk3(b7)
        b8 = BeautifulSoup(b7, 'html.parser')
        b9 = b8.findAll('table')
        b10 = b9[0].find('thead').find('tr').findAll('th')
        b10 = [i.text for i in b10]
        ''' ['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change %'] '''
        ''' ['Feb 27, 2018', '2.85', '2.85', '2.85', '2.85', '1.70K', '3.64%'] '''
        b11 = b9[0].find('tbody').findAll('tr')
        for j in range(len(b11)):
            b12 = b11[j].findAll("td")
            b13 = [i.text for i in b12]
            for k in range(len(b13)):
                pass
    def fonk3(self,b7):
        return (unicodedata.normalize('NFKD', b7.text).encode('ascii', 'ignore'))
    def get_historical_data (self,b22,b23):
        b14 = self.b1 + "instruments/HistoricalDataAjax"
        b15 = { "a2": str(self.a2),
                    "a3": str(self.a3),
                    "header": b23+"+Historical+Data",
                    "st_date": self.b3,
                    "end_date": self.b2,
                    "interval_sec": "Daily",
                    "sort_col": "date",
                    "sort_ord": "DESC",
                    "action": "b21"}
        b16 = self.b5
        b16["DNT"] = "1"
        b16["Content-Length"] = "173"
        b16["Referer"] = "https:
        b16["Cookie"] = "b17 = d8gd4j3pg1ejqasrbjcsoaiesu; b19=1566306981; StickySession=id.23934873569.846_www.investing.com; adbBLk=1; billboardCounter_1=0; G_ENABLED_IDPS=google; r_p_s_n=1; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A4%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941230%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A24%3A%22%2Fequities%2Fbarclays-kenya%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941227%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fsafaricom%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A14%3A%22Euro+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-usd%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%228839%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fus-spx-500-futures%22%3B%7D%7D%7D%7D; sideBlockTimeframe=max; geoC=KE; gtmFired=OK; nyxDorf=MDQ3YTFjZScxYDs3MH1hYTJjZCE%2BOzo%2F"
        b18 = requests.request("POST", b14=b14, b7=b15, b16=b16)
        self.fonk2(b18,b22)
        self.a1 += 1
        print (b22)
    def fonk4(self,b25):
        b14 = self.b1 + "stock-screener/Service/SearchStocks"
        a4 = 1
        b15 = { "b4[]":b25,
                    "sector": "7, 5, 12, 3, 8, 9, 1, 6, 2, 4, 10, 11",
                    "industry": "81, 56, 59, 41, 68, 67, 88, 51, 72, 47, 12, 8, 50, 2, 71, 9, 69, 45, 46, 13, 94, 102, 95, 58, 100, 101, 87, 31, 6, 38, 79, 30, 77, 28, 5, 60, 18, 26, 44, 35, 53, 48, 49, 55, 78, 7, 86, 10, 1, 34, 3, 11, 62, 16, 24, 20, 54, 33, 83, 29, 76, 37, 90, 85, 82, 22, 14, 17, 19, 43, 89, 96, 57, 84, 93, 27, 74, 97, 4, 73, 36, 42, 98, 65, 70, 40, 99, 39, 92, 75, 66, 63, 21, 25, 64, 61, 32, 91, 52, 23, 15, 80",
                    "equityType": "ORD, DRC, Preferred, Unit, ClosedEnd, REIT, ELKS, OpenEnd, Right, ParticipationShare, CapitalSecurity, PerpetualCapitalSecurity, GuaranteeCertificate, IGC, Warrant, SeniorNote, Debenture, ETF, ADR, ETC, ETN",
                    "pn": a4,
                    "order[col]": "eq_market_cap",
                    "order[dir]": "d" }
        b16 = self.b5
        b16["Accept"] = "application/json, text/javascript, */*; b6 = 0.01"
        b16["Content-Length"] = "872"
        b16["Cookie"] = "b19 = 1566368914; _ga=GA1.2.743399127.1566368920; G_ENABLED_IDPS=google; __qca=P0-736185115-1566368921663; r_p_s_n=1; _hjid=c815f523-6bae-42ad-9000-8a51de786167; b17=35f195d457gnp2kufa50dpri79; StickySession=id.83344366310.465.www.investing.com; cookieConsent=was-set; editionPostpone=1566649424685; _gaexp=GAX1.2.l_phCk-tRQKz79dVNnxpag.18215.1; geoC=KE; _gid=GA1.2.1911750261.1566985341; gtmFired=OK; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A6%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%228839%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fus-spx-500-futures%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2237428%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A21%3A%22%2Findices%2Fkenya-nse-20%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2229071%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A26%3A%22%2Findices%2Fftse-nse-kenya-25%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941227%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fsafaricom%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941234%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A17%3A%22%2Fequities%2Fbamburi%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2242554%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A34%3A%22%2Fequities%2Fkenya-commercial-bank-rw%22%3B%7D%7D%7D%7D; _gat=1; _gat_allSitesTracker=1; nyxDorf=ZGVkNjF5M2cwZmx%2BYTVkYmUqNGgyPA%3D%3D; billboardCounter_1=1"
        b16["Referer"] = self.b1 +"stock-screener/?b20 = b4::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1"
        b16["Sec-Fetch-Mode"] = "cors"
        b16["Sec-Fetch-Site"] = "same-origin"
        while True:
            b18 = requests.request("POST", b14, b7=b15, b16=b16)
            try:
                if ((json.loads(b18.text)["pageNumber"]) == 1 and a4 != 1 ):
                    break
                b21 = self.fonk3(b18)
                for i in range(len(json.loads(b21)["hits"])):
                    b22 = json.loads(b18.text)["hits"][i]["viewData"]["b22"]
                    b23 = json.loads(b18.text)["hits"][i]["viewData"]["symbol"]
                    self.get_historical_data(b22 = b22, b23=b23)
                    self.a2 += 1
                    self.a3  += 1
                a4 += 1
                b15["pn"] = a4
            except Exception:
                traceback.print_exc()
                a4 += 1
                b15["pn"] = a4
                if a4 > 210 :
                    break
    def fonk5(self):
        b14 = self.b1 + "search/service/SearchInnerPage"
        b15 = {"search_text": "kenya",
                   "tab": "quotes",
                   "isFilter" : "true"
                   }
        b16 = self.b5
        b16["Content-Length"] = "173"
        b16["Sec-Fetch-Mode"] = "same-origin"
        b16["Referer"] = "https:
        b16[
            "Cookie"] = "b19 = 1566368914; _ga=GA1.2.743399127.1566368920; G_ENABLED_IDPS=google; __qca=P0-736185115-1566368921663; r_p_s_n=1; _hjid=c815f523-6bae-42ad-9000-8a51de786167; b17=35f195d457gnp2kufa50dpri79; geoC=GB; StickySession=id.83344366310.465.www.investing.com; _gid=GA1.2.70643849.1566649388; cookieConsent=was-set; gtmFired=OK; editionPostpone=1566649424685; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A2%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%228839%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fus-spx-500-futures%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2237428%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A21%3A%22%2Findices%2Fkenya-nse-20%22%3B%7D%7D%7D%7D; _gaexp=GAX1.2.l_phCk-tRQKz79dVNnxpag.18215.1; nyxDorf=YGEwYmUtYzZjNTwuMGI4Pz5sM3ZkYjIyYmQ%3D; billboardCounter_1=0; _gat=1; _gat_allSitesTracker=1"
        b18 = requests.request("POST", b14, b7=b15, b16=b16)
        b24 = []
        for i in range(1,(len(json.loads(b18.text)["filters"]["b4"]))):
            b25 = (json.loads(b18.text)["filters"]["b4"][i]["b25"])
            self.b4[(b25)] = (json.loads(b18.text)["filters"]["b4"][i]["country_name_translated"])
            b24.append(b25)
        print(len(b24))
        return({"b24":b24})