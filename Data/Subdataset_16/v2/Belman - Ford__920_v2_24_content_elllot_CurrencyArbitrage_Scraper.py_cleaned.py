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
        b6 = b5.b10('GET', b4)
        b7 = BeautifulSoup(b6.data, "lxml")
        b8 = b7.find("ul", class_="currencyList ratestable")
        for a in b8.find_all("a"):
            self.fonk2(a.text)
            b9 = f"b5:
            b10 = b5.b10('GET', b9)
            b11 = BeautifulSoup(b10.data, "lxml")
            b12 = b11.find_all("table")
            for table in b12:
                b13 = table.find("tbody")
                b14 = b13.find_all("tr")
                for row in b14:
                    b15 = row.find_all("td")
                    b15 = [item.text.strip() for item in b15]
                    self.fonk2(b15[0])
                    b16 = (self.b2[a.text], self.b2[b15[0]])
                    if b16 not in self.b1:
                        self.b1[b16] = float(b15[1])
                        self.b1[(b16[1], b16[0])] = float(b15[2])
if b17 = = '__main__':
    b18 = class1()
    print(b18.b1)