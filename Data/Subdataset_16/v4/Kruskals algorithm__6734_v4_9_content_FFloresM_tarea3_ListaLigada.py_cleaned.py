class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, new_data):
        self.b1 = new_data
    def fonk5(self, new_next):
        self.b2 = new_next
class class2:
    def fonk6(self):
        self.b4 = None
        self.b5 = None
    def fonk7(self):
        return self.b4 is None
    def fonk8(self, item):
        b6 = class1(item)
        if self.fonk7():
            self.b4 = b6
            self.b5 = b6
        else:
            self.b5.fonk5(b6)
            self.b5 = b6
    def fonk9(self):
        b7 = self.b4
        a1 = 0
        while b7 is not None:
            a1 += 1
            b7 = b7.fonk3()
        return a1
    def fonk10(self, item):
        b7 = self.b4
        while b7 is not None:
            if b7.fonk2() == item:
                return True
            b7 = b7.fonk3()
        return False
    def fonk11(self, item):
        b7 = self.b4
        b8 = None
        b9 = False
        while b7 is not None and not b9:
            if b7.fonk2() == item:
                b9 = True
            else:
                b8 = b7
                b7 = b7.fonk3()
        if b9:
            if b8 is None:
                self.b4 = b7.fonk3()
            else:
                b8.fonk5(b7.fonk3())
            if b7 = = self.b5:
                self.b5 = b8
    def fonk12(self):
        b7 = self.b4
        while b7 is not None:
            print(b7.fonk2(), b10 = '')
            b7 = b7.fonk3()
            if b7 is not None:
                print(" ->", b10 = " ")
        print()
