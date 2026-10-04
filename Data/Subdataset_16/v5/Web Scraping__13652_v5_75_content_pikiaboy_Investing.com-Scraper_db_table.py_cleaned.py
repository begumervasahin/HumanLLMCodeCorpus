import sqlite3
class class1:
    b1 = "commodity_prices.db"
    def fonk1(self, b2, b3):
        self.fonk2(b2, b3)
        self.b2 = b2
        self.b3 = b3
        self.b4 = sqlite3.connect(self.b1)
        self.fonk3()
    def fonk2(self, b2, b3):
        if not b2:
            raise ValueError("Invalid table b2")
        if not b3:
            raise ValueError("Invalid database b3")
    def fonk3(self):
        b5 = ', '.join([f"{col_name} {col_type}" for col_name, col_type in self.b3.items()])
        b6 = f"CREATE TABLE IF NOT EXISTS {self.b2} ({b5})"
        self.fonk8(b6)
    def fonk4(self, b7 = None, where=None):
        b7 = b7 or list(self.b3.keys())
        b5 = ", ".join(b7)
        b8 = f"SELECT {b5} FROM {self.b2}"
        if where:
            b9 = " AND ".join([f"{col} = '{val}'" for col, val in where.items()])
            b8 += f" WHERE {b9}"
        return self.fonk9(b8, b7)
    def fonk5(self, item):
        b10 = ", ".join(item.keys())
        b11 = ", ".join([f"'{val}'" for val in item.values()])
        b12 = f"INSERT OR IGNORE INTO {self.b2} ({b10}) VALUES ({b11})"
        return self.fonk8(b12)
    def fonk6(self, values, where):
        b13 = ", ".join([f"{col} = '{val}'" for col, val in values.items()])
        b14 = " AND ".join([f"{col} = '{val}'" for col, val in where.items()])
        b15 = f"UPDATE {self.b2} SET {b13} WHERE {b14}"
        return self.fonk8(b15)
    def fonk7(self, start_date, end_date, commodity_type):
        b16 = f"SELECT Date, {commodity_type} FROM Prices WHERE Date BETWEEN '{start_date}' AND '{end_date}'"
        return self.fonk9(b16)
    def fonk8(self, b8):
        b17 = self.b4.b17()
        b17.execute(b8)
        self.b4.commit()
        return b17.lastrowid if b17.description is None else b17.rowcount
    def fonk9(self, b8, b7 = None):
        b17 = self.b4.b17()
        b17.execute(b8)
        b18 = b17.fetchall()
        if b7:
            return [dict(zip(b7, row)) for row in b18]
        return b18
    def fonk10(self):
        self.b4.fonk10()