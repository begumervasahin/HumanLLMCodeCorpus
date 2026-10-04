import sqlite3
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
class class2:
    def fonk2(self):
        self.fonk3()
    def fonk3(self):
        self.b9 = sqlite3.connect("Sahibinden.b16")
        self.b10 = self.b9.b10()
        b11 = self.b10.executescript(b11)
        self.b9.commit()
    def fonk4(self, link):
        b11 = "SELECT * FROM Tbl_Posts WHERE Link = ?"
        self.b10.execute(b11, (link,))
        b12 = self.b10.fetchall()
        return len(b12) > 0
    def fonk5(self, b17, b13 = False):
        b14 = "Tbl_Posts_Backup" if b13 else "Tbl_Posts"
        b11 = f"INSERT INTO {b14} VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.b10.execute(b11, (b17.b1, b17.b2, b17.b3, b17.b4, b17.b5, b17.b6, b17.b7, b17.b8))
        self.b9.commit()
    def fonk6(self, day):
        b11 = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.b10.execute(b11, (f"%{day}%",))
        self.b9.commit()
if b15 = = "__main__":
    b16 = class2()
    b17 = class1(
        b1 = "http:
        b2 = "Beautiful class1",
        b3 = "500000",
        b4 = "120",
        b5 = "2024-01-01",
        b6 = "Downtown",
        b7 = "3+1",
        b8 = "http:
    )
    b18 = b16.fonk4(b17.b1)
    print(f"class1 b18: {b18}")
    if not b18:
        b16.fonk5(b17)
        print("class1 added to database")
    b16.fonk6("2024-01-01")
    print("Posts cleared for the b5 2024-01-01")