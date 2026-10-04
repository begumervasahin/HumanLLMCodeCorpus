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
        self.b9 = sqlite3.connect("Sahibinden.b15")
        self.b10 = self.b9.b10()
        b11 = self.b10.executescript(b11)
        self.b9.commit()
    def fonk4(self, link):
        b11 = "SELECT 1 FROM Tbl_Posts WHERE Link = ?"
        self.b10.execute(b11, (link,))
        return self.b10.fetchone() is not None
    def fonk5(self, b16, b12 = False):
        b13 = "Tbl_Posts_Backup" if b12 else "Tbl_Posts"
        b11 = f"INSERT INTO {b13} (Link, Title, Price, M2, Date, Neighborhood, Room, Img) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.b10.execute(b11, (b16.b1, b16.b2, b16.b3, b16.b4, b16.b5, b16.b6, b16.b7, b16.b8))
        self.b9.commit()
    def fonk6(self, day):
        b11 = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.b10.execute(b11, (f"%{day}%",))
        self.b9.commit()
if b14 = = "__main__":
    b15 = class2()
    b16 = class1(
        b1 = "http:
        b2 = "Beautiful class1",
        b3 = "500000",
        b4 = "120",
        b5 = "2024-01-01",
        b6 = "Downtown",
        b7 = "3+1",
        b8 = "http:
    )
    b17 = b15.fonk4(b16.b1)
    print(f"class1 b17: {b17}")
    if not b17:
        b15.fonk5(b16)
        print("class1 added to database")
    b15.fonk6("2024-01-01")
    print("Posts cleared for the b5 2024-01-01")