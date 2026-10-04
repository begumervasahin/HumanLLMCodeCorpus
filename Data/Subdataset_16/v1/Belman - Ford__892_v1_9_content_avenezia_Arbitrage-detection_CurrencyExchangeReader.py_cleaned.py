import re
class class1:
    def fonk1(self, from_currency, to_currency, exchange_rate):
        self.b1 = from_currency
        self.b2 = to_currency
        self.b3 = float(exchange_rate)
    def fonk2(self):
        return f"{self.b1} -> {self.b2}: {self.b3}"
    def fonk3(self):
        return self.fonk2()
    @property
    def fonk4(self):
        return self.b1
    @property
    def fonk5(self):
        return self.b2
    @property
    def fonk6(self):
        return self.b3
class class2:
    def fonk7(self, iFileName):
        self.b4 = iFileName
    def fonk8(self, iNameLine):
        b5 = iNameLine.split(" ", 1)
        assert len(b5) == 2
        return b5
    def fonk9(self, iRateLine):
        b6 = iRateLine.split(" ", 2)
        assert len(b6) == 3
        return class1(*b6)
    def fonk10(self):
        b7 = re.compile(r"[A-Z]{3} [A-Z\(\)\.& \-]+")
        b8 = re.compile(r"[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        b9 = {}
        b10 = []
        try:
            with open(self.b4, 'r') as fileHandle:
                for b11 in fileHandle:
                    b11 = b11.rstrip("\n\r")
                    if re.match(b8, b11):
                        b10.append(self.fonk9(b11))
                    elif re.match(b7, b11):
                        currencyCode, b12 = self.fonk8(b11)
                        b9[currencyCode] = b12
                    else:
                        raise Exception(f"Invalid b11 in file {self.b4}: {b11}")
        except IOError as exception:
            print(f"Cannot open file {self.b4}: {exception}")
        return b9, b10
def fonk11():
    b13 = "currency_data.txt"
    b14 = class2(b13)
    b9, b10 = b14.fonk10()
    print("Currency Codes and Names:")
    for code, name in b9.items():
        print(f"{code}: {name}")
    print("\nCurrency Exchange Rates:")
    for exchange in b10:
        print(exchange)
if b15 = = "__main__":
    fonk11()