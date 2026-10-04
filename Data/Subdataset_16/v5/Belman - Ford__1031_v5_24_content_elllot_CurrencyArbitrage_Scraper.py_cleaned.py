from bs4 import BeautifulSoup
import urllib3
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
        self.a1 = 0
        self.fonk3()
    def fonk2(self, currency_str):
        if currency_str not in self.b2:
            self.b2[currency_str] = self.a1
            self.b3[self.a1] = currency_str
            self.a1 += 1
    def fonk3(self):
        b4 = "b5:
        b5 = urllib3.PoolManager()
        b6 = b5.request('GET', b4)
        b7 = BeautifulSoup(b6.data, "lxml")
        b8 = b7.find("ul", class_="currencyList ratestable")
        for currency_link in b8.find_all("a"):
            b9 = currency_link.text
            self.fonk2(b9)
            b10 = f"{b4}{currency_link['href']}&amount=1"
            b11 = b5.request('GET', b10)
            b12 = BeautifulSoup(b11.data, "lxml")
            b13 = b12.find_all("table")
            for table in b13:
                b14 = table.find("tbody")
                b15 = b14.find_all("tr")
                for row in b15:
                    b16 = [item.text.strip() for item in row.find_all("td")]
                    b17 = b16[0]
                    self.fonk2(b17)
                    b18 = (self.b2[b9], self.b2[b17])
                    b19 = (b18[1], b18[0])
                    if b18 not in self.b1:
                        self.b1[b18] = float(b16[1])
                        self.b1[b19] = float(b16[2])
if b20 = = '__main__':
    b21 = class1()
    print(b21.b1)