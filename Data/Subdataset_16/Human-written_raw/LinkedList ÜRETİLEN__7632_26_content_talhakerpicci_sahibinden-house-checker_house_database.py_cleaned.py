import sqlite3
class class1():
    def fonk1(self,b1,b2,b3,b4,b5,b6,b7,b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
class class2():
    def fonk2(self):
        self.fonk3()
    def fonk3(self):
        self.b9 = sqlite3.connect("Sahibinden.db")
        self.b10 = self.b9.b10()
        b11 = "create table if not exists " \
                "Tbl_Posts (" \
                "Link text," \
                "Title text," \
                "Price text," \
                "M2 text," \
                "Date text," \
                "Neighborhood text," \
                "Room text," \
                "Img text);" \
                "create table if not exists " \
                "Tbl_Posts_Backup (" \
                "Link text," \
                "Title text," \
                "Price text," \
                "M2 text," \
                "Date text," \
                "Neighborhood text," \
                "Room text," \
                "Img text);" \
        self.b10.executescript(b11)
        self.b9.commit()
    def fonk4(self,link):
        b11 = "select * from Tbl_Posts where Link = @p1"
        self.b10.execute(b11,(link,))
        b12 = self.b10.fetchall()
        if (len(b12) == 0):
            return 0
        else:
            return 1
    def fonk5(self,class1,b13 = False):
        if (b13):
            b11 = "insert into Tbl_Posts_Backup values (@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8)"
        else:
            b11 = "insert into Tbl_Posts values (@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8)"
        self.b10.execute(b11,(class1.b1,class1.b2,class1.b3,class1.b4,class1.b5,class1.b6,class1.b7,class1.b8))
        self.b9.commit()
    def fonk6(self,day):
        b11 = "delete from tbl_posts where b5 like '%" + day + "%'"
        self.b10.execute(b11)
        self.b9.commit()