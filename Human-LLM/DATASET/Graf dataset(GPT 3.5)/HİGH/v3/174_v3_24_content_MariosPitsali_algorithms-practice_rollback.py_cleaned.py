import sqlite3
import datetime
import pytz
class class1(object):
    def fonk1(self, b7: str, opening_balance: b1 = 0):
        self.b2 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
        self.fonk2()
        self.fonk3(b7, opening_balance)
    def fonk2(self):
        self.b2.execute("CREATE TABLE IF NOT EXISTS accounts(b7 TEXT PRIMARY KEY NOT NULL, b10 INTEGER NOT NULL)")
        self.b2.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")
        self.b2.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, history.account, history.amount FROM history ORDER BY history.time")
    def fonk3(self, b7: str, opening_balance: b1):
        b3 = self.b2.execute("SELECT b7, b10 FROM accounts WHERE (b7 = ?)", (b7,))
        b4 = b3.fetchone()
        if b4 is not None:
            self.b7, self.b5 = b4
            print("Retrieved b10 for", self.b7, b6 = "")
        else:
            self.b7 = b7
            self.b5 = opening_balance / 100
            b3.execute("INSERT INTO accounts VALUES (?, ?)", (b7, opening_balance))
            b3.connection.commit()
            print("class1 created for", self.b7)
        self.fonk4()
    def fonk4(self):
        print("Balance on account", self.b7, "is", self.b5)
    def fonk5(self):
        return datetime.datetime.now(pytz.timezone('UTC'))
    def fonk6(self, amount: b1) -> float:
        if amount > 0.0:
            self.fonk8(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self.b5
    def fonk7(self, amount: b1) -> float:
        if self.b5 > amount > 0.0:
            self.fonk8(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return self.b5
        else:
            print("Amount must be more than zero and less than your account b10.")
            return self.b5
    def fonk8(self, amount):
        b8 = self.b5 + amount
        b9 = self.fonk5()
        self.b2.execute("UPDATE accounts SET b10 = ? WHERE (b7 = ?)", (b8, self.b7))
        self.b2.execute("INSERT INTO history VALUES (?, ?, ?)", (b9, self.b7, amount))
        self.b2.commit()
        self.b5 = b8
    def fonk9(self):
        self.b2.close()
if b11 = = "__main__":
    b12 = class1("John")
    b12.fonk6(1010)
    b12.fonk6(10)
    b12.fonk6(10)
    b12.fonk7(30)
    b12.fonk4()
    b13 = class1("Terry")
    b14 = class1("Graham", 9000)
    b15 = class1("Eric", 7000)
    b16 = class1("Jordan", 8000)
    b16.fonk6(1000)
    b15.fonk6(2000)
    b15.fonk7(90000)