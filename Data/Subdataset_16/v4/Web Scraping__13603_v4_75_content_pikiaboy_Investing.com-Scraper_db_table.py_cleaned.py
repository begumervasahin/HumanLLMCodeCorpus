import sqlite3
class class1:
    b1 = "commodity_prices.db"
    def fonk1(self, b2, b3):
        if not b2:
            raise ValueError("Invalid table b2")
        if not b3:
            raise ValueError("Invalid database b3")
        self.b2 = b2
        self.b3 = b3
        self.b4 = sqlite3.connect(self.b1)
        self.fonk2()
    def fonk2(self):
        b5 = ', '.join([f"{k} {v}" for k, v in self.b3.items()])
        self.b4.execute(f"CREATE TABLE IF NOT EXISTS {self.b2} ({b5})")
        self.b4.commit()
    def fonk3(self, b6 = None, where=None):
        if b6 is None:
            b6 = list(self.b3.keys())
        b5 = ", ".join(b6)
        b7 = f"SELECT {b5} FROM {self.b2}"
        if where:
            b8 = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
            b7 += f" WHERE {b8}"
        b9 = []
        for row in self.b4.execute(b7):
            b10 = {b6[i]: row[i] for i in range(len(b6))}
            b9.append(b10)
        return b9
    def fonk4(self, item):
        b11 = ", ".join(item.keys())
        b12 = ", ".join([f"'{v}'" for v in item.values()])
        b13 = self.b4.b13()
        b13.execute(f"INSERT OR IGNORE INTO {self.b2} ({b11}) VALUES ({b12})")
        self.b4.commit()
        return b13.lastrowid
    def fonk5(self, values, where):
        b14 = ", ".join([f"{k} = '{v}'" for k, v in values.items()])
        b15 = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
        b13 = self.b4.b13()
        b13.execute(f"UPDATE {self.b2} SET {b14} WHERE {b15}")
        self.b4.commit()
        return b13.rowcount
    def fonk6(self, start_date, end_date, commodity_type):
        b16 = f"SELECT Date, {commodity_type} FROM Prices WHERE Date BETWEEN '{start_date}' AND '{end_date}'"
        b17 = []
        for b9 in self.b4.execute(b16):
            b17.append(b9)
        return b17
    def fonk7(self):
        self.b4.fonk7()