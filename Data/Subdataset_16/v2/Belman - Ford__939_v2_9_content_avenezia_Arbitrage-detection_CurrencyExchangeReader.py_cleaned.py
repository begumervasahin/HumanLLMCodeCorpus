import re
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = float(b3)
    def fonk2(self):
        return f"{self.b1} -> {self.b2}: {self.b3}"
    def fonk3(self):
        return self.fonk2()
class class2:
    def fonk4(self, b4):
        self.b4 = b4
    def fonk5(self, name_line):
        b5 = name_line.split(" ", 1)
        if len(b5) != 2:
            raise ValueError(f"Invalid currency b11 b10: {name_line}")
        return b5[0], b5[1]
    def fonk6(self, rate_line):
        b5 = rate_line.split(" ", 2)
        if len(b5) != 3:
            raise ValueError(f"Invalid currency exchange rate b10: {rate_line}")
        return class1(b5[0], b5[1], b5[2])
    def fonk7(self):
        b6 = re.compile(r"[A-Z]{3} [A-Z\(\)\.& \-]+")
        b7 = re.compile(r"[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        b8 = {}
        b9 = []
        try:
            with open(self.b4, 'r') as file:
                for b10 in file:
                    b10 = b10.strip()
                    if b7.match(b10):
                        b9.append(self.fonk6(b10))
                    elif b6.match(b10):
                        code, b11 = self.fonk5(b10)
                        b8[code] = b11
                    else:
                        raise ValueError(f"Invalid b10 in file {self.b4}: {b10}")
        except IOError as e:
            print(f"Cannot open file {self.b4}: {e}")
        return b8, b9
def fonk8():
    b4 = "currency_data.txt"
    b12 = class2(b4)
    b8, b9 = b12.fonk7()
    print("Currency Codes and Names:")
    for code, b11 in b8.items():
        print(f"{code}: {b11}")
    print("\nCurrency Exchange Rates:")
    for exchange in b9:
        print(exchange)
if b13 = = "__main__":
    fonk8()