import sqlite3
import datetime
import pytz
b1 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
b1.execute("CREATE TABLE IF NOT EXISTS accounts(b7 TEXT PRIMARY KEY NOT NULL, b10 INTEGER NOT NULL)")
b1.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")
b1.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, history.account, history.amount FROM history ORDER BY history.time")
class class1(object):
    def fonk1(self, b7: str, opening_balance: b2 = 0):
        b3 = b1.execute("SELECT b7, b10 FROM accounts WHERE (b7 = ?)", (b7,))
        b4 = b3.fetchone()
        if b4 is not None:
            self.b7, self.b5 = b4
            print("Retrieved b10 for {}".format(self.b7), b6 = "")
        else:
            self.b7 = b7
            self.b5 = opening_balance / 100
            b3.execute("INSERT INTO accounts VALUES (?, ?)", (b7, opening_balance))
            b3.connection.commit()
            print("class1 created for {0.b7}".format(self))
        self.fonk2()
    def fonk2(self):
        print("Balance on account {0.b7} is {0.b5}".format(self))
    def fonk3(self):
        return datetime.datetime.now(pytz.timezone('UTC'))
    def fonk4(self, amount: b2) -> float:
        if amount > 0.0:
            self.fonk6(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self.b5
    def fonk5(self, amount: b2) -> float:
        if self.b5 > amount > 0.0:
            self.fonk6(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return self.b5
        else:
            print("Amount must be more than zero and less than your account b10.")
            return self.b5
    def fonk6(self, amount):
        b8 = self.b5 + amount
        b9 = self.fonk3()
        b1.execute("UPDATE accounts SET b10 = ? WHERE (b7 = ?)", (b8, self.b7))
        b1.execute("INSERT INTO history VALUES (?, ?, ?)", (b9, self.b7, amount))
        b1.commit()
        self.b5 = b8
if b11 = = "__main__":
    b12 = class1("John")
    b12.fonk4(1010)
    b12.fonk4(10)
    b12.fonk4(10)
    b12.fonk5(30)
    b12.fonk2()
    b13 = class1("Terry")
    b14 = class1("Graham", 9000)
    b15 = class1("Eric", 7000)
    b16 = class1("Jordan", 8000)
    b16.fonk4(1000)
    b15.fonk4(2000)
    b15.fonk5(90000)
    b1.close()