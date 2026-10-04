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
    def fonk2(self, b9 = "Sahibinden.b16"):
        self.b9 = b9
        self.b10 = None
        self.b11 = None
        self.fonk3()
    def fonk3(self):
        self.b10 = sqlite3.connect(self.b9)
        self.b11 = self.b10.b11()
        self.fonk4()
    def fonk4(self):
        b12 = self.b11.executescript(b12)
        self.b10.commit()
    def fonk5(self, link):
        b12 = "SELECT 1 FROM Tbl_Posts WHERE Link = ?"
        self.b11.execute(b12, (link,))
        return self.b11.fetchone() is not None
    def fonk6(self, b17, b13 = False):
        b14 = "Tbl_Posts_Backup" if b13 else "Tbl_Posts"
        b12 = f
        self.b11.execute(b12, (b17.b1, b17.b2, b17.b3, b17.b4, b17.b5, b17.b6, b17.b7, b17.b8))
        self.b10.commit()
    def fonk7(self, day):
        b12 = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.b11.execute(b12, (f"%{day}%",))
        self.b10.commit()
    def fonk8(self):
        if self.b10:
            self.b10.fonk8()
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
    b18 = b16.fonk5(b17.b1)
    print(f"class1 b18: {b18}")
    if not b18:
        b16.fonk6(b17)
        print("class1 added to database")
    b16.fonk7("2024-01-01")
    print("Posts cleared for the b5 2024-01-01")
    b16.fonk8()