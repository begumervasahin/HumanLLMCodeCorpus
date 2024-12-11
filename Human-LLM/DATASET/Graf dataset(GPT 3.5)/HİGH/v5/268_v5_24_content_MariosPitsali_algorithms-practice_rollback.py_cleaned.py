import sqlite3
class class1:
    def fonk1(self, filename):
        self.b1 = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
    def fonk2(self, query, b2 = None):
        b3 = self.b1.fonk2(query, b2) if b2 else self.b1.fonk2(query)
        return b3
    def fonk3(self):
        self.b1.fonk3()
    def fonk4(self):
        self.b1.fonk4()
class class2:
    def fonk5(self, b5: str, opening_balance: b4 = 0, b6: class1 = None):
        self.b5 = b5
        self.b6 = b6
        self.fonk6(opening_balance)
    def fonk6(self, opening_balance: b4):
        b3 = self.b6.fonk2("SELECT b5, b12 FROM accounts WHERE (b5 = ?)", (self.b5,))
        b7 = b3.fetchone()
        if b7 is not None:
            self.b5, self.b8 = b7
            print("Retrieved b12 for {}".format(self.b5), b9 = "")
        else:
            self.fonk7(opening_balance)
    def fonk7(self, opening_balance: b4):
        self.b8 = opening_balance / 100
        self.b6.fonk2("INSERT INTO accounts VALUES (?, ?)", (self.b5, opening_balance))
        self.b6.fonk3()
        print("class2 created for {}".format(self.b5))
    def fonk8(self):
        print("Balance on account {} is {:.2f}".format(self.b5, self.b8))
    def fonk9(self, amount: b4) -> float:
        if amount > 0:
            self.fonk11(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self.b8
    def fonk10(self, amount: b4) -> float:
        if self.b8 > amount > 0:
            self.fonk11(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
        else:
            print("Amount must be more than zero and less than your account b12.")
        return self.b8
    def fonk11(self, amount: b4):
        b10 = self.b8 + amount / 100
        b11 = self.fonk12()
        self.b6.fonk2("UPDATE accounts SET b12 = ? WHERE (b5 = ?)", (b10, self.b5))
        self.b6.fonk2("INSERT INTO history VALUES (?, ?, ?)", (b11, self.b5, amount))
        self.b6.fonk3()
        self.b8 = b10
    def fonk12(self):
        return 1
if b13 = = "__main__":
    b6 = class1("accounts.sqlite")
    try:
        b14 = class2("John", b6=b6)
        b14.fonk9(1010)
        b14.fonk9(10)
        b14.fonk9(10)
        b14.fonk10(30)
        b14.fonk8()
        b15 = class2("Terry", b6=b6)
        b16 = class2("Graham", 9000, b6=b6)
        b17 = class2("Eric", 7000, b6=b6)
        b18 = class2("Jordan", 8000, b6=b6)
        b18.fonk9(1000)
        b17.fonk9(2000)
        b17.fonk10(90000)
    finally:
        b6.fonk4()