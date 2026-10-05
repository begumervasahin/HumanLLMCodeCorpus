class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class3:
    def fonk3(self):
        self.b6 = None
    def fonk4(self, b1):
        b7 = self.b6
        while b7.b1 is not b1:
            b7 = b7.b2
        return b7
    def fonk5(self):
        b8 = self.b6
        while b8 is not None:
            print ("b3:", b8.b1.b3, "b4:", b8.b1.b4, "b5:", b8.b1.b5)
            b8 = b8.b2
            if b8 = = self.b6:
                break
        print "----------"
    def fonk6(self, newdata):
        b9 = class2(newdata)
        b7 = self.b6
        b9.b2 = self.b6
        if self.b6 is  None:
            b9.b2 = b9
            self.b6 = b9
        else:
            while (b7.b2 != self.b6):
                b7 = b7.b2
            b7.b2 = b9
    def fonk7(self, prevStudent, b9):
        b10 = class2(b9)
        b11 = self.fonk4(prevStudent)
        if b11 is None:
            print("This b14 is not in the list")
        b10.b2 = b11.b2
        b11.b2 = b10
    def fonk8(self, b3, b4):
        b7 = self.b6
        while b7 is not None and b7.b2.b1 != b3 and b7.Id != b4:
            b7 = b7.b2
        b7.b2 = b7.b2.b2
    def fonk9(self):
        b12 = None
        b7 = self.b6
        while b7 is not None:
            b2 = b7.b2
            b7.b2 = b12
            b12 = b7
            b7 = b2
        self.b6 = b12
    def fonk10(self, newhead):
        b13 = self.fonk4(newhead)
        self.b6 = b13
def fonk11():
    b14 = class3()
    b15 = class2("meri","111","3.0")
    b14.fonk6(b15)
    b14.fonk9()
    b14.fonk7()
    b14.fonk8()
    b14.fonk10()
    b14.fonk9()
    b14.fonk5()
fonk11()