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
    def fonk2(self, b9 = "Sahibinden.b17"):
        self.b9 = b9
        self.fonk3()
    def fonk3(self):
        self.b10 = sqlite3.connect(self.b9)
        self.b11 = self.b10.b11()
        self.fonk4()
    def fonk4(self):
        b12 = self.b11.executescript(b12)
        self.b10.commit()
    def fonk5(self, link):
        b12 = "SELECT * FROM Tbl_Posts WHERE Link = ?"
        self.b11.execute(b12, (link,))
        b13 = self.b11.fetchall()
        return len(b13) > 0
    def fonk6(self, house, b14 = False):
        b15 = "Tbl_Posts_Backup" if b14 else "Tbl_Posts"
        b12 = f"INSERT INTO {b15} VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.b11.execute(b12, (house.b1, house.b2, house.b3, house.b4, house.b5,
                                    house.b6, house.b7, house.b8))
        self.b10.commit()
    def fonk7(self, day):
        b12 = f"DELETE FROM Tbl_Posts WHERE Date LIKE '%{day}%'"
        self.b11.execute(b12)
        self.b10.commit()
if b16 = = "__main__":
    b17 = class2()
    b18 = class1("link1", "title1", "100000", "100", "2022-05-01", "Neighborhood1", "3+1", "image1.jpg")
    b19 = class1("link2", "title2", "150000", "120", "2022-05-02", "Neighborhood2", "2+1", "image2.jpg")
    b17.fonk6(b18)
    b17.fonk6(b19)
    print("class1 1 exists:", b17.fonk5("link1"))
    print("class1 3 exists:", b17.fonk5("link3"))
    b17.fonk7("2022-05-01")