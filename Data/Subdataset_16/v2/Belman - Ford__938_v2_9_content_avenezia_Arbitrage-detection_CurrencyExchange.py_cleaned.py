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
def fonk7():
    b4 = class1("USD", "EUR", 0.85)
    print(b4)
    print(f"From Currency: {b4.from_currency}")
    print(f"To Currency: {b4.to_currency}")
    print(f"Exchange Rate: {b4.exchange_rate}")
if b5 = = "__main__":
    fonk7()