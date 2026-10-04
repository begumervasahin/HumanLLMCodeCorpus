import sqlite3
import datetime
import pytz
b1 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
b1.execute()
b1.execute()
b1.execute()
class class1:
    def fonk1(self, b6: str, opening_balance: b2 = 0):
        b3 = b1.execute("SELECT b6, b9 FROM accounts WHERE b6 = ?", (b6,))
        b4 = b3.fetchone()
        if b4:
            self.b6, self.b5 = b4
            print(f"Retrieved b9 for {self.b6}.")
        else:
            self.b6 = b6
            self.b5 = opening_balance
            b3.execute("INSERT INTO accounts (b6, b9) VALUES (?, ?)", (b6, opening_balance))
            b3.connection.commit()
            print(f"class1 created for {self.b6}.")
        self.fonk2()
    def fonk2(self):
        print(f"Balance on account {self.b6} is {self.b5 / 100:.2f}")
    @staticmethod
    def fonk3():
        return pytz.utc.localize(datetime.datetime.utcnow())
    def fonk4(self, amount: b2) -> float:
        if amount > 0:
            self.fonk6(amount)
            print(f"{amount / 100:.2f} deposited.")
        return self.b5 / 100
    def fonk5(self, amount: b2) -> float:
        if 0 < amount <= self.b5:
            self.fonk6(-amount)
            print(f"{amount / 100:.2f} withdrawn.")
        else:
            print("Amount must be greater than zero and less than or equal to your account b9.")
        return self.b5 / 100
    def fonk6(self, amount: b2):
        b7 = self.b5 + amount
        b8 = self.fonk3()
        b1.execute("UPDATE accounts SET b9 = ? WHERE b6 = ?", (b7, self.b6))
        b1.execute("INSERT INTO history (time, account, amount) VALUES (?, ?, ?)", (b8, self.b6, amount))
        b1.commit()
        self.b5 = b7
def fonk7():
    b10 = class1("John")
    b10.fonk4(1010)
    b10.fonk4(10)
    b10.fonk4(10)
    b10.fonk5(30)
    b10.fonk2()
    b11 = class1("Terry")
    b12 = class1("Graham", 9000)
    b13 = class1("Eric", 7000)
    b14 = class1("Jordan", 8000)
    b14.fonk4(1000)
    b13.fonk4(2000)
    b13.fonk5(90000)
    b1.close()
if b15 = = "__main__":
    fonk7()