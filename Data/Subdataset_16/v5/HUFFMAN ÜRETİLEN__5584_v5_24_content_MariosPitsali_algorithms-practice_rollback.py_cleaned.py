import sqlite3
import datetime
import pytz
b1 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
b1.execute()
b1.execute()
b1.execute()
class class1:
    def fonk1(self, b3: str, opening_balance: b2 = 0):
        self.b3 = b3
        self.b4 = self.fonk2(b3, opening_balance)
        self.fonk3()
    def fonk2(self, b3: str, opening_balance: b2) -> b2:
        b5 = b1.execute("SELECT b9 FROM accounts WHERE b3 = ?", (b3,))
        b6 = b5.fetchone()
        if b6:
            print(f"Retrieved b9 for {b3}")
            return b6[0]
        else:
            b1.execute("INSERT INTO accounts (b3, b9) VALUES (?, ?)", (b3, opening_balance))
            b1.commit()
            print(f"class1 created for {b3}")
            return opening_balance
    def fonk3(self):
        print(f"Balance on account {self.b3} is {self.b4 / 100:.2f}")
    @staticmethod
    def fonk4():
        return datetime.datetime.now(pytz.utc)
    def fonk5(self, amount: b2) -> float:
        if amount > 0:
            self.fonk7(amount)
            print(f"{amount / 100:.2f} deposited")
        return self.b4 / 100
    def fonk6(self, amount: b2) -> float:
        if 0 < amount <= self.b4:
            self.fonk7(-amount)
            print(f"{amount / 100:.2f} withdrawn")
        else:
            print("Amount must be more than zero and less than your account b9.")
        return self.b4 / 100
    def fonk7(self, amount: b2):
        b7 = self.b4 + amount
        b8 = self.fonk4()
        b1.execute("UPDATE accounts SET b9 = ? WHERE b3 = ?", (b7, self.b3))
        b1.execute("INSERT INTO history (time, account, amount) VALUES (?, ?, ?)", (b8, self.b3, amount))
        b1.commit()
        self.b4 = b7
if b10 = = "__main__":
    b11 = class1("John")
    b11.fonk5(1010)
    b11.fonk5(10)
    b11.fonk5(10)
    b11.fonk6(30)
    b11.fonk3()
    b12 = class1("Terry")
    b13 = class1("Graham", 9000)
    b14 = class1("Eric", 7000)
    b15 = class1("Jordan", 8000)
    b15.fonk5(1000)
    b14.fonk5(2000)
    b14.fonk6(90000)
    b1.close()