
import sqlite3
class class1:
    b1 = "commodity_prices.db"
    def fonk1(self, b2, b3):
        if not b2:
            raise RuntimeError("invalid table b2")
        if not b3:
            raise RuntimeError("invalid database b3")
        self.b2 = b2
        self.b3 = b3
        self.b4 = sqlite3.connect(self.b1)
        self.fonk2()
    def fonk2(self):
        b5 = ', '.join(["%s %s" % (k, v) for k, v in self.b3.items()])
        self.b4.execute("CREATE TABLE IF NOT EXISTS %s (%s)" % (self.b2, b5))
        self.b4.commit()
    def fonk3(self, b6 = [], where={}):
        if not b6:
            b6 = [k for k in self.b3]
        b5 = ", ".join(b6)
        b7 = "SELECT %s FROM %s" % (b5, self.b2)
        if where:
            b8 = ["%s = '%s'" % (k, v) for k, v in where.items()]
            b7 += " WHERE " + ' AND '.join(b8)
        b9 = []
        for row in self.b4.execute(b7):
            b10 = {}
            for i in range(0, len(b6)):
                b10[b6[i]] = row[i]
            b9.append(b10)
        return b9
    def fonk4(self, item):
        b11 = ", ".join(item.keys())
        b12 = ", ".join(["'%s'" % v for v in item.values()])
        b13 = self.b4.b13()
        b13.execute("INSERT OR IGNORE INTO %s(%s) values (%s)" % (self.b2, b11, b12))
        b13.fonk7()
        self.b4.commit()
        return b13.lastrowid
    def fonk5(self, values, where):
        b14 = ", ".join(["%s = '%s'" % (k, v) for k, v in values.items()])
        b15 = " AND ".join(["%s = '%s'" % (k, v) for k, v in where.items()])
        b13 = self.b4.b13()
        b13.execute("UPDATE %s SET %s WHERE %s" % (self.b2, b14, b15))
        b13.fonk7()
        self.b4.commit()
        return b13.rowcount
    def fonk6(self, start_date, end_date, commodity_type):
        b16 = "SELECT Date, %s FROM Prices WHERE Date BETWEEN %s AND %s" %(commodity_type, start_date, end_date)
        b17 = []
        print(start_date)
        print(end_date)
        for b9 in self.b4.execute(b16):
            b17.append(b9)
        return b17
    def fonk7(self):
        self.b4.fonk7()