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
        b11 = "SELECT * FROM Tbl_Posts WHERE Link = ?"
        self.b10.execute(b11, (link,))
        b12 = self.b10.fetchall()
        if len(b12) == 0:
            return 0
        else:
            return 1
    def fonk5(self, house, b13 = False):
        if b13:
            b11 = "INSERT INTO Tbl_Posts_Backup VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        else:
            b11 = "INSERT INTO Tbl_Posts VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.b10.execute(b11, (house.b1, house.b2, house.b3, house.b4, house.b5,
                                    house.b6, house.b7, house.b8))
        self.b9.commit()
    def fonk6(self, day):
        b11 = "DELETE FROM Tbl_Posts WHERE Date LIKE '%" + day + "%'"
        self.b10.execute(b11)
        self.b9.commit()
if b14 = = "__main__":
    b15 = class2()
    b16 = class1("link1", "title1", "100000", "100", "2022-05-01", "Neighborhood1", "3+1", "image1.jpg")
    b17 = class1("link2", "title2", "150000", "120", "2022-05-02", "Neighborhood2", "2+1", "image2.jpg")
    b15.fonk5(b16)
    b15.fonk5(b17)
    print("class1 1 exists:", b15.fonk4("link1"))
    print("class1 3 exists:", b15.fonk4("link3"))
    b15.fonk6("2022-05-01")