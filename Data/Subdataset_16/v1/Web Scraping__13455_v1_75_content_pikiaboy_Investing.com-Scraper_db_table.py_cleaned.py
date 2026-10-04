import sqlite3
class class1:
    b1 = "commodity_prices.db"
    def fonk1(self, b2, b3):
        if not b2:
            raise RuntimeError("Invalid table b2")
        if not b3:
            raise RuntimeError("Invalid database b3")
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
            b9.append(dict(zip(b6, row)))
        return b9
    def fonk4(self, item):
        b10 = ", ".join(item.keys())
        b11 = ", ".join([f"'{v}'" for v in item.values()])
        b12 = self.b4.b12()
        b12.execute(f"INSERT OR IGNORE INTO {self.b2} ({b10}) VALUES ({b11})")
        self.b4.commit()
        return b12.lastrowid
    def fonk5(self, values, where):
        b13 = ", ".join([f"{k} = '{v}'" for k, v in values.items()])
        b14 = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
        b12 = self.b4.b12()
        b12.execute(f"UPDATE {self.b2} SET {b13} WHERE {b14}")
        self.b4.commit()
        return b12.rowcount
    def fonk6(self, start_date, end_date, commodity_type):
        b15 = f"SELECT Date, {commodity_type} FROM Prices WHERE Date BETWEEN '{start_date}' AND '{end_date}'"
        b16 = []
        for b9 in self.b4.execute(b15):
            b16.append(b9)
        return b16
    def fonk7(self):
        self.b4.fonk7()
b3 = {
    'Date': 'TEXT',
    'Commodity': 'TEXT',
    'Price': 'REAL'
}
b17 = class1('Prices', b3)
b17.fonk4({'Date': '2024-07-22', 'Commodity': 'Gold', 'Price': 1800.0})
print(b17.fonk3())
b17.fonk5({'Price': 1850.0}, {'Date': '2024-07-22', 'Commodity': 'Gold'})
print(b17.fonk6('2024-07-20', '2024-07-23', 'Gold'))
b17.fonk7()