import sqlite3
import datetime
import pytz
class Account(object):
    def __init__(self, name: str, opening_balance: int = 0):
        self.db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
        self._initialize_tables()
        self._load_account(name, opening_balance)
    def _initialize_tables(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
        self.db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")
        self.db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, history.account, history.amount FROM history ORDER BY history.time")
    def _load_account(self, name: str, opening_balance: int):
        cursor = self.db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        if row is not None:
            self.name, self._balance = row
            print("Retrieved balance for", self.name, end="")
        else:
            self.name = name
            self._balance = opening_balance / 100
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for", self.name)
        self.show_balance()
    def show_balance(self):
        print("Balance on account", self.name, "is", self._balance)
    def current_time(self):
        return datetime.datetime.now(pytz.timezone('UTC'))
    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance
    def withdraw(self, amount: int) -> float:
        if self._balance > amount > 0.0:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return self._balance
        else:
            print("Amount must be more than zero and less than your account balance.")
            return self._balance
    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = self.current_time()
        self.db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        self.db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
        self.db.commit()
        self._balance = new_balance
    def __del__(self):
        self.db.close()
if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.show_balance()
    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    jordan = Account("Jordan", 8000)
    jordan.deposit(1000)
    eric.deposit(2000)
    eric.withdraw(90000)