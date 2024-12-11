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
        while b7.b1 != b1:
            b7 = b7.b2
            if b7 = = self.b6:
                return None
        return b7
    def fonk5(self):
        if self.b6 is None:
            print("List is empty")
            return
        b8 = self.b6
        while True:
            print("b3:", b8.b1.b3, "b4:", b8.b1.b4, "b5:", b8.b1.b5)
            b8 = b8.b2
            if b8 = = self.b6:
                break
        print("----------")
    def fonk6(self, newdata):
        b9 = class2(newdata.b3, newdata.b4, newdata.b5)
        if self.b6 is None:
            b9.b2 = b9
            self.b6 = b9
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b9
            b9.b2 = self.b6
    def fonk7(self, prevStudent, b9):
        b10 = self.fonk4(prevStudent)
        if b10 is None:
            print("Previous student not found in the list")
            return
        b11 = class2(b9.b3, b9.b4, b9.b5)
        b11.b2 = b10.b2
        b10.b2 = b11
    def fonk8(self, b3, b4):
        if self.b6 is None:
            print("List is empty")
            return
        b7 = self.b6
        if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = self.b6.b2
            self.b6 = self.b6.b2
            return
        b12 = None
        while b7.b2 != self.b6:
            b12 = b7
            b7 = b7.b2
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                b12.b2 = b7.b2
                return
        if b7.b2 = = self.b6:
            print("class2 not found in the list")
    def fonk9(self):
        if self.b6 is None:
            print("List is empty")
            return
        b12 = None
        b13 = self.b6
        while b13.b2 != self.b6:
            b14 = b13.b2
            b13.b2 = b12
            b12 = b13
            b13 = b14
        b13.b2 = b12
        self.b6.b2 = b13
        self.b6 = b13
    def fonk10(self, newhead):
        b15 = self.fonk4(newhead)
        if b15 is not None:
            self.b6 = b15
def fonk11():
    b16 = class3()
    b17 = class2("meri", "111", "3.0")
    b16.fonk6(b17)
    b16.fonk5()
    b16.fonk9()
    b16.fonk5()
if b18 = = "__main__":
    fonk11()