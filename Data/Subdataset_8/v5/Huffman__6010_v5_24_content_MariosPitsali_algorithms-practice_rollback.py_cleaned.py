import sqlite3
class Database:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
    def execute(self, query, params=None):
        cursor = self.connection.execute(query, params) if params else self.connection.execute(query)
        return cursor
    def commit(self):
        self.connection.commit()
    def close(self):
        self.connection.close()
class Account:
    def __init__(self, name: str, opening_balance: int = 0, db: Database = None):
        self.name = name
        self.db = db
        self._initialize_account(opening_balance)
    def _initialize_account(self, opening_balance: int):
        cursor = self.db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (self.name,))
        row = cursor.fetchone()
        if row is not None:
            self.name, self._balance = row
            print("Retrieved balance for {}".format(self.name), end="")
        else:
            self._create_account(opening_balance)
    def _create_account(self, opening_balance: int):
        self._balance = opening_balance / 100
        self.db.execute("INSERT INTO accounts VALUES (?, ?)", (self.name, opening_balance))
        self.db.commit()
        print("Account created for {}".format(self.name))
    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance))
    def deposit(self, amount: int) -> float:
        if amount > 0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance
    def withdraw(self, amount: int) -> float:
        if self._balance > amount > 0:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
        else:
            print("Amount must be more than zero and less than your account balance.")
        return self._balance
    def _save_update(self, amount: int):
        new_balance = self._balance + amount / 100
        deposit_time = self.current_time()
        self.db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        self.db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
        self.db.commit()
        self._balance = new_balance
    def current_time(self):
        return 1
if __name__ == "__main__":
    db = Database("accounts.sqlite")
    try:
        john = Account("John", db=db)
        john.deposit(1010)
        john.deposit(10)
        john.deposit(10)
        john.withdraw(30)
        john.show_balance()
        terry = Account("Terry", db=db)
        graham = Account("Graham", 9000, db=db)
        eric = Account("Eric", 7000, db=db)
        jordan = Account("Jordan", 8000, db=db)
        jordan.deposit(1000)
        eric.deposit(2000)
        eric.withdraw(90000)
    finally:
        db.close()