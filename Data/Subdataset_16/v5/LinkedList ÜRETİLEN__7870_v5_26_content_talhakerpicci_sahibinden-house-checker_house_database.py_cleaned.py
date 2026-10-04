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
    def fonk2(self, b9 = "Sahibinden.db"):
        self.b10 = sqlite3.connect(b9)
        self.b11 = self.b10.b11()
        self.fonk3()
    def fonk3(self):
        b12 = self.b11.executescript(b12)
        self.b10.commit()
    def fonk4(self, link):
        b12 = "SELECT 1 FROM Tbl_Posts WHERE Link = ?"
        self.b11.execute(b12, (link,))
        return self.b11.fetchone() is not None
    def fonk5(self, b17, b13 = False):
        b14 = "Tbl_Posts_Backup" if b13 else "Tbl_Posts"
        b12 = f
        self.b11.execute(b12, (
            b17.b1, b17.b2, b17.b3, b17.b4, b17.b5,
            b17.b6, b17.b7, b17.b8
        ))
        self.b10.commit()
    def fonk6(self, day):
        b12 = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.b11.execute(b12, (f'%{day}%',))
        self.b10.commit()
if b15 = = "__main__":
    b16 = class2()
    b17 = class1(
        b1 = "http:
        b2 = "Example class1",
        b3 = "100000",
        b4 = "100",
        b5 = "2023-07-27",
        b6 = "Example Neighborhood",
        b7 = "3+1",
        b8 = "http:
    )
    if not b16.fonk4(b17.b1):
        b16.fonk5(b17)