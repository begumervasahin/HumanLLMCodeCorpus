import sqlite3
import datetime
import pytz
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute()
db.execute()
db.execute()
class Account:
    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = self._retrieve_or_create_account(name, opening_balance)
        self.show_balance()
    def _retrieve_or_create_account(self, name: str, opening_balance: int) -> int:
        cursor = db.execute("SELECT balance FROM accounts WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            print(f"Retrieved balance for {name}")
            return row[0]
        else:
            db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, opening_balance))
            db.commit()
            print(f"Account created for {name}")
            return opening_balance
    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance / 100:.2f}")
    @staticmethod
    def current_time():
        return datetime.datetime.now(pytz.utc)
    def deposit(self, amount: int) -> float:
        if amount > 0:
            self._save_update(amount)
            print(f"{amount / 100:.2f} deposited")
        return self._balance / 100
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print(f"{amount / 100:.2f} withdrawn")
        else:
            print("Amount must be more than zero and less than your account balance.")
        return self._balance / 100
    def _save_update(self, amount: int):
        new_balance = self._balance + amount
        deposit_time = self.current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
        db.execute("INSERT INTO history (time, account, amount) VALUES (?, ?, ?)", (deposit_time, self.name, amount))
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