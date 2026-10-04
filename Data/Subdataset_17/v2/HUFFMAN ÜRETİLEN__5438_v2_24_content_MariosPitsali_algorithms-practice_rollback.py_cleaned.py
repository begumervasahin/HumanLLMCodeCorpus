import sqlite3
import datetime
import pytz
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute()
db.execute()
db.execute()
class Account:
    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print(f"Retrieved balance for {self.name}")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}")
        self.show_balance()
    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance / 100:.2f}")
    @staticmethod
    def current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
    def deposit(self, amount: int) -> float:
        if amount > 0:
            self._update_balance(amount)
            print(f"{amount / 100:.2f} deposited")
        return self._balance / 100
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._update_balance(-amount)
            print(f"{amount / 100:.2f} withdrawn")
        else:
            print("Amount must be more than zero and less than or equal to your account balance.")
        return self._balance / 100
    def _update_balance(self, amount: int):
        new_balance = self._balance + amount
        transaction_time = self.current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
        db.execute("INSERT INTO history (time, account, amount) VALUES (?, ?, ?)", (transaction_time, self.name, amount))
        db.commit()
        self._balance = new_balance
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
    db.close()